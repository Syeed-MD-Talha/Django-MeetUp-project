from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.views import View
from .models import MeetUp,Participant
from .forms import RegistrationForm
from django.urls import reverse
# Create your views here.

class registration(View):
    def get(self,request,slug):
        print('------------------ Get Method---------------')
        meetup=get_object_or_404(MeetUp,slug=slug)
        # Print all participant emails
        participants = meetup.participants.all()
        for participant in participants:
            print(participant.email)


        conference=MeetUp.objects.all()
        return render(request,'join_meetup.html',{
        'form':RegistrationForm(),
        'meetups':conference
    })

    def post(self,request,slug):
        print('------------------ Post Method ---------------')
        meetup=get_object_or_404(MeetUp,slug=slug)
        form=RegistrationForm(request.POST)
        if form.is_valid():
            print('valid.........')
            email=form.cleaned_data.get('email')
            print(email)
            participant, created = Participant.objects.get_or_create(email=email)
            meetup.participants.add(participant)

            # return redirect(request,'post_details',slug=slug)
            return redirect(reverse('post_details', kwargs={'slug': slug}))


        return render(request,'join_meetup.html',{
        'form':form
    })
        



class homepage(View):
    def get(self,request):
         conference=MeetUp.objects.all()
         return render(request,'index.html',{
                'meetups':conference,
                'show_meetup':True,
            })
                

def meetup_details(request,slug):
    try:
        meetup=MeetUp.objects.get(slug=slug)
        context={
            'meetup':meetup,
            'registration_open':True
        }
        return render(request,'meetup-details.html',context)
    except:
        return HttpResponse('<h1>404 page not found </h1>')
