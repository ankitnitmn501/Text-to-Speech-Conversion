# Description : This program takes  text from an online article and converts it into speech

# importing libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os

# get the online article
article = Article('https://medium.com/@who/seven-simple-steps-to-protect-yourself-and-others-from-covid-19-83898c2eb972')

article.download()  # download the article

article.parse() # parsing the article

nltk.download('punkt') #download the punkt package

article.nlp() #apply nlp(natural language processing)

# get the article text into a variable called mytext

mytext = article.text

# print the text

print(mytext)

language = 'en' # English

myobj = gTTS(text=mytext, lang = language, slow = False)

# save the converted audio to a file

myobj.save('read_article.mp3')


#play the converted file

os.system('start read_article.mp3')

