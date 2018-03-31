from time import gmtime, strftime
from factom import Factomd, FactomWalletd
import time
import requests

factomd = Factomd()
walletd = FactomWalletd()

timeBetweenEntries=1

entryCredit = 'EC3dUKqQvmgt7zbTqNyDFHZLZEcKHBU54Cqun5pDZMVm9BcDrvzj'
chainID     = '2d6e02445c299be3428662bf7662d3823d71ee708b7183ee87959906ca85f033'
Extid1	    = 'VBIF'
Extid2      = 'People in Space'
Extid3      = 'Open-notify.org'

while True:
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.content
    Extid4 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print Extid1
    print Extid2
    print Extid3
    print Extid4
    print data
    Content = data
    result = walletd.new_entry(factomd, chainID, [Extid1, Extid2, Extid3, Extid4], Content, entryCredit)
    time.sleep(timeBetweenEntries)