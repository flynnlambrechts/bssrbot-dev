import sys
from linecache import (checkcache, getline)

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    checkcache(filename)
    line = getline(filename, lineno, f.f_globals)
    print(f'EXCEPTION IN ({filename}, LINE {lineno} "{line.strip()}"): {exc_obj}')

Range = list(range(1,10))

try:
	for i in range(0,11):
		print(Range[i])
except:
	PrintException()

