import unittest as ut
import sys
import time
import random


sys.path.append('src/runmetricsvisualizer')
from plot import generate_plot


# unit test class
class TestRuntimeFunction(ut.TestCase): 
    message = 'Unit test failed.'

    # possible params for testing
    plots = ['scatter', 'plot', 'stackplot']
    charts = ['default', 'dark_background', 'Solarize_Light2']
    
    # tests different plot styles
    def test_plot_generators(self):
        for x in range(5):    
           generate_plot('data/first_test.csv', random.choice(self.plots), random.choice(self.charts), savefile=f"tests/test-plots/testplot-{x}")



if __name__ == '__main__': 
    ut.main()