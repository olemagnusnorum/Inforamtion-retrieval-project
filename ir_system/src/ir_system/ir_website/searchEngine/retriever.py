"""file of important methods for IR and Tf-Idf similarityModel"""
import gensim
from nltk.stem.porter import PorterStemmer
import codecs
import string


def poemProcessingDickinson():
    """make one func for poems of emily dickinson, returns a list of her poems"""
    #opens the file and reads the text and store it
    f = codecs.open("ir_website/searchEngine/poemsByEmilyDickinsons.txt", "r", "utf-8")
    rawFile = f.readlines()
    #closes the file
    f.close()

    #put the list of lines in to one long string
    rawFileString = "".join(rawFile)
    #separates into list of paragraphs to get a list of poems 
    rawListOfPoems = rawFileString.split("\r\n\r\n\r\n\r\n\r\n")
    #removes empty poems
    for i in range(len(rawListOfPoems)-1,-1,-1):
        if rawListOfPoems[i] == "":
            del rawListOfPoems[i]
    #goes through an removes the newlines/those \r things at the beginning of each poem 
    #and removes every poem that does not star with a roman numeral
    #here we check the two first characters to see if it is "\r\n"
    for i in range(len(rawListOfPoems)-1,-1,-1):
        if rawListOfPoems[i][0:2] == "\r\n":
            count = 0
            #here we remove all the consecutive "\r\n" so that we kan filter on roman numerals
            for j in range(0,len(rawListOfPoems[i]),2):
                if rawListOfPoems[i][j:j+2] == "\r\n":
                    count += 2
                else: 
                    break
            #removes all the consecutive "\r\n"'s
            rawListOfPoems[i] = rawListOfPoems[i][count:]
        #filter on if the doc starts with roman numerals
        if rawListOfPoems[i][0] not in "IVXL":
            del rawListOfPoems[i]
    #returns all docs that are poems that start with roman numerals
    return rawListOfPoems

"""this part can be done by one function that takes in pultiple docs as a list and does IR shit on them"""

def processingTalesFromTheNorse():
    #opens the file and reads the text and store it
    f = codecs.open("ir_website/searchEngine/talesFromTheNorse.txt", "r", "utf-8")
    rawFile = f.readlines()
    #closes the file
    f.close()
    #put the list of lines in to one long string
    rawFileString = "".join(rawFile)
    rawListOfTales = rawFileString.split("\r\n\r\n\r\n\r\n\r\n")
    #remove empty tales
    for i in range(len(rawListOfTales)-1,-1,-1):
        if rawListOfTales[i] == "":
            del rawListOfTales[i]
    del rawListOfTales[0]
    del rawListOfTales[-2:]
    #removes all docs that is not a tale in the start
    count = 0
    hitCount = 0
    for i in range(len(rawListOfTales)):
        if "TRUE AND UNTRUE" in rawListOfTales[i]:
            hitCount += 1
            if hitCount == 2:
                break
        count += 1
    rawListOfTales = rawListOfTales[count:]
    #returns the tales as alist of tales
    return rawListOfTales

def processItalianRecipes():
    #opens the file and reads the text and store it
    f = codecs.open("ir_website/searchEngine/italianRecipes.txt", "r", "utf-8")
    rawFile = f.readlines()
    #closes the file
    f.close()

    #put the list of lines in to one long string
    rawFileString = "".join(rawFile)
    rawListOfRecipes = rawFileString.split("* Exported from MasterCook *")
    for index in range(len(rawListOfRecipes)):
        rawListOfRecipes[index] = rawListOfRecipes[index][:-20]
        count = 0
        for j in range(len(rawListOfRecipes[index])-1,-1,-1):
            if rawListOfRecipes[index][j] in " \r\n-":
                count += 1
            else:
                rawListOfRecipes[index] = rawListOfRecipes[index][:-count]
                break
    #returns a list of recipes
    return rawListOfRecipes

def calcualteTfIdfMatrix(listOfDocs):
    """calculates and return a tf-idf matrix based on the corpus it is given"""
    """Returns similiarityMatrix, tf-idf-model, dictionary of terms"""
    stemmer = PorterStemmer()

    #making a list of the common stopwords in english
    storpWordFile= codecs.open("ir_website/searchEngine/common-english-words.txt", "r", "UTF-8")
    stopWordList = storpWordFile.readlines()
    stringStopWords = "".join(stopWordList)
    stopWordList = stringStopWords.split(",")


    """sets every letter to lower case and replaces every \n with spaces, and splits them inn to a list of words
    now every poem is a list of words so poemsByDikinson is a list of a list of words (poems)"""
    for i in range(len(listOfDocs)):
        listOfDocs[i] = listOfDocs[i].lower()
        listOfDocs[i] = listOfDocs[i].replace("\n", " ")
        listOfDocs[i] = listOfDocs[i].split(" ")
        #here we remove punctuations
        for j in range(len(listOfDocs[i])):
            word = listOfDocs[i][j]
            listOfDocs[i][j] = word.translate(str.maketrans("","",string.punctuation+"\r\n\t"))

    #deletes every empty word in every docs
    for i in range(len(listOfDocs)-1,-1,-1):
        for j in range(len(listOfDocs[i])-1,-1,-1):
            if listOfDocs[i][j] == "":
                del listOfDocs[i][j]

    #stemmes every word in every document
    for i in range(len(listOfDocs)):
        for j in range(len(listOfDocs[i])):
            listOfDocs[i][j] = stemmer.stem(listOfDocs[i][j])

    #makes a dictionary of the stemmed terms over the document set
    dictionaryOfTerms = gensim.corpora.Dictionary(listOfDocs)

    #stemming the stopword list
    for i in range(len(stopWordList)):
        stopWordList[i] = stemmer.stem(stopWordList[i])

    #making a list with the stopwords IDs
    stopWordIDs = []
    for stopword in stopWordList:
        if stopword in dictionaryOfTerms.token2id:
            stopWordIDs.append(stopword)


    #removes the stopwords from the list of stemmed terms
    dictionaryOfTerms.filter_tokens(bad_ids=stopWordIDs)

    #makes a list of bag of words for each doc
    #bag of words is basicly a dictionary of what words the doc has and how many times it is used
    bagOfWordsList = []
    for i in range(len(listOfDocs)):
        bagOfWordsList.append(dictionaryOfTerms.doc2bow(listOfDocs[i]))

    #build a tf-idf model based on the documents and the bagOfWordsList
    tf_idf_model = gensim.models.TfidfModel(bagOfWordsList)

    #mapping the tf-idf model to the bagOfWordsList
    tf_idf_corpusList = []
    #print(bagOfWordsList)
    #print(tf_idf_model)
    for i in bagOfWordsList:
        tf_idf_corpusList.append(tf_idf_model[i])

    #making the similarity matrix based on the tf-idf corpus list
    #print(tf_idf_corpusList)
    similarityMatrixForTfIdf = gensim.similarities.MatrixSimilarity(tf_idf_corpusList)

    return similarityMatrixForTfIdf, tf_idf_model, dictionaryOfTerms

#function for preprocessing the querry
def queryStandariation(query):
    """preprocesses the query and returns a list of words"""
    stemmer = PorterStemmer()
    lowerCaseQuery = query.lower()
    withoutPunctQuery = lowerCaseQuery.translate(str.maketrans("", "", string.punctuation))
    queryWordList = withoutPunctQuery.split(" ")
    for j in range(len(queryWordList)-1, -1, -1):
        if queryWordList[j] == "":
            del queryWordList[j]
        else:
            stemmedWord = stemmer.stem(queryWordList[j])
            queryWordList[j] = stemmedWord
    return queryWordList

def simQueryDocs(standarizedQuery, dictionaryOfTerms, tf_idf_model, similarityMatrixForTfIdf):
    """function that takes a standarized query (list of words) and rank the most relevant documents"""
    """returns the tupel (x,y) with the index = x and value = y to the top ranked document"""
    #makes a bag of words for query
    query2Bow = dictionaryOfTerms.doc2bow(standarizedQuery)
    #gets the term weights for the query
    tdf_idf_representationOfQuery = tf_idf_model[query2Bow]
    #computes each docs simelarity to the query, and says how god the match is and what index it is in a tupel (index, matchScore)
    rankedQueryDocSimilarity = enumerate(similarityMatrixForTfIdf[tdf_idf_representationOfQuery])
    #index to the best matching doc
    indexToDoc = sorted(rankedQueryDocSimilarity, key=lambda kv: -kv[1])
    firstMatch = indexToDoc[0]
    return firstMatch


#functions for saving and loading dictionaries, models, and matrixes
def saveDictionary(dictionary, file):
    dictionary.save(file)

def loadDictionary(file):
    return gensim.corpora.Dictionary.load(file)

def saveTfIdfModel(TfIdfModel, file):
    TfIdfModel.save(file)

def loadTfIdfModel(file):
    return gensim.models.TfidfModel.load(file)

def saveSimilarityMatrix(similarityMatrix, file):
    similarityMatrix.save(file)

def loadSimilarityMatrix(file):
    return gensim.similarities.MatrixSimilarity.load(file)


#Testing ground______________________________________________________
if __name__ == "__main__":  
     
    
    """    listOfNorseTales = processingTalesFromTheNorse()
    print(listOfNorseTales[0])
    similarity, tfidmodel, dictionary = calcualteTfIdfMatrix(listOfNorseTales)
    dictionary.save("talesFromTheNorseDictionary.sav")
    tfidmodel.save("talesFromTheNorseTfIdfModel.sav")
    similarity.save("talesFromTheNorseSimilarityMatrix.sav")
    
    listOfDocs = poemProcessingDickinson()
    OrginalListOfDocs = listOfDocs.copy()

    #similarity, tfidfmodel, dictionary = calcualteTfIdfMatrix(listOfDocs)

    #dictionary.save("dictionary.sav")
    #tfidfmodel.save("saveTest.sav")
    #similarity.save("similarityMatrix.sav")


    dictionaryTest = gensim.corpora.Dictionary.load("dictionary.sav")

    tfidfmodelTest = gensim.models.TfidfModel.load("saveTest.sav")

    similarityTest = gensim.similarities.MatrixSimilarity.load("similarityMatrix.sav")

    testQuery = queryStandariation("the chariot deth for stop")
    index = simQueryDocs(testQuery, dictionaryTest, tfidfmodelTest, similarityTest)

    print(OrginalListOfDocs[index])  """

