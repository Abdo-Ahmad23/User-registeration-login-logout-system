import sys
sys.path.append('validation')  # Adjust the path according to your directory structure
from validation_of_email import EmailValidation
from validation_of_password import PasswordValidation
from register import Register
class Logout:
    def __init__(self,email='',password=''):
        self.email=email
        self.password=password
        Logout.check_if_empty(self)
        Logout.logout_perform(self)

    def check_if_empty(self):
        if(self.email==''):
            print('Email field is required')
        if(self.password==''):
            print('Password field is required')
    def check_if_this_data_found(self):
        users=Register.Users
        for i in range(len(users)):
            if(users[i]['user_email']==self.email and users[i]['user_password']==self.password and users[i]['user_token']!=''):
                users[i]['user_token']=''
                return True
            
        return False
    def logout_perform(self):
        if(self.check_if_this_data_found()):
            self.check_if_this_data_found()
            print("Loggined Out successfually !")
        else:
            print('Your Data is not Correct !!')
            return 
        

user1=Logout('Abdo@gmail.com','Abdurrahman@1')
# user1.check_if_empty()
register=Register.show_all_users()