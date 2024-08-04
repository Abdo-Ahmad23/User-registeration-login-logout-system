
import string
class PasswordValidation:
    def __init__(self):
        pass
    def is_valid_password(self,password):
        # Check if the password length is greater than 8
        if len(password) <= 8:
            return False

        
        # Count the occurrences of each category
        upper_case = sum(1 for c in password if c.isupper())
        lower_case = sum(1 for c in password if c.islower())
        digits = sum(1 for c in password if c.isdigit())
        punctuation = sum(1 for c in password if c in string.punctuation)

        # Check if the password meets the criteria
        if (upper_case >= 1 and 
            lower_case >= 1 and 
            digits >= 1 and 
            punctuation >= 1):
            return True
        return False
# email1=PasswordValidation()
# print(email1.is_valid_password('aliNasser1.'))
# print(is_valid_password("AliNasser1"))