import unittest as ut
import sys
import time

sys.path.append('src/runmetricsvisualizer')
from helpers import time_function

# functions to be used for testing
def other_function(iterations, sleep):
    for x in range(iterations):
        sum([x**5 for x in range(iterations)])
        time.sleep(sleep)

# unit test class
class TestRuntimeFunction(ut.TestCase): 

    # error message in case if test case got failed 
    message = "Data amount/type failed."

    # generates data for testing
    def generate_test_data(self, count):
        # generate test data
        output_data = []
        for x in range(count):
            elapsed = time_function(other_function, 3, 0.1)  
            output_data.append(elapsed)
        
        return output_data
    
    # tests whether proper amount of data was generated
    def test_columns(self): 
        test_data = self.generate_test_data(40)

        # check if test passed
        self.assertEqual(40, len(test_data), self.message)

    # tests whether all datapoints are of type float (x.xxxx)
    def test_datatypes(self):
        test_data = self.generate_test_data(50)
        
        float_status = True
        for point in test_data:
            if isinstance(point, float) == False:
                float_status = False
                break
        
        self.assertEqual(float_status, True, self.message)
        


if __name__ == '__main__': 
    ut.main()