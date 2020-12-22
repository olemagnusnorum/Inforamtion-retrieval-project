"""this is a file that holds the urls for the different views"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("secretsite/", views.secretsite, name="secretsite"),
    path("emilyDickinson/", views.emilyDickinsonView, name="emilyDickinson"),
    path("talesFromTheNorse/", views.talesFromTheNorseView, name="talesFromTheNorse"),
    path("italianRecipes/", views.italianRecipesView, name="italianRecipes"),

]