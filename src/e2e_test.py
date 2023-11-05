import random
import json
import helper

import gradeBook

bookName = "e2e_test"
book = gradeBook.GradeBook(bookName)
bookForParents = gradeBook.GradeBook(bookName)
bookForParents.conf.isReadOnlyMode = True

def test_scenario1():
    book.prepareTest()
    student1Id = random.randrange(10000)
    grade = {'studentId':student1Id,'name':f"Student_1", "surname":f"Surname_1","subject":f"Mathematics", "value":1}
    # Add grade for Student1
    result = book.addGrade(grade)
    helper.gradeAssertion(result, grade, book)
    gradeId = result.json()['documentId']
    # Parents check Student1's grades
    result = bookForParents.checkStudentGrades(student1Id)
    # Check if '1' grade is in vault
    assert any(i['document']['value'] == 1 for i in result.json()['revisions']), f"Expected grade 1 but found:" + json.dumps(result.json()['revisions'],indent=2)
    grade['value']=6
    # Parents try to check grade
    result = bookForParents.updateGrade(grade,gradeId)
    # Check that Parents cannot change the grade
    assert result.status_code == 403, f"Parents shouldn't update grade, expected '403' status code, got '{result.status_code}'"
    grade['value']=4
    # The teacher improves the grade
    result = book.updateGrade(grade,gradeId)
    helper.gradeUpdateAssertion(result, grade, gradeId)
    # Parents check whether the improved grade is '4'
    result = bookForParents.checkStudentGrades(student1Id)
    assert any(i['document']['value'] == 4 for i in result.json()['revisions']), f"Expected grade 4 but found:" + json.dumps(result.json()['revisions'],indent=2)