from google.appengine.ext import ndb

studentnr= 883374

def student_key(key=studentnr):
    return ndb.Key('Person', key)

class ScheduleItem(ndb.Model):
    time_from = ndb.StringProperty()
    time_until = ndb.StringProperty()
    vak_code = ndb.StringProperty()
    docent_code = ndb.StringProperty()
    chamber = ndb.StringProperty()


class Schedule(ndb.Model):
    day = ndb.StringProperty()
    schedule_item = ndb.KeyProperty(kind='ScheduleItem', repeated=True, indexed=True)


class Grade(ndb.Model):
    study_points = ndb.IntegerProperty()
    passed = ndb.BooleanProperty()
    grades = ndb.FloatProperty()
    docent = ndb.StringProperty()
    concept = ndb.BooleanProperty()
    exam_date = ndb.StringProperty()  # changed later to DateProperty
    mutation_date = ndb.StringProperty()  # changed later to DateProperty
    weight = ndb.IntegerProperty()


class GradesList(ndb.Model):
    vak_code = ndb.StringProperty()
    grades = ndb.KeyProperty(kind='Grade')


class Student(ndb.Model):
    student_nr = ndb.StringProperty()
    password = ndb.StringProperty()
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    country = ndb.StringProperty()
    birthday = ndb.StringProperty()
    email = ndb.StringProperty()
    telephone_nr = ndb.StringProperty()
    groups = ndb.StringProperty(repeated=True)
    zip_address = ndb.StringProperty()
    street = ndb.StringProperty()
    schedule = ndb.KeyProperty(kind='Schedule', repeated=True)
    grade_list = ndb.KeyProperty(kind='GradesList', repeated=True)
