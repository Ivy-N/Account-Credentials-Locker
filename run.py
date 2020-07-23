from accountcredential import Accountcredential

def create_accountcredential (socialnetworkaccount, username, password): # create a function called create_accountcredential(), that takes in three arguments.
    new_accountcredential = Accountcredential(socialnetworkaccount, username, password) #  create a new accountcredential object and return it
    return new_accountcredential # return the new accountcredential object

def save_accountcredential (accountcredential): # create the function save_accountcredential that takes in the accountcredential object
    accountcredential.save_accountcredential # calling save_contact method to save the contact.

def delete_accountcredential (accountcredential):
    accountcredential.delete_accountcredential

def display_all_accountcredentials (accountcredential):
    accountcredential.display_all_accountcredentials
    return Accountcredential.display_all_accountcredentials

def main():
    print ("Hello. Welcome to your accountcredential list. What would you like to do?")
    print('\n') # \n means new line

    while True: # ? why? while name == main?
        print ("Use these short codes: ca - create accountcredential, da- displayaccountcredential, cp- create password, del- delete a contact, ex-exit the accountcredential list")
        short_code=input().lower() # The input() method reads a line from input, converts into a string and returns it, in this case, we assign short_code to that input ?
        if short_code=='ca': # if user inputs ca
            print ("New Accountcredential")
            print ("-"*10) # print --------------

            print ("Which social network account?")
            socialnetworkaccount=input() # assign input (user's response) to socialnetworkaccount

            print ("Enter your username")
            username=input()

            print ("Enter your password")
            password=input()

            save_accountcredential (create_accountcredential(socialnetworkaccount, username, password)) # all this that the user has input through the create_accountcredential process, we save (create and save new accountcredential) ?
            print('\n')
            print(f"New accountcredential {socialnetworkaccount} for {username} created") # While other string literals always have a constant value, formatted strings are really expressions evaluated at run time
            print('\n')

        elif short_code=='cp': # if user inputs ca
            print ("New Accountcredential")
            print ("-"*10) # print --------------

            print ("Which social network account?")
            socialnetworkaccount=input() # assign input (user's response) to socialnetworkaccount

            print ("Enter your username")
            username=input()

            print ("Here is your password")
            create_password(length) #?
            print("Password is:", password)

            save_accountcredential (create_accountcredential(socialnetworkaccount, username, password)) # all this that the user has input through the create_accountcredential process, we save (create and save new accountcredential) ?
            print('\n')
            print(f"New accountcredential {socialnetworkaccount} for {username} created") # While other string literals always have a constant value, formatted strings are really expressions evaluated at run time
            print('\n')

        elif short_code== 'da':
            if display_all_accountcredentials(): # ? check if display_all_accountcredentials has any result?
                print ("Here is a list of all your account credentials")
                print ('\n')

                for accountcredential in display_all_accountcredentials: # ? for every accountcredential in display_all_accountcredentials (which is the accountcredentials_list)
                    print (f"{accountcredential.socialnetworkaccount}-{accountcredential.username}-{accountcredential.password}") # return every socialnetworkaccount, username and password
                    
                print ('\n')
            
            else: # if there is nothing to display?
                print ('\n')
                print ("You don't seem to have any account credentials saved yet")
                print ('\n')

        # elif short_code=='del': # ?
        #     delete_accountcredential (create_accountcredential(socialnetworkaccount, username, password)) # all this that the user has input through the create_accountcredential process, we save (create and save new accountcredential) ?

        elif short_code=='ex':
            print ("Bye ...")
            break

        else:
            print ("I really did not get that.")


                







