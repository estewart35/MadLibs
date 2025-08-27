from .models import MadLibTemplate

def madlibs(request):
    madlibs = MadLibTemplate.objects.all()
    return {'madlibs': madlibs}