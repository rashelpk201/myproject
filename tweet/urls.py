
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tweet import views



urlpatterns = [

    # Home & tweet views
    path('', views.home, name='home'),
    path('tweets/', views.tweet_list, name='tweet_list'),
    path('tweets/create/', views.tweet_create, name='tweet_create'),
    path('tweets/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('tweets/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('tweets/my-posts/', views.my_posts, name='my_posts'),
    path('tweets/<int:pk>/', views.tweet_detail, name='tweet_detail'),
    
    # Auth
    path('register/', views.register, name='register'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='tweet/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Password reset
    path('password-reset/', auth_views.PasswordResetView.as_view(
            template_name='tweet/password_reset.html',
            email_template_name='tweet/password_reset_email.html'
        ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='tweet/password_reset_done.html'
        ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='tweet/password_reset_confirm.html'
        ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
            template_name='tweet/password_reset_complete.html'
        ), name='password_reset_complete'),

    # Include app urls
   
]
