from github import Github
import os
import csv
import sys
from pprint import pprint

repo_names = ['trufflesuite/truffle', 'ethereum/mist', 'MetaMask/metamask-extension', 'ConsenSys/smart-contract-best-practices', 'ConsenSys/quorum', 
'embarklabs/embark', 'ethereum/ethereumj', 'deckarep/golang-set', 'ConsenSys/Tokens', 'trustwallet/trust-wallet-ios', 'sigp/lighthouse', 
'Zokrates/ZoKrates', 'MyCryptoHQ/MyCrypto', 'ethereumjs/ethereumjs-monorepo', 'EYBlockchain/nightfall', 'nomiclabs/hardhat', 'MyEtherWallet/MyEtherWallet', 
'cosmos/ethermint-archive', 'status-im/status-go', 'ethhub-io/ethhub', 'AugurProject/augur-core', 'crytic/echidna', 'rainbow-me/rainbow',
 'ConsenSys/ethql', 'ethereumjs/ethereumjs-util', 'Web3Modal/web3modal', 'trufflesuite/drizzle-legacy', 'web3p/web3.php', 'EthWorks/ethereum.rb',
  'matter-labs/zksync', 'rocket-pool/rocketpool', 'ethereumproject/go-ethereum', 'MetaMask/web3-provider-engine', 'walleth/walleth', 'ethereum/trinity', 
  'yuzushioh/EthereumKit', 'WeTrustPlatform/rosca-contracts', 'leapdao/solEVM-enforcer', 'OpenZeppelin/openzeppelin-upgrades']

repo_names+=['ChainSafe/web3.js', 'ethereum/solidity', 'openethereum/parity-ethereum', 'ethereum/EIPs', 'ethereum/wiki',
            'ethereum/ethereum-org-website', 'ethereum/web3.py', 'ethereum/evmone', 'ethereum/remix-project', 'ethereum-mining/ethminer',
            'ethereum/aleth', 'web3j/web3j', 'status-im/status-react', 'trufflesuite/ganache-cli', 'trufflesuite/ganache', 'ethers-io/ethers.js',
            'prysmaticlabs/prysm', 'ethereum/eth2.0-specs', 'trustwallet/trust-wallet-ios', 'TokenMarketNet/smart-contracts',
            'Nethereum/Nethereum', 'ethereum/py-evm', 'sammy007/open-ethereum-pool', 'ethereum/yellowpaper', 'poanetwork/blockscout',
            'graphprotocol/graph-node', 'cubedro/eth-netstats', 'ethereum-ts/TypeChain', 'aragon/client', 'ethereumjs/ethereumjs-wallet',
            'district0x/ethlance']+['ethereum/go-ethereum']


repo_names1=repo_names
l=[]
total=0
token = os.getenv('GITHUB_TOKEN', github_access_token)
g = Github(token)
for repo_name in repo_names1:
    repo = g.get_repo(repo_name)
    issues = repo.get_issues(state='all')
    fields = ['issue', 'number', 'state', 'link','repository_name']
    filename=(repo_name+'.csv').replace('/','_')  # copying all the issues to a csv file
    with open(filename, "w", encoding='utf-8') as file:
        csv_file = csv.writer(file)
        cols = fields
        csv_file.writerow(cols)
        count=0
        for issue in issues:
            row = [issue.title, issue.number, issue.state,
                   'https://github.com/'+repo_name+'/issues/' + str(issue.number),repo_name]
            csv_file.writerow(row)
            count+=1
        l.append(count)
        print(repo_name,count)
        total+=count

print(total)
for i in range(len(l)):
    print(repo_names1[i],l[i])
