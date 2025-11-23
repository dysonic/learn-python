# This is Python3 code - see https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
import urllib.request

# Does nothing
#dir(urllib.request.urlopen)

# When we find the function in the module we want to use, we can read more about it with the `help` function, using the Python interpreter:
#help(urllib.request.urlopen)

with urllib.request.urlopen("http://www.python.org") as url:
    s = url.read()
    # I'm guessing this would output the html source code ?
    print(s)