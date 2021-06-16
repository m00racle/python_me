This is Python app that should be run as :
e:/python_me/ocw_env/Scripts/python.exe e:/python_me/6-006_python/lec02_code/docdist1.py
This is because the location of the python.exe virtual environment is different from the current address.

To simplify things I want to test relative address:
1. first you must be in the python_me/6-006_python/lec02_code folder
2. then use this relative address:
../../ocw_env/Scripts/python.exe ./<docdist> <filename1> <filename2>

It worked. A bit tideous but it will make the program runs agnostic to file system. In case this program is running on different machine the relative command will always work.

WARNING: some texts are so long that it will take some time to finish the document distance analysis. Reccommending to use t1 and t2 as basis for initial testing runs.


TypeError: 'dict_items' object is not subscriptable
https://stackoverflow.com/questions/58183904/how-to-fix-typeerror-dict-keys-object-is-not-subscriptable
the docdist 4,5,and 6 shows the same error.
This error is because the object dict.items() is not indexable. This is the case for Python 3.X unlike in the Python 2.7.
Thus it needed to be changed to list.
This why in docdist4.py line 106 I change it to list(D.items()) => and this allows the insertion_sort function to works!


For Debug function other than the VSCODE internal debugger (which require using the central Python debugger) or using Python Debugger (pdb) library: https://docs.python.org/3/library/pdb.html
This library is not as versatile as the VSCODE debugger since there is no console which display each expression and stack trace. In the pdb library all that function is also available 