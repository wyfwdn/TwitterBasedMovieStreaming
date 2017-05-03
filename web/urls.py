"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from movie import views as movie_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^where/', movie_views.where, name='where'),
    url(r'^recommendation/', movie_views.recommendation, name='recommendation'),
    url(r'^add/$', movie_views.add, name='add'),
    url(r'^addlist/$', movie_views.addlist, name='addlist'),
    url(r'^post/$', movie_views.post, name='post'),
    url(r'^$', movie_views.index0, name='main'),
    url(r'^hidden_figures/$', movie_views.hidden_figures, name='hidden_figures'),
    url(r'^get_out/$', movie_views.get_out, name='get_out'),
    url(r'^sleepless/$', movie_views.sleepless, name='sleepless'),
    url(r'^patriots_day/$', movie_views.patriots_day, name='patriots_day'),
    url(r'^alien_covenant/$', movie_views.alien_covenant, name='alien_covenant'),
    url(r'^aftermath/$', movie_views.aftermath, name='aftermath'),
    url(r'^going_in_style/$', movie_views.going_in_style, name='going_in_style'),
    url(r'^a_monster_calls/$', movie_views.a_monster_calls, name='a_monster_calls'),
    url(r'^the_bye_bye_man/$', movie_views.the_bye_bye_man, name='the_bye_bye_man'),
    url(r'^unforgettable/$', movie_views.unforgettable, name='unforgettable'),
    url(r'^a_cure_for_wellness/$', movie_views.a_cure_for_wellness, name='a_cure_for_wellness'),
    url(r'^the_circle/$', movie_views.the_circle, name='the_circle'),
    url(r'^the_promise/$', movie_views.the_promise, name='the_promise'),
    url(r'^the_lost_city_of_z/$', movie_views.the_lost_city_of_z, name='the_lost_city_of_z'),
    url(r'^colossal/$', movie_views.colossal, name='colossal'),
    url(r'^below_her_mouth/$', movie_views.below_her_mouth, name='below_her_mouth'),
    url(r'^stream/$', movie_views.stream, name='stream'),
]
