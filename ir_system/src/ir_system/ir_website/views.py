from django.shortcuts import render
from django.http import HttpResponse
from .forms import searchPoemForm
from .searchEngine import retriever
from .models import EmilyDickinson, TalesFromTheNorse, ItalianRecipes



# Create your views here.

def home(response):
    #view for home screen
    return render(response, "ir_website/home.html", {})

def secretsite(response):
    return HttpResponse("<h1>shhh this is a secret site</h1>")


#lager denne for costum form
def emilyDickinsonView(response):
    #custom view for Emily Dickinson
    doc = "many of Dickinson's poems does not have names \n so this way you can discover her poems by searching query terms"
    if response.method == "POST":
        if response.POST.get("searchbutton"):
            query = response.POST.get("searchquery")
            if len(query) > 0:
                dictionary = retriever.loadDictionary("ir_website/searchEngine/dictionary.sav")
                tfidfmodel = retriever.loadTfIdfModel("ir_website/searchEngine/saveTest.sav")
                tfidfmatrix = retriever.loadSimilarityMatrix("ir_website/searchEngine/similarityMatrix.sav")
                query = retriever.queryStandariation(query)
                firstMatch = retriever.simQueryDocs(query, dictionary, tfidfmodel, tfidfmatrix)
                if firstMatch[1] == 0:
                    doc = "No poem matching the query"
                else:
                    #gets the document from database with the corresponding id
                    doc = EmilyDickinson.objects.get(id=firstMatch[0]).document
    return render(response, "ir_website/emilyDickinson.html", {"doc": doc})

def talesFromTheNorseView(response):
    #custum view for Tales from the Norse
    doc = "search for tales from the norse"
    if response.method == "POST":
        if response.POST.get("searchbutton"):
            query = response.POST.get("searchquery")
            if len(query) > 0:
                dictionary = retriever.loadDictionary("ir_website/searchEngine/talesFromTheNorseDictionary.sav")
                tfidfmodel = retriever.loadTfIdfModel("ir_website/searchEngine/talesFromTheNorseTfIdfModel.sav")
                tfidfmatrix = retriever.loadSimilarityMatrix("ir_website/searchEngine/talesFromTheNorseSimilarityMatrix.sav")
                query = retriever.queryStandariation(query)
                firstMatch = retriever.simQueryDocs(query, dictionary, tfidfmodel, tfidfmatrix)
                if firstMatch[1] == 0:
                    doc = "No tale matching the query"
                else:
                    doc = TalesFromTheNorse.objects.get(id=firstMatch[0]).document
    return render(response, "ir_website/talesFromTheNorse.html", {"doc": doc})

def italianRecipesView(response):
    #custum view for italian recipes
    doc = "search for italian recipes"
    if response.method == "POST":
        if response.POST.get("searchbutton"):
            query = response.POST.get("searchquery")
            if len(query) > 0:
                dictionary = retriever.loadDictionary("ir_website/searchEngine/italianRecipesDictionary.sav")
                tfidfmodel = retriever.loadTfIdfModel("ir_website/searchEngine/italianRecipesTfIdfModel.sav")
                tfidfmatrix = retriever.loadSimilarityMatrix("ir_website/searchEngine/italianRecipesSimilarityMatrix.sav")
                query = retriever.queryStandariation(query)
                firstMatch = retriever.simQueryDocs(query, dictionary, tfidfmodel, tfidfmatrix)
                if firstMatch[1] == 0:
                    doc = "no recipes matching the query"
                else:
                    doc = ItalianRecipes.objects.get(id=firstMatch[0]).document
    return render(response, "ir_website/italianRecipes.html", {"doc": doc})