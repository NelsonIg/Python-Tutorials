import time
import threading

def myfunc(name):
    print(f'my func started with {name}')
    time.sleep(10)
    print(f'myfunc ended')

if __name__ == '__main__':
    print('main started')
    # we can pass arguments to threaded function too!
    # Deamon enables the main thread to end without waiting for the thread to finish
    t = threading.Thread(target=myfunc, args=['realpython'], daemon=True)
    t.start()
    print('main ended')