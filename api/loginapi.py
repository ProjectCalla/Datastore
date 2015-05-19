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
            <form method="post">
                <label for="studentnummer">studentnummer:</label>
                <input name="studentnummer" type="text" value""><br>

                <label for="wachtwoord">Wachtwoord:</label>
                <input name="wachtwoord" type="text" value=""><br>

                <input name="" type="submit" value="">
            </form>
    </body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(html)

    def post(self):
        studentnummer = self.request.get("studentnummer")
        wachtwoord = self.request.get("wachtwoord")

        # This is for check if student exists
        from controllers.student import CheckStudent
        CheckStudent(studentnummer, wachtwoord)

        self.response.out.write('done')
