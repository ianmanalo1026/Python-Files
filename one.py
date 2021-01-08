def func():
    print("Func() in ine.py")


print("top level in one.py")

if __name__ == '__main__':
    print('One.py is being run directly')
else:
    print('one.py has been imported!')
