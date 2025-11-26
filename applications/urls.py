from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('<int:job_id>/', views.apply_view, name='apply'),
]
