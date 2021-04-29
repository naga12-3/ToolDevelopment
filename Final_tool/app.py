from flask import Flask,render_template,request
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
# from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy
from gensim import corpora
from gensim import corpora, models, similarities, downloader
import operator

app=Flask(__name__)

count=0

from gensim.models import Word2Vec
import gensim.downloader as api


v2w_model=None
if(count==0):
    try:
        v2w__model=gensim.models.KeyedVectors.load("./w2vecmodel.mod")
        print("Loaded w2v model")
    except:
        v2w_model=api.load("word2vec-google-news-300")
        v2w_model.save("./w2vecmodel.mod")
        print("Saved w2v model")
    count+=1
else:
    print("Task done")
        
w2vec_embedding_size=len(v2w_model['computer'])



df=pd.read_csv("security_issues.csv")

stop_words = stopwords.words('english')

# import gensim
# from gensim.parsing.preprocessing import remove_stopwords
def remove_stopwords_fun(sentence):
    #words=sentence.split(' ')
    l=word_tokenize(sentence) # splitting into words
    f=[]
    for i in l:
        if i not in stop_words:
            f.append(i)
    s=''
    for i in f:
        s=s+i+' '
    return s
    

def clean_sentence(sentence,stopwords=False):
    sentence=sentence.lower().strip()
    sentence=re.sub(r'[^a-z0-9\s]','',sentence)
    if stopwords:
        sentence=remove_stopwords_fun(sentence)
    return sentence


def get_cleaned_sentences(df,stopwords=False):
    sents=df[['Issue']]
    cleaned_sentences=[]
    
    for  index,row in df.iterrows():
        cleaned=clean_sentence(row['Issue'],False)
        cleaned_sentences.append(cleaned)
    return cleaned_sentences

global dict1
def retrieve_security(question_embedding, sen_emb, faqdf, sentences):
    max_sim=-1
    index_sim=-1
    global dict1
    dict1={}
    matrix=[[0 for i in range(len(dictionary.items()))] for j in range(len(bow_corpus))]
    in1=0
    set1=set()
    for index, embedding in enumerate(sen_emb):
         sim=cosine_similarity(embedding,question_embedding)
         in1=in1+1
         #print(index, sim, sentences[index])
         dict1.update({sentences[index]:sim})


def getWordVec(word,model):
    samp=model['computer']
    vec=[0]*len(samp)
    try:
        vec=model[word]
    except:
        vec=[0]*len(samp)
    return (vec)

def getPhraseEmbedding(phrase,embeddingmodel):
    samp=getWordVec('computer', embeddingmodel)
    vec=numpy.array([0]*len(samp))
    den=0
    for word in phrase.split():
        den=den+1
        vec=vec+numpy.array(getWordVec(word,embeddingmodel))
    return vec.reshape(1,-1)

def know_link_from_issue(Issue):
    i=0
    for issues in df["Issue"]:
        if(clean_sentence(issues)==Issue):
            break;
        else:
            i+=1;
    return df["Link"][i],df["Status"][i]

def print_issues(dicti,num):
    cd = sorted(dicti.items(),key=operator.itemgetter(1),reverse=True)
    arr=[]
    for index,i in enumerate(cd[ :num]):
        #print(i)
        print(index+1,i[0])
        st=know_link_from_issue(i[0])
        print(st[0]," -- ",st[1])
        print()
        arr.append([i[0],st[0],st[1]])
    return arr

cleaned_sentences=get_cleaned_sentences(df,stopwords=False)
sentences=cleaned_sentences
sentence_words=[[word for word in document.split()] for document in sentences]



dictionary=corpora.Dictionary(sentence_words)    
bow_corpus=[dictionary.doc2bow(text) for text in sentence_words]







@app.route('/')
def home():
    global dict1
    dict1={}
    return render_template('home.html',data2=len(dict1))
    #return "<h1>hello</h1>"
@app.route('/predict',methods=['POST'])
def predict():
    input1=request.form['query']
    input_question=input1
    question_org=input_question
    question=clean_sentence(question_org,stopwords=False)
    question_embedding=dictionary.doc2bow(question.split())
    sent_embeddings=[]

    for sent in cleaned_sentences:
        sent_embeddings.append(getPhraseEmbedding(sent,v2w_model))
        #print(rohit)
        
    question_embedding=getPhraseEmbedding(question,v2w_model)

    retrieve_security(question_embedding,sent_embeddings,df,cleaned_sentences)
    #print_issues(dict1,15)
    global dict1
    data11=print_issues(dict1,20)
    return render_template('home.html',data1=data11,data2=len(dict1),data3=input1)


# @app.route('/')
# def home():
#     global dict1
#     dict1={}
#     return render_template('index.html',data2=len(dict1))

# @app.route('/predict',methods=['POST'])
# def predict():
#     input1=request.form['owner']
#     input_question=input1
#     question_org=input_question
#     question=clean_sentence(question_org,stopwords=False)
#     question_embedding=dictionary.doc2bow(question.split())
#     sent_embeddings=[]

#     for sent in cleaned_sentences:
#         sent_embeddings.append(getPhraseEmbedding(sent,v2w_model))
#         #print(rohit)
        
#     question_embedding=getPhraseEmbedding(question,v2w_model)

#     retrieve_security(question_embedding,sent_embeddings,df,cleaned_sentences)
#     #print_issues(dict1,15)
#     global dict1
#     data11=print_issues(dict1,20)
#     return render_template('index.html',data1=data11,data2=len(dict1))

if __name__=="__main__":
    app.run(debug=True)