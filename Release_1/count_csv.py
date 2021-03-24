import pandas as pd
import nltk
import re
import csv
import os
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


#creating a reference to the csv file
# filename="Nethereum_Nethereum.csv"
filenames=['trufflesuite_truffle.csv', 'ethereum_mist.csv', 'MetaMask_metamask-extension.csv', 'ConsenSys_smart-contract-best-practices.csv',
 'ConsenSys_quorum.csv', 'embarklabs_embark.csv', 'ethereum_ethereumj.csv', 'deckarep_golang-set.csv', 'ConsenSys_Tokens.csv',
 'trustwallet_trust-wallet-ios.csv', 'sigp_lighthouse.csv', 'Zokrates_ZoKrates.csv', 'MyCryptoHQ_MyCrypto.csv', 'ethereumjs_ethereumjs-monorepo.csv',
 'EYBlockchain_nightfall.csv', 'nomiclabs_hardhat.csv', 'MyEtherWallet_MyEtherWallet.csv', 'cosmos_ethermint-archive.csv', 'status-im_status-go.csv',
  'ethhub-io_ethhub.csv', 'AugurProject_augur-core.csv', 'crytic_echidna.csv', 'rainbow-me_rainbow.csv', 'ConsenSys_ethql.csv', 'ethereumjs_ethereumjs-util.csv', 'Web3Modal_web3modal.csv', 'trufflesuite_drizzle-legacy.csv', 'web3p_web3.php.csv', 'EthWorks_ethereum.rb.csv', 'matter-labs_zksync.csv'  
, 'rocket-pool_rocketpool.csv', 'ethereumproject_go-ethereum.csv', 'MetaMask_web3-provider-engine.csv', 'walleth_walleth.csv',
 'ethereum_trinity.csv', 'yuzushioh_EthereumKit.csv', 'WeTrustPlatform_rosca-contracts.csv', 'leapdao_solEVM-enforcer.csv',
 'OpenZeppelin_openzeppelin-upgrades.csv', 'ChainSafe_web3.js.csv', 'ethereum_solidity.csv', 'openethereum_parity-ethereum.csv', 'ethereum_EIPs.csv',
  'ethereum_wiki.csv', 'ethereum_ethereum-org-website.csv', 'ethereum_web3.py.csv', 'ethereum_evmone.csv', 'ethereum_remix-project.csv', 
  'ethereum-mining_ethminer.csv', 'ethereum_aleth.csv', 'web3j_web3j.csv', 'status-im_status-react.csv', 'trufflesuite_ganache-cli.csv', 
  'trufflesuite_ganache.csv', 'ethers-io_ethers.js.csv', 'prysmaticlabs_prysm.csv', 'ethereum_eth2.0-specs.csv', 'trustwallet_trust-wallet-ios.csv',
   'TokenMarketNet_smart-contracts.csv', 'Nethereum_Nethereum.csv', 'ethereum_py-evm.csv', 'sammy007_open-ethereum-pool.csv', 'ethereum_yellowpaper.csv', 
   'poanetwork_blockscout.csv', 'graphprotocol_graph-node.csv', 'cubedro_eth-netstats.csv', 'ethereum-ts_TypeChain.csv', 'aragon_client.csv',
   'ethereumjs_ethereumjs-wallet.csv', 'district0x_ethlance.csv', 'ethereum_go-ethereum.csv'] 
total=0
for filename in filenames:
	df=pd.read_csv(filename)
	print(filename,len(df))
	total+=len(df)
print("total issues",total)