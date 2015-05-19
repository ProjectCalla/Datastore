
from google.appengine.api import taskqueue
import webapp2
import logging

class test(webapp2.RequestHandler):
    def post(self):
        a = "testen"
        logging.info(a);


class Check(object):
    def check_student(self,studentnr,password):
        logging.info("We here")