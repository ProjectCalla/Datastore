import webapp2

html = """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8"/>
        <title>Login Form</title>
    </head>
    <body>
        <h1>Student login details</h1>
    </body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Hello')

app = webapp2.WSGIApplication