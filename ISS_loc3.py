from time import gmtime, strftime
from factom import Factomd, FactomWalletd
import time
import requests

factomd = Factomd()
walletd = FactomWalletd()

timeBetweenEntries=1

entryCredit = 'EC3dUKqQvmgt7zbTqNyDFHZLZEcKHBU54Cqun5pDZMVm9BcDrvzj'
chainID     = '2f512df03bd4b942891be78da6c67c7cafc2bfc3b0dd22cc4d383fbeda04c15b'
Extid1	    = 'VBIF'
Extid2      = 'ISS location3'
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