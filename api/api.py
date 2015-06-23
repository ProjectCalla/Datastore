import webapp2
from models.models import Student, Schedule, ScheduleItem,Grade,GradesList,student_key
from google.appengine.api import taskqueue
import logging
import json

class crawler(webapp2.RequestHandler):
    def put(self):
        a=1

class schedule(webapp2.RequestHandler):
    def get(self, username="0883374"):
        obj = {}
        student_query = Student.query(
            ancestor=student_key(key=username)).order(Student.student_nr)
        students = student_query.fetch(1)

        schedules = None
        data = []
        obj = {"start": "10.30", "chamber": "h.05.002", "vak": "ANL05" }



        self.response.write(json.dumps(obj))

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
                obj = {'vak_code': vak_code, 'grade': 7}

        self.response.write(json.dumps(obj))

class newData(webapp2.RequestHandler):
    def get(self,username):
        time = None
        date = None
        student_query = Student.query(
            ancestor=student_key(key=username)).order(Student.student_nr)
        students = student_query.fetch(1)

        for student in students:
            time = student.last_edit_time
            date = student.last_edit_date

        response = {'date':date, 'time': time}
        self.response.write(json.dumps(response))

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

class test(webapp2.RequestHandler):
    def get(self):

        schedule_items = []
        schedule_items.append(ScheduleItem(time_from='10.30',
                                           time_until='12.50',
                                           vak_code='ANL05',
                                           docent_code='paris',
                                           chamber='h.05.002'))

        schedule_items.append(ScheduleItem(time_from='13.30',
                                           time_until='15.50',
                                           vak_code='SLC',
                                           docent_code='muill',
                                           chamber='H.04.318'))

        schedule_item_keys = []
        for i in schedule_items:
            schedule_item_keys.append(i.put())

        schedule = Schedule(day='Wednesday',
                            schedule_item=schedule_item_keys)

        schedule_key = [schedule.put()]

        grade = Grade(study_points=4,
                      passed=True,
                      grades=8.1,
                      docent='Busker',
                      concept=False,
                      exam_date='1-5-2015',
                      mutation_date='5-5-2015',
                      weight=1)

        grade_key = grade.put()

        grades_list = GradesList(vak_code='dev06',
                                 grades=grade_key)

        grades_list_key = [grades_list.put()]

        student = Student(
            parent=student_key(key="0846735"),
            student_nr="0846735",
            password='Hello',
            first_name='Jeroen',
            last_name='Stravers',
            country='Nederland',
            birthday='12-08-1988',
            email='jeroen@gmail.nl',
            telephone_nr='0678945032',
            groups=['inf1F', 'inf2c'],
            zip_address='4435-GK',
            street='Kruisplein',
            schedule=schedule_key,
            grade_list=grades_list_key
        )
        student.put()

        obj = {"test:", "done"}
        self.response.write(obj)