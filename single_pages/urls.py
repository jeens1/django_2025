from django.urls import path
from.import views
#single_pages/views.py
urlpatterns=[
    path('',views.landing,name='landing'),
    path('aboutme/',views.aboutme,name='about')
]