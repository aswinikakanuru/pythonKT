#Multithreading means running multiple threads within the same process to handle multiple tasks concurrently.
import threading

def task():
    print("Task is running")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

print("Main program completed")

#What is Multiprocessing?(Multiprocessing means running multiple processes to perform tasks concurrently or in parallel.)

from multiprocessing import Process

def task():
    print("Task is running")


def main():
    p1 = Process(target=task)
    p2 = Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main program completed")


if __name__ == "__main__":
    main()