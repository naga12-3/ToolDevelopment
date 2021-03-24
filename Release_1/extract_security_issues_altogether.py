import pandas as pd
import nltk
import re
import csv
import os
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


global data_list
data_list=['access policy', 'access role', 'access-policy', 'access-role', 'accesspolicy', 'accessrole', 'aes', 'audit', 
	'authentic', 'authority', 'authoriz', 'biometric', 'black list', 'black-list', 'blacklist', 'blacklist', 'cbc', 'certificate', 
	'checksum', 'cipher', 'clearance', 'confidentiality','cookie', 'crc', 'credential', 'crypt', 'csrf', 'decode', 'defensive programming', 
	'defensive-programming', 'delegation', 'denial of service', 'denial-of-service', 'difee-hellman', 'dmz', 'dotfuscator', 'dsa','ecdsa', 'encode',
	 'escrow', 'exploit', 'firewall', 'forge', 'forgery', 'gssapi', 'gss-api', 'gssapi', 'hack', 'hash', 'hmac', 'honey pot', 'honey-pot', 'honeypot',
	  'inject', 'integrity', 'kerberos', 'ldap', 'login', 'malware', 'md5', 'nonce', 'nss', 'oauth', 'obfuscat', 'open auth', 'open-auth', 'openauth', 'openid',
	   'owasp', 'password', 'pbkdf2', 'pgp', 'phish-ing', 'pki', 'privacy', 'private key', 'private-key', 'privatekey', 'privi-lege', 'public key', 'public-key',
	    'publickey', 'rbac', 'rc4', 'repudiation','rfc 2898', 'rfc-2898', 'rfc2898', 'rijndael', 'rootkit', 'rsa', 'salt', 'saml','sanitiz', 'secur', 'sha', 
	    'shell code', 'shell-code', 'shellcode', 'shib-boleth', 'signature', 'signed', 'signing', 'sing sign-on', 'single sign on', 'single-sign-on', 
	    'smart assembly', 'smart-assembly', 'smartassembly', 'snif', 'spam', 'spnego', 'spoofing', 'spyware', 'ssl', 'sso','steganography', 'tampering', 
	    'trojan', 'trust', 'violat', 'virus', 'whitelist', 'white-list', 'whitelist', 'x509', 'xss']


data_list+=['steal', 'parity', 'safest', 'metamask', 
	'address', 'wallet', 'proxy', 'tamper', 'crack', 'fake', 'verify', 'secure', 'impersonation', 'proof', 
	'proof of stake', 'check', 'self-destruct', 'destruct',  'cheat', 'danger', 'protect', 'selfdestruct', 'insecure',
	 'lock', 'unlock', 'hide', 'remote','security']

data_list+=['risk','manipulate','rely','strict','anonymity','conditional','duplicate','prone','prevent','audit','race conditional',
	 'restriction','spam','destroy','vulnerability','attack','safe','pattern']






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
	return str(l)

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
	return str(l)

def lemmat(f):
	l=[]
		


		#lemmatize the words
	for i in f:
		v=wl.lemmatize(i)
		l.append(v.lower())
	return l

def stemm(f):
	l=[]
	s=''

		#lemmatize the words
	for i in f:
		v=ps.stem(i)
		l.append(v.lower())
		#print(l)
	return l

def check_security(row):
	global val
	global csv_file
		#print(type(row['trimmed_list']))
	txt=row['trimmed_list_lemmatize'][1:len(row['trimmed_list_lemmatize'])-1].split(',')

		#print(txt)
	for i in range(len(txt)):
		ind1=txt[i].find('\'')
		ind2=txt[i].rfind('\'')
		txt[i]=txt[i][ind1+1:ind2]
	k=0
	for i in txt:
		if i in data_list:
			val+=1
			csv_file.writerow(row)
				#print(row['number'], row['issue'])
			k+=1;
			break
	if(k!=1):
		txt2=row['trimmed_list_stemming'][1:len(row['trimmed_list_stemming'])-1].split(',')
		for i in range(len(txt2)):
			ind11=txt2[i].find('\'')
			ind21=txt2[i].rfind('\'')
			txt2[i]=txt2[i][ind11+1:ind21]
		for i in txt2:
			if i in data_list:
				val+=1
				csv_file.writerow(row)
	            	
					#print(row['number'], row['issue'])
				break

#creating a reference to the csv file
filenames=["ethereum_EIPs.csv","ethereum_wiki.csv"]
count_file=0
data_list=data_list+stemm(data_list)+lemmat(data_list)
for filename in filenames:
	df=pd.read_csv(filename)
	# print(len(df))

	#print(df.columns)
	#print(df.iloc[1])


	#WordNetLemmatizer
	


	#  Creating Lemmatized data
	df['trimmed_list_lemmatize']=df.apply(clean_lemmatize,axis=1)
	# print(df['trimmed_list_lemmatize'].head())

	df.to_csv(filename, index=False)

	print('done lemmatization')

	# Creating Stemming data

	df['trimmed_list_stemming']=df.apply(clean_stemming,axis=1)

	# print(df['trimmed_list_stemming'].head())

	df.to_csv(filename, index=False)

	print('done stemming')


	


	

	

		#print(data_list)
	global val
	val=0
	def check_security_lemmatized(row):
		global val
		#print(type(row['trimmed_list']))
		txt=row['trimmed_list_lemmatize'][1:len(row['trimmed_list_lemmatize'])-1].split(',')
		#print(txt)
		for i in range(len(txt)):
			ind1=txt[i].find('\'')
			ind2=txt[i].rfind('\'')
			txt[i]=txt[i][ind1+1:ind2]
		k=0;
		for i in txt:
			for data in data_list:
				if i in data:
					val+=1
					#print(row['number'], row['issue'])
					k=1
					break
			if(k==1):
				break
	def check_security_stemming(row):
		global val
		#print(type(row['trimmed_list']))
		txt=row['trimmed_list_stemming'][1:len(row['trimmed_list_stemming'])-1].split(',')
		#print(txt)
		for i in range(len(txt)):
			ind1=txt[i].find('\'')
			ind2=txt[i].rfind('\'')
			txt[i]=txt[i][ind1+1:ind2]
		k=0
		'''for i in txt:
			for data in data_list:
				if i in data:
					val+=1
					print(row['number'], row['issue'])
					k=1
					break
			if(k==1):
				break'''
		for i in txt:
			if i in data_list:
				val+=1
				print(row['number'], row['issue'])
				break

	global csv_file
	file=open("final.csv", "a", encoding='utf-8')
	# fields = ['issue', 'number', 'state', 'link']
	csv_file = csv.writer(file)
	# cols = fields
	# csv_file.writerow(cols)
	






	for i in range(len(df)):
		#print(i,end='\t')
		check_security(df.iloc[i])

	#check_security(df.iloc[19])
	print(val)
	#print(stemm(data_list))


