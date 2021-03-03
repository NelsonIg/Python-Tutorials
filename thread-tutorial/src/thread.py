import time


def myfunc():
    print('hello')
    time.sleep(10) # represent something that blocks
    return True

if __name__ == '__main__':
    myfunc()