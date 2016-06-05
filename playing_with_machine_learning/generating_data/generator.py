import math
import random

def random_number():
    result = 0
    for i in xrange(200):
        first_term = float(1)/ (float(16)**i) 
        second_term = float(4)/( 8*i + 1)
        third_term = float(2) / ( 8 * i + 4)
        fourth_term = float(1) / (8*i + 5)
        fifth_term = float(1) / (8*i + 6)
        result += first_term*( second_term - third_term - fourth_term - fifth_term ) 
    return result

if __name__ == '__main__':
    print random_number()
