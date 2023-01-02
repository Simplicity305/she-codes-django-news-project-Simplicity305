from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import NewsStory
from .forms import StoryForm


#-----------------------------------------
# HOME PAGE
#-----------------------------------------
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

#-----------------------------------------
# PAGE SHOWING ALL STORIES
#-----------------------------------------

#  TODO: Add logic 
#  - Show only x many stories

# VIEW WHERE ALL STORIES ARE DISPLAYED AND CAN BE SORTED
class AllStoriesView(generic.ListView):
    model = NewsStory 
    template_name = 'news/allStories.html'
    context_object_name = 'allStories'

    # FUNCTION TO RETRIEVE ALL STORIES 
    def get_queryset(self): #talks about newstory model 
        '''Return all news stories in reverse chronological order.'''
        return NewsStory.objects.all().order_by('-pub_date')
    

#-----------------------------------------
# PAGE SHOWING A SINGLE STORY
#-----------------------------------------

class StoryView(generic.DetailView): 
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

#-----------------------------------------
# FORM WHERE USER CREATES A NEW STORY
#-----------------------------------------

class AddStoryView(generic.CreateView): 
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form): #This function gets called when the form is valid - can test submitting a form without anything in it 
        # Guard against anonymous submissions
        
        if (self.request.user.is_anonymous):
            return redirect('login')
            # return HttpResponseForbidden()
            # return super().form_invalid(form)
        
            # NOTE: User not logged in won't be able to see the form due to logic in createStory.html, but unsure if this is sufficient to disable the functionality (e.g. could someone use something like Postman?). Tried a redirect for now - as a customer friendly approach. 
            # TODO: Look further into other approaches - forbidden response, error message etc - how do others handle these situations? Is this over-engineering? 
            
            
    # def form_valid(self, form):
    #     # Guard against anonymous submissions
    #     if self.request.user.is_anonymous:
    #         messages.error(self.request, 'You must be logged in to create a new story.')
    #         return self.render_to_response(self.get_context_data(form=form))    
        
        # Record Author
        form.instance.author = self.request.user #logic to set the current user as the author. 
        return super().form_valid(form)

#-----------------------------------------
#  EDITING A STORY 
#-----------------------------------------

class EditStoryView(generic.UpdateView):
    model = NewsStory
    form_class = StoryForm
    template_name = 'news/editStory.html'
    context_object_name = 'editStory'
    success_url = reverse_lazy('news:index')
    
    def get_object(self):
        return get_object_or_404(NewsStory, pk=self.kwargs.get('pk'))
    

        