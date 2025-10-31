from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('student/create/', views.create_student, name='create_student'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/edit/', views.edit_student, name='edit_student'),
    path('students/<int:pk>/delete/', views.delete_student, name='delete_student'),


    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="./login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

