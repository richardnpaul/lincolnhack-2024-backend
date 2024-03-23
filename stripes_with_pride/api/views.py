from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def dyslexia_modes(request):
    return render(request, 'dyslexia_modes.html', {'title': 'Dyslexia'})

def dyslexia_visual(request):
    return render(request, 'dyslexia_visual.html', {'title': 'Dyslexia Visual'})

def dyslexia_auditory(request):
    return render(request, 'dyslexia_auditory.html', {'title': 'Dyslexia Auditory'})
