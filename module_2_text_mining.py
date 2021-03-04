import pandas as pd
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


#creating a reference to the csv file
filename="first_data_ethereum_go-ethereum.csv"
df=pd.read_csv(filename)

#print(df.columns)
#print(df.iloc[1])


#WordNetLemmatizer
wl=WordNetLemmatizer()

#porter stemmer
ps=PorterStemmer()

#list of stopwords 
stop_words = stopwords.words('english')

def clean_lemmatize(row):
	tx=str(row['issue'])
	#print(tx)
	txt=re.sub(r'[^\w\s]','',tx) # to remove punctuation and replace it with space

	#print(txt)
	l=word_tokenize(txt) # splitting into words
	#print(l)
	f=[]

	#remove stop word
	for i in l:
		if i not in stop_words:
			f.append(i)
	l=[]
	


	#lemmatize the words
	for i in f:
		v=wl.lemmatize(i)
		l.append(v.lower())
	return l

def clean_stemming(row):
	tx=str(row['issue'])
	#print(tx)
	txt=re.sub(r'[^\w\s]',' ',tx) # to remove punctuation
	#print(txt)
	l=word_tokenize(txt) # splitting into words
	#print(l)
	f=[]

	#remove stop word
	for i in l:
		if i not in stop_words:
			f.append(i)
	l=[]
	s=''

	#lemmatize the words
	for i in f:
		v=ps.stem(i)
		l.append(v.lower())
	return l



# Creating Lemmatized data
df['trimmed_list_lemmatize']=df.apply(clean_lemmatize,axis=1)

print(df['trimmed_list_lemmatize'].head())

df.to_csv(filename, index=False)

print('done stemming')

# Creating Stemming data

df['trimmed_list_stemming']=df.apply(clean_stemming,axis=1)

print(df['trimmed_list_stemming'].head())

df.to_csv(filename, index=False)

print('done stemming')








