from time import gmtime, strftime
from factom import Factomd, FactomWalletd
import time
import requests

factomd = Factomd()
walletd = FactomWalletd()

timeBetweenEntries=1

entryCredit = 'EC3dUKqQvmgt7zbTqNyDFHZLZEcKHBU54Cqun5pDZMVm9BcDrvzj'
chainID     = 'c8e3d78d4331e57bf84c6cbeb6a8d5fe7072b3c97e86c566a54e833c24608297'
Extid1	    = 'VBIF'
Extid2      = 'ISS location4'
Extid3      = 'ISS Open-notify.org'

while True:
    Extid4 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    response= requests.get("http://api.open-notify.org/iss-now.json")
    data = response.content
    print Extid1
    print Extid2
    print Extid3
    print Extid4
    print data
    Content = data
    result = walletd.new_entry(factomd, chainID, [Extid1, Extid2, Extid3, Extid4], Content, entryCredit)
    time.sleep(timeBetweenEntries)