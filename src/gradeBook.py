import requests
import json
from credentials import CREDENTIALS
from config import CONFIG
from datetime import datetime
from pprint import pprint



class GradeBook:
    def __init__(self, name):
        self.conf = CONFIG()
        self.urlCollection = self.conf.urlLedger + '/collection/' + name
        self.documentUrl = self.urlCollection+ "/document"
        self.name = name
        self.fields = [{"name": "studentId", "type":"INTEGER"},
                        {"name": "name", "type":"STRING"},
                        {"name": "surname", "type":"STRING"},
                        {"name": "subject", "type":"STRING"},
                        {"name": "value", "type":"INTEGER"}
                      ]

    def prepareTest(self):
        if (not self.checkBookExists()):
            self.createGradeBook()

    def createGradeBook(self):
        content = {"idFieldName": "id_grade","fields": self.fields, "indexes":[{"fields":["studentId"],"isUnique": False}]}
        return requests.put(self.urlCollection, data=json.dumps(content), headers=self.conf.getHeaders())
    
    def addGrade(self, grade):
        return requests.put(self.documentUrl, data=json.dumps(grade), headers=self.conf.getHeaders())
        
    def updateGrade(self, newGrade, gradeId):
        content = {'document': newGrade, "query": {"expressions": [{"fieldComparisons": [{"field": "id_grade","operator": "EQ","value": gradeId}]}]}}
        return requests.post(self.documentUrl, data=json.dumps(content), headers=self.conf.getHeaders())
    
    def createIndex(self, fields):
        content = {"fields": fields, "isUnique":True}
        return requests.post(self.conf.urlCollection + "/indexes",  data=json.dumps(content), headers=self.conf.getHeaders())

    def checkVaultStatus(self):
        url = self.conf.urlLedger + "/state"
        response = requests.get(url, headers=self.conf.getHeaders())
        return response.status_code
    
    def checkBookExists(self):
        url = self.urlCollection
        response = requests.get(url, headers=self.conf.getHeaders())
        return response.status_code == 200

    def listGradeBooks(self):
        url = self.conf.urlLedger + "/collections"
        response = requests.get(url, headers=self.conf.getHeaders())
        return response

    def checkStudentGrades(self, studentId):
        url = self.urlCollection + "/documents/search"
        query = {"page": 1, "perPage": 100, "query": {"expressions": [{"fieldComparisons": [{"field": "studentId", "operator": "EQ","value": studentId }]}], "limit": 0}}
        return requests.post(url,  data=json.dumps(query), headers=self.conf.getHeaders())
    
    def deleteBook(self):
        url = self.urlCollection
        response = requests.delete(url, headers=self.conf.getHeaders())
        return response.status_code
        
