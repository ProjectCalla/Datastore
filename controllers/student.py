from google.appengine.api import taskqueue
import webapp2
import logging
from models.models import student_key, Student, ScheduleItem, Schedule, GradesList, Grade

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
            # call the crawler api for injecting the user to the crawler
            logging.info(username)
            logging.info(password)


class SaveNewUser(webapp2.RequestHandler):
    def post(self):

        schedule_items = []
        schedule_items.append(ScheduleItem(time_from='08.30',
                                           time_until='10.50',
                                           vak_code='Dev05',
                                           docent_code='paris',
                                           chamber='wd.03.002'))

        schedule_items.append(ScheduleItem(time_from='11.30',
                                           time_until='13.50',
                                           vak_code='Skils',
                                           docent_code='Yolo',
                                           chamber='H.04.318'))

        schedule_item_keys = []
        for i in schedule_items:
            schedule_item_keys.append(i.put())

        schedule = Schedule(day='Monday',
                            schedule_item=schedule_item_keys)

        schedule_key = [schedule.put()]

        grade = Grade(study_points=3,
                      passed=True,
                      grades=7.0,
                      docent='busker',
                      concept=False,
                      exam_date='1-5-2015',
                      mutation_date='5-5-2015',
                      weight=1)

        grade_key = grade.put()

        grades_list = GradesList(vak_code='dev04',
                                 grades=grade_key)

        grades_list_key = [grades_list.put()]

        student = Student(
            parent=student_key(key="0883374"),
            student_nr="0883374",
            password='Hello',
            first_name='Geddy',
            last_name='Schellevis',
            country='Nederland',
            birthday='05-03-1990',
            email='geddy@geddy.nl',
            telephone_nr='0653380120',
            groups=['inf1F', 'inf2c'],
            zip_address='4444-LP',
            street='ergens',
            schedule=schedule_key,
            grade_list=grades_list_key
        )
        student.put()