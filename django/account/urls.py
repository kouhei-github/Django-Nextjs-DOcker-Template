from django.urls import path, include

from . import views

urlpatterns = [
    path('users/', views.UserViewSet.as_view()),
    path('exist-email/', views.UserEmailExist.as_view()),
    path('users/password-update/', views.UserPassWordSettingView.as_view()),
]
