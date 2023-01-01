from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm


# VIEW FOR THE HOMEPAGE
class IndexView(generic.ListView): #class based views 
    template_name = 'news/index.html'

    def get_queryset(self): #talks about newstory model 
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4] #get all news stories but only take the first 4 and those are the latest stories 
        context['all_stories'] = NewsStory.objects.all() #removed this to not show all the stories 
        return context

# VIEW FOR A SINGLE STORY
class StoryView(generic.DetailView): 
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

# VIEW FOR THE FORM TO CREATE A NEW STORY
class AddStoryView(generic.CreateView): 
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form): #This function gets called when the form is valid - can test submitting a form without anything in it 
        form.instance.author = self.request.user #logic to set the current user as the author. 
        return super().form_valid(form)


# VIEW WHERE ALL STORIES ARE DISPLAYED AND CAN BE SORTED
class AllStoriesView(generic.ListView):
    model = NewsStory 
    template_name = 'news/allStories.html'
    context_object_name = 'allStories'

    # FUNCTION TO RETRIEVE ALL STORIES 
    def get_queryset(self): #talks about newstory model 
        '''Return all news stories in reverse chronological order.'''
        return NewsStory.objects.all().order_by('-pub_date')
    
    
    
    
    