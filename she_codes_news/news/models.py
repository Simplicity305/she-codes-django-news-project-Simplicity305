from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE
        ) #we want author to be a reference to a specific user - getusermodel -
    pub_date = models.DateTimeField()
    content = models.TextField()
    # Adding a field so a url (for image) can be stored. This is optional as defined by blank=True
    image_url = models.URLField(blank=True)
    

