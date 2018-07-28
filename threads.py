import time
from threading import Thread

def ask_user():
    start = time.time()
    user_input = input('Enter name')
    greet = 'Hello, {}'.format(user_input)
    print(greet)
    print('ask user, {}'.format(time.time()-start))
def calc():
    start = time.time()
    print('start calculation')
    [x**2 for x in range(20000000)]
    print('calc, {}'.format(time.time() - start))


start_time = time.time()
ask_user()
calc()
print('single thread time {}'.format(time.time() - start_time))


thread1 = Thread(target=calc)
thread2 = Thread(target=ask_user)

start_time = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('2 threads run time {}'.format(time.time()-start_time))