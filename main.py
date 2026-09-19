"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

#from test_main import test_quadratic_multiply, test_subquadratic_multiply

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def quadratic_multiply(x, y):
    ### TODO
    #make sure the vectors are even and the same size so we can divide easier
    n= max(len(x.binary_vec), len(y.binary_vec))

    # check base case first tho 
    if n <=1:
            x_bit = int(x.binary_vec[0]) if len(x.binary_vec) > 0 else 0
            y_bit = int(y.binary_vec[0]) if len(y.binary_vec) > 0 else 0
            result= x_bit * y_bit
            return BinaryNumber(result)

    # if its more than 1 and odd, then add one
    if n%2 != 0:
        n+=1
    #add 0 infront of the binary vector to make it the same size
    x_new = ['0']*(n-len(x.binary_vec)) + x.binary_vec
    y_new = ['0']*(n-len(y.binary_vec)) + y.binary_vec

    #next we will split the binary vectors in half
    mid = n//2
    x_l= x_new[:mid]
    x_r= x_new[mid:]
    y_l= y_new[:mid]
    y_r= y_new[mid:]

    #convert the binary vectors back to decimal numbers because our BinaryNumber takes in integers
    # ''.join joins our list, and 2 is so it knows its base 2
    x_l_num = int(''.join(x_l),2)
    x_r_num = int(''.join(x_r),2)   
    y_l_num = int(''.join(y_l),2)
    y_r_num = int(''.join(y_r),2)   

    #recursive call to multiply our halves 
    x_l_y_l = quadratic_multiply(BinaryNumber(x_l_num), BinaryNumber(y_l_num))
    x_r_y_r = quadratic_multiply(BinaryNumber(x_r_num), BinaryNumber(y_r_num))
    x_l_y_r = quadratic_multiply(BinaryNumber(x_l_num), BinaryNumber(y_r_num))
    x_r_y_l = quadratic_multiply(BinaryNumber(x_r_num), BinaryNumber(y_l_num))

    #the left value shifted, plus the middle values added and shifter plus the right value
    result = (x_l_y_l.decimal_val * (2**(n))) + ((x_l_y_r.decimal_val + x_r_y_l.decimal_val) * (2**(mid))) + x_r_y_r.decimal_val
    return BinaryNumber(result)
    ###

def subquadratic_multiply(x, y, is_top_level=True):
    ### TODO
    #most of it is the same as quadratic multiply.
    n= max(len(x.binary_vec), len(y.binary_vec))
    
        # check base case first tho 
    if n <=1:
        x_bit = int(x.binary_vec[0]) if len(x.binary_vec) > 0 else 0
        y_bit = int(y.binary_vec[0]) if len(y.binary_vec) > 0 else 0
        result= x_bit * y_bit
        return BinaryNumber(result)
    
        # if its more than 1 and odd, then add one
    #if n%2 != 0:
        #n+=1
    #check for a power of 2 instead of just even to the division always divides smoothly after the first step
    #just at top level because once the top level is a power of 2,
    #the divisions will be even always. 
    if is_top_level:
        k = 1
        while k < n:
            k *= 2
        n=k    

    #add 0 infront of the binary vector to make it the same size
    x_new = ['0']*(n-len(x.binary_vec)) + x.binary_vec
    y_new = ['0']*(n-len(y.binary_vec)) + y.binary_vec
    
        #next we will split the binary vectors in half
    mid = n//2
    x_l= x_new[:mid]
    x_r= x_new[mid:]
    y_l= y_new[:mid]
    y_r= y_new[mid:]

#convert the binary vectors back to decimal numbers because our BinaryNumber takes in integers
    # ''.join joins our list, and 2 is so it knows its base 2
    x_l_num = int(''.join(x_l),2)
    x_r_num = int(''.join(x_r),2)   
    y_l_num = int(''.join(y_l),2)
    y_r_num = int(''.join(y_r),2)   

    #recursive call to multiply our halves 
    x_l_y_l = subquadratic_multiply(BinaryNumber(x_l_num), BinaryNumber(y_l_num), is_top_level=False)
    x_r_y_r = subquadratic_multiply(BinaryNumber(x_r_num), BinaryNumber(y_r_num), is_top_level=False)
   # middle = subquadratic_multiply(BinaryNumber(x_l_num + x_r_num), BinaryNumber(y_l_num + y_r_num))
   
   #compute the middle
    sum_x = x_l_num + x_r_num
    sum_y = y_l_num + y_r_num

    bin_sum_x = BinaryNumber(sum_x)
    bin_sum_y = BinaryNumber(sum_y)
    middle = subquadratic_multiply(bin_sum_x, bin_sum_y, is_top_level=False)

    #the left value shifted, plus the middle values added and shifter plus the right value
    result = (x_l_y_l.decimal_val *(2**(n)) + (middle.decimal_val - x_l_y_l.decimal_val - x_r_y_r.decimal_val)*(2**(mid)) + x_r_y_r.decimal_val)
    return BinaryNumber(result)
    #pass
    ###

def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x, y)
    return (time.time() - start)*1000
    
def compare_multiply():
    pass
    # compare the empirical runtimes of multiplication functions
    ### TODO - add test cases and measure runtime
    test_size =[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    print("Size\tQuadratic\tSubquadratic")
    for size in test_size:

        n1 = (2**size) -1
        n2 = (2**size) -3 

        x = BinaryNumber(n1)
        y = BinaryNumber(n2)

        time_quad = time_multiply(x, y, quadratic_multiply)
        time_subquad = time_multiply(x, y, subquadratic_multiply)

        print(f"{size}\t{time_quad:.6f}\t{time_subquad:.6f}")
    
compare_multiply()  

