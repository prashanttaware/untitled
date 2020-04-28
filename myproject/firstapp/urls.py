from django.urls import path

from . import views

urlpatterns = [
    path('<int:course_id>/', views.details, name='details'),
    path('', views.courses, name='courses'),
]

