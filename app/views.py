from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    My_skills=models.My_skills.objects.all()
    My_skills2 = models.My_skills2.objects.all()
    My_service=models.my_service.objects.all()
    Future_plane=models.Future_plane.objects.all()
    Why_trust=models.Why_trust.objects.all()
    return render(request, 'app/index.html', context={'My_skills': My_skills ,'My_skills2': My_skills2,'My_service':My_service,
                        'Future_plane':Future_plane,'Why_trust':Why_trust})
