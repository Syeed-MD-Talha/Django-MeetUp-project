from django.db import models
from django.utils.text import slugify

# Create your models here.

class Participant(models.Model):
    email=models.EmailField()
    
    def __str__(self) -> str:
        return f"{self.email}"


class MeetupDetails(models.Model):
   description=models.TextField()
   organizer_name=models.CharField(max_length=200)
   organizer_email=models.CharField(max_length=200)
   time=models.DateTimeField()

   def __str__(self) -> str:
          return f"{self.organizer_name}"


class MeetUp(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True,blank=True)
    location=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')
    details=models.OneToOneField(MeetupDetails,on_delete=models.CASCADE,null=True,default=None)
    participants=models.ManyToManyField(Participant, blank=True,null=True,default=None)

    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = slugify(self.title)
        super().save(*args, **kwargs)
