from time import time
import simple_test
import simple

print "running simple python code:"
start_reg = time()
simple.main()
reg_result = time() - start_reg
print reg_result,"is how long regular python code took to run"
print "running compiled python code:"
start_comp = time()
simple_test.main()
comp_result = time() - start_comp
print comp_result,"is how long compiled python code took to run"

print "Analysis:"
print 
print

if reg_result < comp_result:
    print comp_result - reg_result,"is how much longer the compiled result took"
else:
    print reg_result - comp_result,"is how much longer the regular result took"

