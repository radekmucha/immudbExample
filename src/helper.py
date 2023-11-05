import random
import json
import string

def getRandomString(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def gradeAssertion(result, grade, book):
     assert result.status_code == 200, f"Cannot add grade \n{json.dumps(grade,indent=2)}\n to the Grade Book '{book.name}', status code '200' expected, got: '{result.status_code}'\nDetails:\n{json.dumps(result.json(),indent=2)}"

def gradeUpdateAssertion(result, grade, gradeId):
     assert result.status_code == 200, f"Cannot update grade ({json.dumps(grade,indent=2)}), id '{gradeId}', status code '200' expected, got: '{result.status_code}'\nDetails:\n{json.dumps(result.json(),indent=2)}"