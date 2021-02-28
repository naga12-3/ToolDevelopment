from github import Github
import os
import csv
import sys
from pprint import pprint

token = os.getenv('GITHUB_TOKEN', '787f85f88e4bc128250495eb201652d3b616af7f')
g = Github(token)
repo = g.get_repo("ethereum/go-ethereum")
issues = repo.get_issues(state='all')
'''for issue in issues[:25]:
    print(issue.title)
    print(issue.number)
    print(issue.state)
    print(issue.url)'''


#for i in range(int(issues.totalCount/1000)):
#    pprint(issues.get_page(i))
'''print(type(issues.get_page(0)))
print(issues.totalCount)
print(len(issues.get_page(8)),11336/30)
print(str(issues.get_page(8)[4]))
print(str(issues.get_page(0)).find('number'))'''

fields = ['issue', 'number', 'state','link']

i=0
with open("first_data_ethereum_go-ethereum_1.csv", "w", encoding='utf-8') as file:
    csv_file = csv.writer(file)
    cols = fields
    csv_file.writerow(cols)
    for issue in issues:
        row=[issue.title,issue.number,issue.state,'https://github.com/ethereum/go-ethereum/issues/'+str(issue.number)]
        csv_file.writerow(row)
        print(i)
        i=i+1
#for issue in issues[:10]:
    #row = [issue.title, issue.number, issue.state, 'https://github.com/ethereum/go-ethereum/issues/' + str(issue.number)]
    #print(row)