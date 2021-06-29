from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_apis, name='api'),

    path('people', views.get_people, name='people'),
    path('people/students/', views.get_students, name='faculties'),
    path('people/staff/', views.get_staff, name='staff'),
    path('people/faculties/', views.get_faculties, name='faculties'),

    path('events', views.get_events, name='people'),
    path('events/conf-workshops-presentations/', views.get_work, name='faculties'),
    path('events/awards/', views.get_awards, name='staff'),
    path('events/talks/', views.get_talks, name='faculties'),

    path('home', views.get_home, name='home'),
    path('home/announcements/', views.get_announcements, name='announcements'),
    path('home/news/', views.get_news, name='news'),
    path('home/phd_awarded/', views.get_phd_awarded, name='phd_awarded'),


    path('research', views.get_projects, name='research'),
    path('committees', views.get_committees, name='committees'),
]
