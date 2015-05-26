import webapp2

app = webapp2.WSGIApplication([
    ('/controllers/student', 'controllers.student.test'),
], debug=True)
