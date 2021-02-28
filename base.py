from github import Github
import os
import csv
import sys
from pprint import pprint
# name of the repository
repo_name="ethereum/go-ethereum"

token = os.getenv('GITHUB_TOKEN', '787f85f88e4bc128250495eb201652d3b616af7f')
g = Github(token)
repo = g.get_repo(repo_name)
issues = repo.get_issues(state='all')

fields = ['issue', 'number', 'state','link']
# copying all the issues to a csv file
with open("first_data_ethereum_go-ethereum_1.csv", "w", encoding='utf-8') as file:
    csv_file = csv.writer(file)
    cols = fields
    csv_file.writerow(cols)
    for issue in issues:
        row=[issue.title,issue.number,issue.state,'https://github.com/ethereum/go-ethereum/issues/'+str(issue.number)]
        csv_file.writerow(row)
      
#for issue in issues[:10]:
    #row = [issue.title, issue.number, issue.state, 'https://github.com/ethereum/go-ethereum/issues/' + str(issue.number)]
    #print(row)
