          ------------Tool Idea-----------------
 Although blockchain is one of the most important technologies in this fast-running software industry known for its sophisticated security, there are very few questions answered related to security issues. Addressing this issue, the tool is being developed for the users to find all the topmost related issues to their Ethereum security query using the data from the top seventy GitHub repositories related to Ethereum.
              



          -------------------Files-----------
  Release 1:
              The release one files are included in the Release1 folder which comprises the code used for extracting all the Github issues from the top seventy Ethereum Github repositories and further the security issues from those into security_issues.csv (Module 1 - Module 6).

 Release 2:
                The release two files are included in the Release2 folder which comprises the code extracting similar issues from the data we have collected in release one.
                
 The final_tool has the interface we have built.

             ----------------How to run the tool--------------
   In order to run the tool, one can download the final_tool folder and run it successfully by adding the required dependencies. On successfully running the file, a web interface is launched on the local machine of the individual running it.

            -------- Modules explained in detail -------------

As advised by the course instructor, we have divided the whole project into twelve modules.

Module 1:
                   In module one, we have extracted the required Github issues. We modified our code in such a way that users can just add the GitHub repository name to the list and all the issues in the respective GitHub repository will be extracted and stored in the CSV file. The CSV file includes the title of the issue, issue number, and link to the GitHub issue.	
		We used the GitHub module in python to extract the issues. We provided the access token of our GitHub account, which can access all public GitHub repository information. Once these issues are extracted, we implemented the basic python code to write all these issues including their title, issue number, and link to the concerned issue into a CSV file.

Module 2:
                   In module two, we applied different strategies to clean the text. We removed the punctuation in an issue and replaced them with space. We vectorized the issues into words. We also removed the stop words from the issues. We applied both stemming and lemmatization on the words obtained from each issue. We added the resultant words into the CSV file. We applied both stemming and lemmatization to decide the strategy that gives us accurate results.	
  	We cleaned our data(issues extracted from Github repositories) using  Natural Language ToolKit. We used word_tokenize to split each issue into a vector of words. We used the list of stop words in NLTK and removed those from our issues. PorterStemmer is used for stemming and WordNet Lemmatizer to lemmatize the words in the issue.
    
Module 3:
 	In module three in order to extract the security-related issues from the set of all issues extracted from Github, we used the strategy of extraction based on the keywords related to security issues. This is an extension to module two, where we applied different strategies to clean the text. We made sure that this module is confined only to a selection of keywords because this determines the issues that are going to be a part of the final data we are considering for implementing the tool. We went through various papers written on security-related issues and finalized the keywords.  
                   
Module 4:
        In module four we extracted the issues based on the security keywords using both the lemmatized words and stemming words list. We used both techniques to find out the technique that gives out accurate results and with fewer false positives. We also tested a few repositories and manually verified the repositories with fewer security issues.

Module 5:
		In module five, we improvised the code for extracting a good number of security issues. This module was necessary because we need the data set to be large enough so that we can search for the issues related to the user's query and come up with good results. We added a few more keywords, lemmatized and stemmed versions of all keywords along with the bigrams and trigrams.  We also selected seventy repositories containing Ethereum issues for the implementation of the project and extracted all the issues into separate CSV files.

Module 6:
          In module six, we extracted all the security issues from all the seventy repositories we have chosen and made a CSV file out of them which will form the data set for the implementation of the recommendation tool in release two. We also manually verified the extracted issues and how relevant they are to the aspect of security. We also recorded the number of issues in each repository and the number of security issues extracted from them.
          
The files till module 6 are included in Release1. 

Module 7 and module 8:
After completing the extraction of the security issues from the top seventy Ethereum GitHub repositories, the next implementation is the recommendation tool for the query given by the user using the dataset we have obtained. We used cosine similarity as the metric to determine the similarity between the user query and the security issues we have extracted from the Github repositories. Using the cosine similarity score we pulled out the security issues starting from issues with high similarity scores. We have observed that the results are not completely compatible with what we expected. We plan on applying other algorithms and coming up with accurate results.

Module 9 and Module 10:
	As a part of module 9 we implemented the word2vec module on the issues we have made as a part of our database and calculated the similarity of issues with the given input query and sorted the results to extract the issues with a high percentage of similarity. The word2vec model typically is of three hundred dimensions. Due to this dimension words are more generalized and given high similarity if they have some relevance in their meaning. We also did this using a glove module which is of only twenty-five dimensions and verified the results with both of them and observed a high percentage of accuracy in the word2vec module.

The files that are part of the first ten modules combinedly included in Release2.

Module 11 and Module 12:
	As we have completed the major part of our project by implementing the recommendation tool for the security queries related to Ethereum, we developed a simple user-friendly interface where the user enters his/her query and the top fifteen results that we match from the data we have extracted and modified are displayed. The user can dive into it and view the top recommendations and click on them to further get directed to the webpage of the selected issue. We have also displayed the status of the issues whether a particular issue is closed or open.

The interface we have developed is deployed as the final_tool.





