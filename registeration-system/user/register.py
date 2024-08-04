import sys
sys.path.append('validation')  # Adjust the path according to your directory structure

from validation_of_email import EmailValidation
from validation_of_password import PasswordValidation

# from validation import EmailValidation
# from validation import PasswordValidation
class Register:
    Users=list()
    id=0
    def __init__(self,name='',email='',password='',token=''):
        self.name=name
        self.email=email
        self.password=password
        Register.check_errors(self)
        # Register.check_if_user_found(self)
        Register.check_and_insert_if_valid_data(self,self.name,self.email,self.password)
    def check_if_user_found(self):
        ok=0
        for i in range(len(Register.Users)):
            if(Register.Users[i]['user_email']== self.email and Register.Users[i]['user_password']== self.password ):
                print(f'Try to Enter other data in User number {Register.Users[i]['user_id']}!')
                # print(f'Change password or email in user number{Register.Users[i]['user_id']}!!')
                return False
                ok=1
                break
        return not ok
    def check_errors(self):
        validatePassword=PasswordValidation()
        validateEmail=EmailValidation()
        if self.name=='':
            print('Name Field is required .')
        if validateEmail.is_valid_email(self.email)==False:
            print("This email is not valid !!")
        if validatePassword.is_valid_password(self.password)==False:
            print("This password is not valid !!")
        # if(Register.check_if_user_found(self)==0):
        #     Register.check_if_user_found(self)
    
    def check_and_insert_if_valid_data(self,name,email,password):
        validatePassword=PasswordValidation()
        validateEmail=EmailValidation()
        if(self.name!='' 
            and validateEmail.is_valid_email(self.email)
            and validatePassword.is_valid_password(self.password) 
            and Register.check_if_user_found(self)==True):
            Register.Users.append({
                'user_id':Register.id,
                'user_name':self.name,
                'user_email':self.email,
                'user_password':self.password,
                'user_token':''
            })
            Register.id+=1
    def show_all_users():
        for i in range(len(Register.Users)):
            
            if(i!=0):
                print('#'*50)
            print(f'Id : {Register.Users[i]['user_id']}')
            print(f'User Name : {Register.Users[i]['user_name']}')
            print(f'User Email : {Register.Users[i]['user_email']}')
            print(f'User Password : {Register.Users[i]['user_password']}')
            print(f'User Token : {Register.Users[i]['user_token']}')


# user1=Register('Ali','ali@gmail.com','Alinasser@1')
user2=Register('Abdo','Abdo@gmail.com','Abdurrahman@1')
# user2=Register('Abdo','Abdo@gmail.com','Abdurrahman@1')
# user2=Register('Abdo','Abdo@gmail.com','Abdurrahman@1')
# user1.show_all_users()
Register.show_all_users()
            

