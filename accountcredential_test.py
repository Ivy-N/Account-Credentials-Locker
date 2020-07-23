import unittest #importing the Python test framework called unittest module
from accountcredential import Accountcredential # import the Accountcredential class

class TestAccountcredential (unittest.TestCase): # create a subclass called TestAccountcredential that inherits from unittest.TestCase (unittest.TestCase: TestCase class (from unittest?) that helps in creating test cases). A subclass is like a normal class but in addition to its own variables and method it also inherits methods and variables from another class. We pass in the parent class, in this case unittest.testcase? as a parameter in the parenthesis.)

    def setUp(self): # setUp() method allows us to define instructions that will be executed before each test method. 
        self.new_accountcredential = Accountcredential("Instagram","JamesM","jamesm") # create accountcredential object. We have instructed our personal setUp() method to create a new instance of Accountcredential class, before each test method declared, and store it in an instance variable in the test class self.new_accountcredential.

    def tearDown(self): # tearDown method that does clean up after each test case has run (so that eg save_multiple_contact does not run save_contact before running itself). Just like the setUp() method the tearDown() method executes a set of instructions after *every test*. In the tearDown() method we assign the accountcredential_list list in the Accountcredential class as an empty list. This helps us get accurate test results every time a new test case runs.
        Accountcredential.accountcredential_list = []

    def test_init(self): # test_init test case (case=function?) to test if the object is initialized properly. Tests are defined with methods that start with test_, (this is just proper convention to define your tests). 
        self.assertEqual(self.new_accountcredential.socialnetworkaccount,"Instagram") # self.assertEqual() is a TestCase method that checks for an expected result. The first argument is the expected result and the second argument is the result that is actually gotten. Here, we are checking if the details of our new object is what we actually inputted.
        self.assertEqual(self.new_accountcredential.username,"JamesM")
        self.assertEqual(self.new_accountcredential.password,"jamesm")

    def test_save_accountcredential(self): # create a test called test_save_accountcredential test case to test if the accountcredential object is saved into the accountcredential list. test_save_contact that calls a save_contact method to our newly generated object.
        self.new_accountcredential.save_accountcredential() # calling a save_accountcredential method to our newly generated object.
        self.assertEqual(len(Accountcredential.accountcredential_list),1) # check the length of our accountcredential_list list to confirm an addition has been made to our accountcredential list.

    def test_save_multiple_accountcredential(self): # test_save_multiple_accountcredential to check if we can save multiple accountcredential objects to our accountcredential_list
        self.new_accountcredential.save_accountcredential () #saving first accountcredential? 
        test_accountcredential=Accountcredential("Twitter","TeddyN","teddyn") #create a new accountcredential object called test_accountcredential 
        test_accountcredential.save_accountcredential() # save new accountcredential
        self.assertEqual(len(Accountcredential.accountcredential_list),2) # check if the length of accountcredential list is now 2

    def test_delete_accountcredential(self): # test_delete_accountcredential to test if we can remove an accountcredential from our accountcredential list
        self.new_accountcredential.save_accountcredential () # saving first accountcredential in setUp
        test_accountcredential = Accountcredential("Twitter","TeddyN","teddyn") #create new test_accountcredential object for this function specifically?
        test_accountcredential.save_accountcredential() # save new test_accountcredential
        self.new_accountcredential.delete_accountcredential() #delete an accountcredential object
        self.assertEqual(len(Accountcredential.accountcredential_list),1) # check if length of accountcredential_list after deletion is 1

    def test_display_all_accountcredentials(self): # test_display_all_accountcredentials to check if we display all contacts
        self.assertEqual(Accountcredential.display_all_accountcredentials(),Accountcredential.accountcredential_list) # the display_all_accountcredential method should give the same result as the accountcredential_list

if __name__ == '__main__': #Python runtime has special attributes delimited with double underscores (_). __name__ variable evaluates to "__main__" or the actual module name depending on how the module is being executed. if __name__ == '__main__': we are confirming that anything inside the if block should run only if this is the file that is currently being run. 
    unittest.main() # provides a command line interface that collects all the tests methods and executes them.