import re
class EmailValidation:
    def __init__(self):
        pass
    def is_valid_email(self,email):
        # Regular expression for validating an Email
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None
email1=EmailValidation()
# print(email1.is_valid_email('aligmail.com'))
