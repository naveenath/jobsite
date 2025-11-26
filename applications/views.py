from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from jobs.models import Job
from core.models import Profile
from .forms import ApplicationForm
from .models import Application

@login_required
def apply_view(request, job_id):
    job = get_object_or_404(Job, pk=job_id, is_active=True)
    profile = Profile.objects.get(user=request.user)
    if profile.role != 'candidate':
        return redirect('jobs:detail', pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application, created = Application.objects.get_or_create(
                job=job,
                candidate=request.user,
                defaults=form.cleaned_data
            )
            if not created:
                # already applied; update resume/cover letter
                application.resume = form.cleaned_data['resume']
                application.cover_letter = form.cleaned_data['cover_letter']
                application.save()
            return redirect('jobs:detail', pk=job_id)
    else:
        form = ApplicationForm()
    return render(request, 'applications/apply_form.html', {'form': form, 'job': job})
