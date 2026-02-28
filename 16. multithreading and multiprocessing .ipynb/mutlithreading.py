### Multithreading 
### went to use multi threading 
### i/o bound task:task spends more time waiting for i/o operaions(file opreation,neetwork issue)
### concurrent execution: when you want to improve the throught of your application by multiple operations concurently.
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f'number :{i}')

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f'Letter:{letter}')

## create 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)
t=time.time()
t1.start()
t2.start()

### wait for the thread to complete
t1.join()
t2.join()
finised_time=time.time()-t
print(finised_time)