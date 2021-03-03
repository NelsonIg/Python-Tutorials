import time
import threading

def myfunc(name):
    print(f'my func started with {name}')
    time.sleep(10)
    print(f'myfunc ended')

if __name__ == '__main__':
    print('main started')
    t = threading.Thread(target=myfunc, args=['realpython']) # we can pass arguments to threaded function too!
    t.start()
    print('main ended')