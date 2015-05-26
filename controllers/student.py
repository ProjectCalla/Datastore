
from google.appengine.api import taskqueue
import webapp2
import logging

class test(webapp2.RequestHandler):
    def post(self):
        a = "testen"
        logging.info(a)


class CheckStudent(object):
    def __init__(self, nr, ww):
        self.nr = nr
        self.ww = ww
        logging.info(nr)