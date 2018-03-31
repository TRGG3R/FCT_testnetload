from time import gmtime, strftime
from factom import Factomd, FactomWalletd
import time
import requests

factomd = Factomd()
walletd = FactomWalletd()

timeBetweenEntries=1

entryCredit = 'EC3dUKqQvmgt7zbTqNyDFHZLZEcKHBU54Cqun5pDZMVm9BcDrvzj'
chainID     = 'c04ebdf83894a48aa19a08d31c02083e02e2372cff86c7b00ea30b8d4b04ec97'
Extid1	    = 'VBIF'
Extid2      = 'ISS location'
Extid3      = 'ISS Open-notify.org'

while True:
    Extid4 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.content
    print Extid1
    print Extid2
    print Extid3
    print Extid4
    print data
    Content = data
    result = walletd.new_entry(factomd, chainID, [Extid1, Extid2, Extid3, Extid4], Content, entryCredit)
    time.sleep(timeBetweenEntries)
