import webapp2

app = webapp2.WSGIApplication([
    ('/controllers/student', 'controllers.student.CheckStudent')
], debug=True)
