pip install nltk
pip install newspaper3k
pip install lxml_html_clean

from newspaper import Article
import string
import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings("ignore")


nltk.download('punkt',quiet=True)


article=Article("") #--> any article page(link:http://example.com) that have information about thing that you are interested in
article.download()
article.parse()
article.nlp()
corpus=article.text

#tokenization
text=corpus
sentence_list=nltk.sent_tokenize(text)#list of sentence



#function to return random greeting response

def greeting_res(text):
    text=text.lower()
    
    bot_greeting=['how are you','hi','hey','hola','hello','hey there']
    user_greeting=['hi','hey','hello','wassup','hola']
    
    
    for word in text.split():
        if word in user_greeting:
            return random.choice(bot_greeting)





def index_sort(list_var):
    length=len(list_var)
    list_index=list(range(0,length))
    
    x=list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:

                temp=list_index[i]
                list_index[i]=list_index[j]
                list_index[j]=temp
       
    
    
        
    return list_index









  #bot response

def bot_res(user_input):
    user_input=user_input.lower()
    sentence_list.append(user_input)
    bot_res=""
    cm=CountVectorizer().fit_transform(sentence_list)
    similarity_scores=cosine_similarity(cm[-1],cm)
    similarity_scores_list=similarity_scores.flatten()
    index=index_sort(similarity_scores_list)
    index=index[1:]
    resp_flag=0
    
    j=0
    for i in range(len(index)):
        if similarity_scores_list[index[i]]> 0.0:
            bot_res=bot_res + ' '+sentence_list[index[i]]
            resp_flag=1
            j=j+1
        if j >2:
            break
            
            
    if resp_flag==0:
        bot_res=bot_res + ' '+ 'I APOLOGIZE ,I DONT UNDERSTAND.'
    
    
    sentence_list.remove(user_input)
    
    
    return bot_res






#start chat

print("Doc bot:i am bot from abdelrahman services")
exit_list=['exit','quit','break']
while(True):
    user_input=input()
    if user_input.lower() in exit_list:
        print("continue later")
        break
    
    else:
        if greeting_res(user_input) != None:
            print("Bot:"+greeting_res(user_input))
        else:
            print("Bot:"+bot_res(user_input) )
