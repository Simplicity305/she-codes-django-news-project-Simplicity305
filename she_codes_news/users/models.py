from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser): #CustomUser class is inheriting from abstract user class - AbstractUser class is out of the box from Django - we get all of the stuff it comes with but we can amend and add it - might have to make your own models because Django doesnt have a concept for users for newsstory for eg - build on the existing class in Django 
    pass

    def __str__(self): #this function prints a string with your username (think back to example where the question was coming up as question object 1 but we want to see the actual question)
        return self.username


