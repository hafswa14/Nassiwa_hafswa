class UserForm:
    def validate(self):
        print("User basic validation")

class EmailForm(UserForm):
    def validate(self):
        print("Validating email format")
        super().validate()

class RegistrationForm(EmailForm):
    def validate(self):
        print("Validating user password ")
        super().validate()
userReg = RegistrationForm()
userReg.validate()        
