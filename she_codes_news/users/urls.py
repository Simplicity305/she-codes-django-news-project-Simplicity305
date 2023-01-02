from django.urls import path
from .views import CreateAccountView
from . import views # TODO Confirm why we didnt just do this in the first place and why we specified the CreateAccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('profile/<str:username>/', views.UserProfileView.as_view(), name='userProfile')
]
