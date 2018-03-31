from time import gmtime, strftime
from factom import Factomd, FactomWalletd
import time
import datetime
import requests
factomd = Factomd()
walletd = FactomWalletd()

timeBetweenEntries = 1

entryCredit = 'EC3dUKqQvmgt7zbTqNyDFHZLZEcKHBU54Cqun5pDZMVm9BcDrvzj'
chainID     = '563275fa2cbc54bdad9c0c70fe412ae4af64725d039f199b82dac9fa191b64cd'
Extid1	    = 'VBIF'
Extid2      = 'CoinMarketCap Ticker'
Extid3      = 'Crypto Ticker Updated Every 5 Seconds'
Extid5      = 'Continue_1'
Extid6      = 'Continue_2'
Extid7      = 'Continue_3'
Extid8      = 'Continue_4'
Extid9      = 'Continue_5'

while True:
    URL_Complete = ('https://api.coinmarketcap.com/v1/ticker/')
    response = requests.get(URL_Complete)
    Content = response.content[:10000]
    Content2 = response.content[10000:20000]
    Content3 = response.content[20000:30000]
    Content4 = response.content[30000:40000]
    Content5 = response.content[40000:50000]
    Content6 = response.content[50000:]
    Extid4 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print Extid1
    print Extid2
    print Extid3
    print Extid4
    print Content
    result = walletd.new_entry(factomd, chainID, [Extid1, Extid2, Extid3, Extid4], Content, entryCredit)
    print Extid5
    result = walletd.new_entry(factomd, chainID, [Extid1, Extid2, Extid3, Extid4, Extid5], Content2, entryCredit)
    print Content2
    print Extid6
    result = walletd.new_entry(factomd, chainID, [Extid1, Extid2, Extid3, Extid4, Extid6], Content3, entryCredit)
    print Content3
    print Extid7
    result = walletd.new_entry(factomd, chainID, [Extid1, Extid2, Extid3, Extid4, Extid7], Content4, entryCredit)
    print Content4
    print Extid8
    result = walletd.new_entry(factomd, chainID, [Extid1, Extid2, Extid3, Extid4, Extid8], Content5, entryCredit)
    print Content5
    print Extid9
    result = walletd.new_entry(factomd, chainID, [Extid1, Extid2, Extid3, Extid4, Extid9], Content6, entryCredit)
    print Content6
    time.sleep(timeBetweenEntries)
