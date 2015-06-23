import webapp2
from google.appengine.api import taskqueue
import logging

html = """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8"/>
        <title>Login Form</title>
    </head>
    <body>
            <h1>Student login details</h1>
            <form method="post">
                <label for="username">studentnummer:</label>
                <input name="username" type="text" value"">
                <br>
                <br>
                <label for="password">wachtwoord:</label>
                <input name="password" type="text" value="">
                <br>
                <br>
                <label for="regId">regId:</label>
                <input name="regId" type="text" value="">
                <br>
                <br>

                <input name="" type="submit" value="inloggen">
            </form>
    </body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(html)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        regId = self.request.get("regId")

        logging.info(username)
        logging.info(password)
        # This is for check if student exists

        taskqueue.add(url='/controllers/student', params={'username':username,'password':password,"regId":regId})