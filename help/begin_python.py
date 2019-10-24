### Filename = testfile.py

class Smoke_Test:
# 200 status expected 
    username = "smoketestuser"
    file = "smoke.pdf"

=========================

### In another python script 

from testfile import *

x = vars(Smoke_Test)
x.get('username')
