from django.urls import path

from api import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('adhd/', views.adhd, name='adhd'),
    # path('alzheimers/', views.alzheimers, name='alzheimers'),
    # path('autism/', views.autism, name='autism'),
    path('dyslexia/', views.dyslexia_modes, name='dyslexia_modes'),
    path('dyslexia/assessment/', views.assessment, name='assessment'),
    path('dyslexia/auditory/', views.dyslexia_auditory, name='dyslexia_auditory'),
    path('dyslexia/referrals/', views.referrals, name='referrals'),
    path('dyslexia/visual/', views.dyslexia_visual, name='dyslexia_visual'),
    path('referrals/', views.referrals, name='referrals'),
    path('scoring/', views.scoring, name='scoring'),
    path('<uuid:uuid>/results/', views.results, name='results'),
    path('<uuid:uuid>/email/', views.email, name='email'),
]
