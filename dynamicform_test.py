# import unittest
# > import the functions you want to text into the test.py file
import unittest
from form import fireput
from app import dynamic_form

#create a test class and pass "unittest.TestCase"
class TestDynamicForm(unittest.TestCase):
    #def a function
    #write a test method in the class and
    #make sure that the name starts with "test"
    def test_dynamicform(self):
        #call the asssertAlmostEqual
        self.asssertAlmostEqual(dynamic_form(), True)
        # here pass the values where the first value is the output and the
        #second value is the correct answer
        # to run the test
        # in shell type
        #    > python -m unittest (*name of the test module*)

    def test_value(self):
        #make sure value errors are raised when necessary
        self.assertRaises(ValueError, dynamic_form )
         #assertRaises is used to raise errors when input is wrong

    def test_type(self):
        self.assertRaises(TypeError, dynamic_form, int )
