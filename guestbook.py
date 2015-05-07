import cgi
from google.appengine.api import users
import webapp2
from models import student_key, ScheduleItem, Schedule, Student
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


class Testdata(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_FOOTER_TEMPLATE)


class MainPage(webapp2.RequestHandler):
    def get(self):
        student_query = Student.query(
            ancestor=student_key(key=883374)).order(Student.student_nr)
        students = student_query.fetch(1)

        data = []
        # Get student
        for student in students:
            # Get schedule
            for schedule in student.schedule:
                schedule = schedule.get()
                item = schedule.schedule_item
                # Get schedule item
                for lesson in item:
                    les = lesson.get()
                    data.append(les.vak_code)

        self.response.write(data)
        # self.response.write(MAIN_PAGE_FOOTER_TEMPLATE)


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

        schedule=Schedule(day='Monday',
                          schedule_item=schedule_item_keys)

        schedule_key = schedule.put()

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
            zip_address='3142LP',
            street='sparrendal',
            schedule=[schedule_key]
        )
        student.put()
        schedule=student.schedule[0].get()
        schedule_item = schedule.schedule_item[0].get()
        self.response.write(schedule_item.time_from+" - "+schedule_item.time_until+"<br>" +
                            schedule_item.vak_code+"<br>" +schedule_item.docent_code +"<br>" +
                            schedule_item.chamber)
        # logging.INFO(student.schedule[0].get())



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
    ('/testdata', Testdata)

], debug=True)