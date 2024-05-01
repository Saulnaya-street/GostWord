from django.urls import path
from myapp import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-elements/', views.add_elements, name='add_elements'),
    path('create-word-document/', views.create_word_document, name='create_word_document'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms_view, name='terms'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('confirm-logout/', views.confirm_logout, name='confirm_logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html', success_url='/password_change_done/'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
]
