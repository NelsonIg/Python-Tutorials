import concurrent.futures
import time

def myfunc(name):
    print(f'myfunc started with {name}')
    time.sleep(10)
    print(F'myfunc ended with {name}')


if __name__ == '__main__':
    print('main begins')
    # context manager handles start and join of threads automatically
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
        e.map(myfunc, ['foo', 'bar', 'baz'])
    print('main ends')