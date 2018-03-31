from time import gmtime, strftime
from factom import Factomd, FactomWalletd
import time
import datetime
import requests
factomd = Factomd()
walletd = FactomWalletd()

timeBetweenEntries = 2.5

entryCredit = 'EC3dUKqQvmgt7zbTqNyDFHZLZEcKHBU54Cqun5pDZMVm9BcDrvzj'
chainID     = 'cfb5d93e747d20433e3b14603f90a5eb152d0399e7278f9671ecf9763f8780e8'
Extid1	    = 'VBIF'
Extid2      = 'NASA NEOs'
Extid3      = 'Listing of Near Earth Objects for today'

while True:
    Extid4 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    Today = (datetime.datetime.now().strftime("%Y-%m-%d"))
    URL1 = 'https://api.nasa.gov/neo/rest/v1/feed?start_date='
    URL2 = '&end_date='
    URL3 = '&api_key='
    API_key = 'MyxQDpC76PDGkqBZVzBEC0FDVsd2ngoztCH1T4kV'
    URL_Complete = (URL1 + Today + URL2 + Today + URL3+ API_key)
    response = requests.get(URL_Complete)
    Content = response.content[:10000]
    Content2 = response.content[10000:]
    print Extid1
    print Extid2
    print Extid3
    print Extid4
    print Content
    print Content2
    result = walletd.new_entry(factomd, chainID, [Extid1, Extid2, Extid3, Extid4], Content, entryCredit)
    result = walletd.new_entry(factomd, chainID, [Extid1, Extid2, Extid3, Extid4], Content2, entryCredit)
    time.sleep(timeBetweenEntries)
