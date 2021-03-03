import time
import threading

def myfunc(name):
    print(f'my func started with {name}')
    time.sleep(10)
    print(f'myfunc ended')

def myfunc2(name):
    print(f'my func2 started with {name}')
    time.sleep(10)
    print(f'myfunc2 ended')

def myfunc3(name):
    print(f'my func3 started with {name}')
    time.sleep(10)
    print(f'myfunc3 ended')

if __name__ == '__main__':
    print('main started')
    # we can pass arguments to threaded function too!
    t = threading.Thread(target=myfunc, args=['realpython'])
    t.start()
    t2 = threading.Thread(target=myfunc2, args=['foo'])
    t2.start()
    t3 = threading.Thread(target=myfunc3, args=['bar'])
    t3.start()
    t.join()  # block until t finishes
    t2.join()  # block until t finishes
    t3.join()  # block until t finishes
    print('main ended')