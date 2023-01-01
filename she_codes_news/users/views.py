from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from news.models import NewsStory
from django.shortcuts import get_object_or_404

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'



class UserProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'news/userProfile.html'
    context_object_name = 'userProfile'
    
    def get_object(self, queryset=None): #TODO understand queryset a bit more
        return get_object_or_404(CustomUser, username=self.kwargs['username'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        stories = NewsStory.objects.filter(author=user)
        context['stories'] = stories
        return context
    
    #TRYING TO ADD AUTHORS STORIES TO USER PROFILE 
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user = self.get_object()
    #     context['user_stories'] = user.news_stories.all()
    #     return context
    
    #calls CustomUser.objects.get based on that username 
    #eg queryset, subset all users that have an id greater than 10 

        # return CustomUser.objects.filter(username__contains="wen").first()
