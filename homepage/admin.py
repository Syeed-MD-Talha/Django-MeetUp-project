from django.contrib import admin
from .models import MeetUp,MeetupDetails,Participant
# Register your models here.

class MeetUpAdmin(admin.ModelAdmin):
    list_display=('title','location')

admin.site.register(MeetUp,MeetUpAdmin)
admin.site.register(MeetupDetails)
admin.site.register(Participant)