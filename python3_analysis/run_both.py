from subprocess import call

print "Running python 2 code"
call(["python","python2_code.py"])
print "Running python 3 code"
call(["python3","python2_code.py"])
