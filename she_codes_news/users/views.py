from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.shortcuts import get_object_or_404

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'


class UserProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/userProfile.html'
    context_object_name = 'userProfile'
    
    def get_object(self, queryset=None): #TODO understand queryset a bit more
        return get_object_or_404(CustomUser, username=self.kwargs['author_username'])

    #calls CustomUser.objects.get based on that username 
    #eg queryset, subset all users that have an id greater than 10 

        return CustomUser.objects.filter(username__contains="wen").first()
