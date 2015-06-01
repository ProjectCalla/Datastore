import webapp2
from models.models import Student, Schedule, ScheduleItem,Grade,GradesList,student_key
from google.appengine.api import taskqueue
import logging

class crawler(webapp2.RequestHandler):
    def put(self):
        a=1

class grade(webapp2.RequestHandler):
    def get(self, username="0883374"):
        student_query = Student.query(
            ancestor=student_key(key=username)).order(Student.student_nr)
        students = student_query.fetch(1)

        data = []
        # Get student
        for student in students:
            # Get schedule
            for grade_list in student.grade_list:
                grade_listt = grade_list.get()
                item = grade_listt.grades
                vak_code = grade_listt.vak_code
                grades = grade_listt.grades.get()
                grade = grades.grades
                data.append(vak_code)
                obj = {'vak_code': vak_code, 'grade': grade}

        self.response.write(obj)