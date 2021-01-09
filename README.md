# Inforamtion-retrieval-project
A django powerd website that uses tf-ifd matrix similarity to match query to documents

## General information
This is a website that uses a django powerd server. The website has four main pages. Home which is the home screen. Emily Dickinson, where you can search the works 
of the poet Emily Dickinson. Tales from the Norse, where you can seach for folktales from scandinavia. Italian recipes where you can search for recipes from a
collection of italian recipes. All the documents are already inserted in to the database so it is not necessary to add to it if you just want to try it.

## Dependencies 
This project uses some external libraries from the standard python library. These libraries are: \
django \
gensim \
nltk

## Structure and files

### retriever.py & searchEngine directory
The main component of this project is the retrieval mechanism and is written in retriever.py. \
\
In retriever.py you can find the functions that are responsible for processing the query, processing raw documents, making the tf-idf model and computing 
similarites between query and document.\
\
retriver.py file lies in the searchEngine document which can be found in:

````
ir_system/src/ir_system/ir_website
````
seachEngine contains also every other IR relevant files such as the saved td-idf models and similarity matrcies for the different document collections.

### templates directory
The templates directory contains the html files for all the pages under a sub-directory called ir_website.\
You can find the html templates in the path of:
````
ir_system/src/ir_system/ir_website/templates/ir_website
````
### ir_website directory
This directory in addition to the once mentioned above also contain all app related files for the django server. Here you can find.
models.py \
admin.py \
urls.py \
views.py \
test.py \
apps.py \
\
The path for this directory is:
````
ir_system/src/ir_system/ir_website
````
### ir_system directory
The ir_system directory contains the django settings.py and urls.py. /
The path for this directory is:
````
ir_system/src/ir_system
````

### commands directory
The commands directory is where all the custom manage.py commands are written. \
The custom commands that are written here are for inserting the processed documents in to tables in the database. \
The commands that are written are written in the files: \
loadEmilyDickinsonToDatabase.py \
loadTalesFromTheNorseToDatabase.py \
loadItalianRecipesToDatabase.py \
these are inwoked py running:
````
python manage.py "name of the python file"
````
\
The path of this directory is:
````
ir_system/src/ir_website/management/commands
````
## SECRET_KEY
In settings.py it is important that you make a secret key for the applicartion, this has been removed when oploaded to github and needs to be added again

## Creating an admin
To create an admin, you you navigate to the same directory that manage.py is in and run the command:
`````
python manage.py createsuperuser
`````

## Running server
To run the server localy, you navigate to the same directory that manage.py is in and run the command:
```
python manage.py runserver
```
## Adding new files to the database
