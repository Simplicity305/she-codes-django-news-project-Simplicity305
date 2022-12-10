from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm



class IndexView(generic.ListView): #class based views 
    template_name = 'news/index.html'

    def get_queryset(self): #talks about newstory model 
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4] #get all news stories but only take the first 4 and those are the latest stories 
        context['all_stories'] = NewsStory.objects.all()
        return context


class StoryView(generic.DetailView): #View for a single story
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView): #View to use the form
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form): #This function gets called when the form is valid - can test submitting a form without anything in it 
        form.instance.author = self.request.user #logic to set the current user as the author. 
        return super().form_valid(form)

    