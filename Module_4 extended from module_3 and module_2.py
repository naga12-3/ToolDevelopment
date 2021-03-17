import pandas as pd
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
#creating a reference to the csv file
filename="sample_file.csv"
df=pd.read_csv(filename)

print(df.columns)
print(df.iloc[1])
#WordNetLemmatizer
wl=WordNetLemmatizer()
ps=PorterStemmer()
stop_words = stopwords.words('english')
#remove stop word
def clean_lemmatize(row):
	tx=str(row['issue'])
	#print(tx)
	txt=re.sub(r'[^\w\s]','',tx) # to remove punctuation
	#print(txt)
	l=word_tokenize(txt) # splitting into words
	#print(l)
	f=[]
	for i in l:
		if i not in stop_words:
			f.append(i)
	l=[]
	s=''
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
	for i in l:
		if i not in stop_words:
			f.append(i)
	l=[]
	s=''
	for i in f:
		v=ps.stem(i)
		l.append(v.lower())
	return str(l)




#clean_stemming(df.iloc[12])
# Creating Lemmatized data
df['trimmed_list_lemmatize']=df.apply(clean_lemmatize,axis=1)

#print(df['trimmed_list_lemmatize'].head())

df.to_csv(filename, index=False)

# Creating Stemming data

df['trimmed_list_stemming']=df.apply(clean_stemming,axis=1)

#print(df['trimmed_list_stemming'].head())

df.to_csv(filename, index=False)
print('done stemming')


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
    
	for i in txt:
		if i in data_list:
			val+=1
			print(row['number'], row['issue'])
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
	for i in txt:
		if i in data_list:
			val+=1
			#print(row['number'], row['issue'])
			break
      
      
#for i in range(11335):
	#print(i,end='\t')
	#check_security_lemmatized(df.iloc[i]) #to check the lemmatized or stemming list

#check_security(df.iloc[19])
#print(val)
