import sys
sys.path.append('validation')  # Adjust the path according to your directory structure

from validation_of_email import EmailValidation
from validation_of_password import PasswordValidation

from register import Register
import random
import string
class Login:
    def __init__(self,email='',password=''):
        self.email=email
        self.password=password
        Login.check_errors(self)
    
    def check_errors(self):
        validatePassword=PasswordValidation()
        validateEmail=EmailValidation()
        if validateEmail.is_valid_email(self.email)==False:
            print("This email is not valid !!")
        if validatePassword.is_valid_password(self.password)==False:
            print("This password is not valid !!")
    def generate_random_text(length):
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        # Define character sets
        letters = string.ascii_letters  # A-Z, a-z
        digits = string.digits          # 0-9
        punctuation = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        
        # Combine all character sets
        all_characters = letters + digits + punctuation
        
        # Generate random string
        random_text = ''.join(random.choice(all_characters) for _ in range(length))
        
        return random_text
    def check_user(self):
        ok=0
        for i in range(len(Register.Users)):
            if(Register.Users[i]['user_email']==self.email and Register.Users[i]['user_password']==self.password):
                Register.Users[i]['user_token']=Login.generate_random_text(20)
                ok=1
                break
        if(ok==0):
            return 'This is an error in this entered data !'
        
        
user1=Login('Abdo@gmail.com','Abdurrahman@1')
user1.check_user()
register=Register.show_all_users()
        
        