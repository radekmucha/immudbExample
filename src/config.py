from credentials import CREDENTIALS

class CONFIG:
    mainUrl = 'https://vault.immudb.io/ics/api/v1/ledger'
    urlLedger =  mainUrl + '/default'
    isReadOnlyMode = False
    debug = True     

    def getHeaders(self):
        return {'content-type': 'application/json',  'accept': 'application/json', 'X-API-Key': self.getApiKey()}

    def getApiKey(self):
        if (self.isReadOnlyMode):
            return CREDENTIALS.readOnlyApiKey
        else:
            return CREDENTIALS.apiKey
