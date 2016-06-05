from subprocess import call

print "Running python 2 code"
call(["python","simple_test.py"])
print "Running python 3 code"
call(["python3","simple_test.py"])
