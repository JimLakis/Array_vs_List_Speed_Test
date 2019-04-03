# Clocking time taken to multiply two arrays verses two lists.
# Python v3.6
# Author: Jim L
# January, 2019



import numpy as np
import sys
import time
#from decimal import Decimal

import matplotlib.pyplot as plt
from pylab import *


class GenArray:
    def __init__ (self, len):
        self._len = len
        
    def array_generator(self):
        a = np.random.rand(self._len)
        return a


def main():
    
    max_array_elements = (100000000)
    template_array = GenArray(len = max_array_elements).array_generator()
    array_slice_num = (999, 9999, 99999, 999999, 9999999) # 99999999
    
    #### Time points to multiply two lists
    list_seconds = []
    dict_elements_seconds = {}
    for i in array_slice_num:
        start_time = time.time()
        resultant_list = [a * a for a in template_array[:i]]
        #resultant_list = None
        end_time = time.time()
        difference_time = end_time - start_time
        dict_elements_seconds[i+1] = difference_time
        list_seconds.append(difference_time)
    print(f"Time to multiply two lists, element by element")
    print(f"keys: number of elements in list. values: time in seconds")
    print(dict_elements_seconds) # Key/Value pairs
    #print(list_seconds)

    #### Time points to multiply two arrays
    array_seconds = []
    dict_elements_seconds2 = {}
    for i in array_slice_num:
        start_time = time.time()
        resultArray = template_array[:i] * template_array[:i]
        #resultant_list = None
        end_time = time.time()
        difference_time = end_time - start_time
        dict_elements_seconds2[i+1] = difference_time
        array_seconds.append(difference_time)
    print(f"\nTime to multiply two arrays, element by element")
    print(f"keys: number of elements in array. values: time in seconds")
    print(dict_elements_seconds2)
    #print(array_seconds)
    
    
    x = array_slice_num
    yArr = array_seconds
    yList = list_seconds
    
    plt.subplot(2, 1, 1) # sizing the chart
    plt.plot(x, yArr, 'b', label='Array')
    plt.plot(x, yList, 'r', label='List')
    plt.xscale('log')
    plt.grid(True)
    
    plt.legend(loc='upper left', shadow=True, title="Iterables:")
    plt.xlabel('elements in iterable')
    plt.ylabel('seconds')
    plt.title('Time to multiply an array and a list containing random\n64-bit values of less than one upon itself,\nelement by element ')
    
    plt.show()
    
    
if __name__ == '__main__':
    main()