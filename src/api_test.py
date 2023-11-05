import random
import helper

import gradeBook


bookName = "api_tests"
book = gradeBook.GradeBook(bookName)
bookNameTmpTest = "gradeBook_" + helper.getRandomString(5)
bookTmpTest = gradeBook.GradeBook(bookNameTmpTest)

def test_createGradeBook():
    result = bookTmpTest.createGradeBook()
    assert result.status_code == 200, f"Cannot create Grade Book '{bookTmpTest.name}', status code '200' expected, got: '{result.status_code}'\nDetails:\n{result.json()}"

def test_deleteBook():
    result = bookTmpTest.deleteBook()
    assert result == 200, f"Cannot delete Grade Book, status code '200' expected, got: '{result}'"

def test_addNewGrade():
    book.prepareTest()
    sufix = helper.getRandomString(4)
    grade = {'studentId':random.randrange(10000),'name':f"Student_{sufix}", "surname":f"Surname_{sufix}","subject":f"Subject_{sufix}", "value":random.randrange(1,6)}
    result = book.addGrade(grade)
    helper.gradeAssertion(result, grade, book)

def test_updateGrade():
    book.prepareTest()
    sufix = helper.getRandomString(4)
    grade = {'studentId':random.randrange(10000),'name':f"Student_{sufix}", "surname":f"Surname_{sufix}","subject":f"Subject_{sufix}", "value":random.randrange(1,6)}
    result = book.addGrade(grade)
    gradeId = result.json()['documentId']
    grade['value'] = 6
    result = book.updateGrade(grade, gradeId)
    helper.gradeUpdateAssertion(result, grade, gradeId)



   