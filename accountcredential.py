import random
import string 

class Accountcredential: # class that generates new Accountcredentials
    accountcredential_list=[] # create the accountcredential_list variable that will be used to store our created accountcredential objects. At the beginning it is empty


    def __init__(self, socialnetworkaccount, username, password): #__init__ method that helps us define properties for our objects, takes in arguments for account, username and password
        self.socialnetworkaccount = socialnetworkaccount # ? assigning socialnetworkaccount to what
        self.username = username
        self.password = password

    def save_accountcredential(self): #  create a save_accountcredential method that is called on an accountcredential object ,save_accountcredentials method saves accountcredential objects into accountcredential_list
        Accountcredential.accountcredential_list.append(self) # appends accountcredential object to our accountcredential_list list

    def delete_accountcredential(self): # create a delete_accountcredential method
        Accountcredential.accountcredential_list.remove(self) # using remove method to delete accountcredential object from account_credential list

    def create_password(length): # ? function that creates password for user
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters) for i in range(length))
        print("Password is:", password)

    @classmethod # @classmethod. This is referred to as a decorator. Decorators allow you to make simple modifications to callable objects like functions, methods, or classes. @classmethod simply informs the python interpreter that this is a method that belongs to the entire class. 
    def display_all_accountcredentials(cls): # Just like the self argument refers to the object, cls referred to the entire class, and does not need to be passed in when we call the method.
        return cls.accountcredential_list
        
