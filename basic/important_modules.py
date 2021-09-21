import os
import sys
from datetime import date


def year_is(year):
    """
    Define whether a year is high or not
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 366
    else:
        return 365


def days_diff(date1, date2):
    """
    Return the difference between two dates
    """
    year1, month1, day1 = date1
    year2, month2, day2 = date2
    days1, days2 = date(year1, month1, day1), date(year2, month2, day2)
    return abs(days2 - days1).days


print(days_diff((1982, 4, 19), (1982, 4, 22)))
print(days_diff((2014, 1, 1), (2014, 8, 27)))


# Shows the name of the OS
print(os.name)

# Some environment variables
print(os.environ)

# - the name of the user logged into the terminal (Unix).
print(os.getlogin())

# Return current process id
print(os.getpid())

# information about the OS. returns an object with the following attributes:
# sysname is the name of the operating system, nodename is the name of the machine on
# the network (implementation-defined), release is the release, version is the version,
# machine is the machine ID.
print(os.uname())

# Checking access to the object for the current user. Flags: os.F_OK - object exists
print(os.access("/home/myadmin/PycharmProjects/python_education/basic/sets.py", 2))

# Show value of enviroment variable or return None
print(os.getenv("TMP"))

# Show path to current working directory
print(os.getcwd())

# Change the path of working directory
# print(os.chdir("/home/myadmin/PycharmProjects/python_education/"))

# Create folder
# os.mkdir("test")

# Creates intermediate folders in the path if they are not there
# os.makedirs("/home/myadmin/PycharmProjects/python_education/test/test/test")

# Delete file if file exists or raise FileNotFoundError
# os.remove("test.txt")

# Delete directory if directory exist or raise FileNotFoundError
# os.rmdir("pytest")

# Rename file if file exist or raise FileNotFoundError
# os.rename("test.txt", "pytest.txt")

# Open the file. Only for win32. raise AttributeError
# os.startfile("/home/myadmin/PycharmProjects/python_education/basic/sets.py")

# Show the entire list of directories and files.
for root, dirs, files in os.walk("/home/myadmin/PycharmProjects/python_education/basic"):
    print(root)
    for _dir in dirs:
        print(_dir)
    print('**********************************')
    for _file in files:
        print(_file)


# Return a list of command line arguments to pass to the Python script.
print(sys.argv)

# Return byte order: little or big
print(sys.byteorder)

# Return a tuple of strings containing the names of all available modules.
print(sys.builtin_module_names)

# Return a string containing copyright related to the Python interpreter.
print(sys.copyright)

# returns a dictionary-mapping of the identifier for each thread in the top frame
# of the stack currently on that thread at the time the function is called.
print(sys._current_frames())

# returns a tuple of three values that give information about the exceptions currently being handled.
print(sys.exc_info())

# Return Python installation directory
print(sys.exec_prefix) # - каталог установки Python.

# Return path to Python interpreter
print(sys.executable)

# Return command line flags. Read-only attributes.
print(sys.flags)

# Return information about the data type float.
print(sys.float_info)

# Return the encoding used.
print(sys.getdefaultencoding())

# returns the encoding of the filesystem.
print(sys.getfilesystemencoding())


# returns the number of references to an object. The getrefcount
# function argument is another object reference.
a = 1
print(sys.getrefcount(a))

# Return the recursion limit.
print(sys.getrecursionlimit())

# Returns the size of the object (in bytes).
print(sys.getsizeof(a))

# Return information about hashing parameters.
print(sys.hash_info)

# Return an object containing information about the running python interpreter
print(sys.implementation)

# the maximum number of bits to store a Unicode character
print(sys.maxunicode)

# Return list of module search paths.
print(sys.path)

# Return dictionary-cache for searching objects.
print(sys.path_importer_cache)
