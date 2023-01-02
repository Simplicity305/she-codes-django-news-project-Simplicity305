from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('all-stories/', views.AllStoriesView.as_view(), name='allStories'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('edit-story/<int:pk>/', views.EditStoryView.as_view(), name='editStory'),
    path('delete-story/<int:pk>/', views.DeleteStoryView.as_view(), name='deleteStory')
]
