import cgi
from google.appengine.api import users
import webapp2
from models import student_key, ScheduleItem, Schedule, Student , Grade, GradesList
import json
import logging
from google.appengine.ext import ndb

MAIN_PAGE_FOOTER_TEMPLATE = """\
    <form action="/sign?%s" method="post">
      <div><textarea name="content" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Sign Guestbook"></div>
    </form>
    <hr>
    <form>Guestbook name:
      <input value="%s" name="guestbook_name">
      <input type="submit" value="switch">
    </form>
    <a href="%s">%s</a>
  </body>
</html>
"""

#test
class Testdata(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_FOOTER_TEMPLATE)


class MainPage(webapp2.RequestHandler):
    def get(self,student_nr=883374):
        student_query = Student.query(
            ancestor=student_key(key=student_nr)).order(Student.student_nr)
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

                # # Get schedule item
                # for gradee in grades:
                #     grad = gradee.get()
                #
                #     data.append(vak_code)
                #     obj = {'vak_code': vak_code,'grade': grad.grades[0]}

        self.response.write(obj)
        # self.response.write(MAIN_PAGE_FOOTER_TEMPLATE)
        # obj = {
        #                 'grade': cijfer.grades[0],
        #                 'vak': ,
        #               }
        #
        # self.response.headers['Content-Type'] = 'application/json'
        # self.response.out.write(json.dumps(obj))


class Guestbook(webapp2.RequestHandler):
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
            parent=student_key(key=883374),
            student_nr=883374,
            password='Hello',
            first_name='Geddy',
            last_name='Schellevis',
            country='Nederland',
            birthday='05-05-0-1990',
            email='geddy@geddy.nl',
            telephone_nr='0653380120',
            groups=['inf1F', 'inf2c'],
            zip_address='3142-LP',
            street='sparrendal',
            schedule=schedule_key,
            grade_list=grades_list_key
        )
        student.put()
        schedule = student.schedule[0].get()
        schedule_items = schedule.schedule_item
        pin = ''
        for schedule_item in schedule_items:
            schedule_item = schedule_item.get()
            pin += "<p>" + schedule_item.time_from+" - " + schedule_item.time_until + "<br>" + schedule_item.vak_code\
                      + "<br>" + schedule_item.docent_code + "<br>" + schedule_item.chamber + "</p><br><br><br>"

        self.response.write(pin)
        # logging.INFO(student.schedule[0].get())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
    ('/testdata', Testdata)

], debug=True)