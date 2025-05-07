# Operation: Start a process using multiprocessing.Process

from multiprocessing import Process

def square(n):
    print("Square:", n * n)

p = Process(target=square, args=(5,))
p.start()
p.join()
# Output: Square: 25
