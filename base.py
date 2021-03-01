from github import Github
import os
import csv
import sys
from pprint import pprint

# name of the repository
repo_names=['ChainSafe/web3.js', 'ethereum/solidity', 'openethereum/parity-ethereum', 'ethereum/EIPs', 'ethereum/wiki',
            'ethereum/ethereum-org-website', 'ethereum/web3.py', 'ethereum/evmone', 'ethereum/remix-project', 'ethereum-mining/ethminer',
            'ethereum/aleth', 'web3j/web3j', 'status-im/status-react', 'trufflesuite/ganache-cli', 'trufflesuite/ganache', 'ethers-io/ethers.js',
            'prysmaticlabs/prysm', 'ethereum/eth2.0-specs', 'trustwallet/trust-wallet-ios', 'TokenMarketNet/smart-contracts',
            'Nethereum/Nethereum', 'ethereum/py-evm', 'sammy007/open-ethereum-pool', 'ethereum/yellowpaper', 'poanetwork/blockscout',
            'graphprotocol/graph-node', 'cubedro/eth-netstats', 'ethereum-ts/TypeChain', 'aragon/client', 'ethereumjs/ethereumjs-wallet',
            'district0x/ethlance']

token = os.getenv('GITHUB_TOKEN', 'Access Token') 
g = Github(token)
for repo_name in repo_names:
    repo = g.get_repo(repo_name)
    issues = repo.get_issues(state='all')

    fields = ['issue', 'number', 'state', 'link']

    # copying all the issues to a csv file

    filename=(repo_name+'.csv').replace('/','_')
    with open(filename, "w", encoding='utf-8') as file:
        csv_file = csv.writer(file)
        cols = fields
        csv_file.writerow(cols)
        for issue in issues:
            row = [issue.title, issue.number, issue.state,
                   'https://github.com/'+repo_name+'/issues/' + str(issue.number)]
            csv_file.writerow(row)

# for issue in issues[:10]:
# row = [issue.title, issue.number, issue.state, 'https://github.com/ethereum/go-ethereum/issues/' + str(issue.number)]
# print(row)
