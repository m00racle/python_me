This is Python app that should be run as :
e:/python_me/ocw_env/Scripts/python.exe e:/python_me/6-006_python/lec02_code/docdist1.py
This is because the location of the python.exe virtual environment is different from the current address.

To simplify things I want to test relative address:
1. first you must be in the python_me/6-006_python/lec02_code folder
2. then use this relative address:
../../ocw_env/Scripts/python.exe ./docdist1.py <filename1> <filename2>

It worked. A bit tideous but it will make the program runs agnostic to file system. In case this program is running on different machine the relative command will always work.