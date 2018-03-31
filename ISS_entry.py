from time import gmtime, strftime
from factom import Factomd, FactomWalletd
import time
import requests

factomd = Factomd()
walletd = FactomWalletd()

timeBetweenEntries=10

entryCredit = 'EC3dUKqQvmgt7zbTqNyDFHZLZEcKHBU54Cqun5pDZMVm9BcDrvzj'
chainID     = '762ae6f88d6960ef7ca22c593f7b708f84bb85c758b4080a8c3f432068c3c299'
Extid1	    = 'VBIF'
Extid2      = 'ISS over Factom HQ'
Extid3      = 'ISS Open-notify.org'
Extid4      = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# Establish parameters for Austin, TX
parameters = {"lat": 30.26, "lon": -97.73}

# Make a get request with the parameters.
response2 = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

#Make request to get information on when ISS will be in vicinity of your input
data2 = response2.content
# Print the content of the response (the data the server returned)
#print(response.content)

while True:
    requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
    data3 = response2.content
    print Extid1
    print Extid2
    print Extid3
    print Extid4
    print data3
    Content = data3
    result = walletd.new_entry(factomd, chainID, [Extid1, Extid2, Extid3, Extid4], Content, entryCredit)
    time.sleep(timeBetweenEntries)
