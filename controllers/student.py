
from google.appengine.api import taskqueue
import webapp2
import logging
from models.models import student_key,Student

class CheckStudent(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")

        student_query = Student.query(
            ancestor=student_key(key=username)).order(Student.student_nr)
        students = student_query.fetch(1)

        if students:
            logging.info("student bestaat al")
        else:
            logging.info(username)
            logging.info(password)
