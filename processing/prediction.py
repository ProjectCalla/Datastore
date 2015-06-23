from gcm import *

student = {"student_nr": "0883374",
            "password": 'Hello',
            "first_name": 'Geddy',
            "last_name": 'Schellevis',
            "country": 'Nederland',
            "birthday": '05-03-1990',
            "email": 'geddy@geddy.nl',
            "telephone_nr": '0653380120',
            "groups": ['inf1F', 'inf2c'],
            "zip_address": '4444-LP',
            "street": 'ergens'}

grades = {"vak_code": 'dev04',
          "study_points": 2,
          "grades": [7.0,6.0],
          "docent": 'busker',
          "concept": False,
          "exam_date": '1-1-2001',
          "mutation_date": '2-2-2015',
          "weight": 1}

schedule = {}  # for later

gcm = GCM("AIzaSyC8kSCgpukS0zCcVttup5bCWH-yAKeuDls")
data = {'the_message': 'You have x new friends', 'param2': 'value2'}

reg_id = 'APA91bHDRCRNIGHpOfxivgwQt6ZFK3isuW4aTUOFwMI9qJ6MGDpC3MlOWHtEoe8k6PAKo0H_g2gXhETDO1dDKKxgP5LGulZQxTeNZSwva7tsIL3pvfNksgl0wu1xGbHyQxp2CexeZDKEzvugwyB5hywqvT1-UxxxqpL4EUXTWOm0RXE5CrpMk'

gcm.plaintext_request(registration_id=reg_id, data=data)
