#!/usr/bin/env python
# coding: utf-8
Question 1 . what is multithreading in python? why is it used? Name the module used to handle threads in python. Answer :Multithreading in Python refers to the ability of a program to create and execute multiple threads simultaneously, allowing multiple tasks to be performed concurrently. A thread is a lightweight subprocess that runs concurrently with other threads in a single process.

Multithreading is used in Python to improve the performance of programs that have tasks that can be executed concurrently. By using threads, the program can perform multiple tasks simultaneously, which can significantly reduce the execution time of the program. Multithreading is particularly useful for I/O-bound tasks, such as reading from or writing to files, network communication, or database access, as threads can overlap I/O operations to increase efficiency.

The module used to handle threads in Python is called threading. It provides a simple and easy-to-use interface for creating and managing threads in Python. The threading module allows you to create and start new threads, pause and resume existing threads, and communicate between threads using synchronization primitives such as locks, events, and semaphores.Question 2. Why threading module used? Write the use of the following functions a. activeCount() b. currentThread() c. enumerate() Answer :The threading module in Python is used for creating and managing threads in a program. It provides a simple and efficient way to implement concurrency in Python programs. Here are the uses of some of the functions provided by the threading module:

a. activeCount(): This function returns the number of Thread objects that are currently active in the current Python interpreter. An active thread is a thread that has been created but has not yet finished its execution.

b. currentThread(): This function returns a reference to the current thread object. The current thread is the thread that is currently executing the Python code.

c. enumerate(): This function returns a list of all Thread objects that are currently active in the current Python interpreter. Each Thread object in the list represents a separate thread of execution. The list includes the main thread, as well as any additional threads that have been created using the threading module.

The enumerate() function can be used to iterate over all active threads and perform some action on each thread. For example, you can use it to check the status of each thread, pause or resume a specific thread, or terminate a thread if necessary. Overall, these functions are useful for managing and debugging threads in a Python program, and they provide an easy way to access information about the current state of the threading system.ouestion 3. Explain the following functions a. run() b. start() c. join() d. isAlive() Answer:In Python's threading module, the following functions are related to the creation, execution, and management of threads:

a. run(): This is the method that is executed when a thread is started using the start() method. This method can be overridden in a subclass to define the behavior of the thread.

b. start(): This method starts a new thread of execution. When called, it creates a new thread and calls the run() method of the thread. The start() method does not wait for the thread to finish executing; instead, it returns immediately, allowing the calling thread to continue its own execution.

c. join(): This method waits for the thread to finish executing before the calling thread can continue. When called, it blocks the calling thread until the thread being joined completes its execution. The join() method is typically used to ensure that a thread has finished executing before the main program exits or before another thread needs to access data that the first thread is modifying.

d. isAlive(): This method returns a boolean value indicating whether the thread is currently executing or not. If the thread has finished executing, this method returns False; otherwise, it returns True. The isAlive() method can be used to check whether a thread is still running before calling the join() method.

Overall, these methods are important for managing threads in a Python program. The start() and run() methods are used to start a new thread and define its behavior, respectively. The join() method is used to wait for a thread to finish executing before continuing, while the isAlive() method is used to check whether a thread is still running or not.question 4. write a python program to create two threads. Thread one must print the list of squares and thread two must print the list of cubes. Answer: the print_squares() function prints the list of squares of numbers from 1 to n, and the print_cubes() function prints the list of cubes of numbers from 1 to n. Two threads are created using the Thread class from the threading module, one for each function. The start() method is called on both threads to start their execution, and the join() method is called on both threads to wait for their completion. Finally, a message is printed indicating that the program has finished executing. When run, this program should print the list of squares and cubes in parallel, interleaving the output of the two threads.
# In[1]:


import threading

def print_squares(n):
    for i in range(1, n+1):
        print(f"{i}**2 = {i*i}")

def print_cubes(n):
    for i in range(1, n+1):
        print(f"{i}**3 = {i*i*i}")

# Create two threads to print squares and cubes
t1 = threading.Thread(target=print_squares, args=(10,))
t2 = threading.Thread(target=print_cubes, args=(10,))

# Start both threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Done")

Question 5. State advantages and disadvantages of multithreading. Answer :Multithreading, which is the ability to run multiple threads of execution within a single process, has several advantages and disadvantages. Here are some of the major ones:

Advantages of Multithreading:

a.Improved performance: Multithreading can improve the performance of a program by allowing it to execute multiple tasks in parallel, thereby reducing the overall time taken to complete a task. b. Better resource utilization: Multithreading allows multiple threads to share the same resources such as memory and CPU, resulting in better utilization of resources. c. Responsiveness: Multithreading can make a program more responsive by allowing it to perform multiple tasks simultaneously, such as accepting user input while performing a background task. d. Simplified programming: Multithreading can simplify programming by allowing complex tasks to be broken down into smaller, more manageable threads. e. Better scalability: Multithreading allows a program to scale better by adding more threads to handle increasing workloads.

Disadvantages of Multithreading:

a. Increased complexity: Multithreading can add complexity to a program by requiring more careful coordination and synchronization of the threads, which can increase the chances of errors and bugs. b. Difficulty in debugging: Debugging multithreaded programs can be difficult because the execution of threads can be non-deterministic and hard to reproduce. c. Increased resource usage: Multithreading can increase the resource usage of a program, such as memory and CPU usage, due to the overhead of creating and managing multiple threads. d. Increased programming effort: Writing multithreaded programs can require additional effort to manage thread creation, synchronization, and communication between threads. e. Race conditions: Multithreading can introduce race conditions, where two or more threads access the same shared data at the same time, potentially resulting in incorrect or inconsistent behavior.

Overall, multithreading can be a powerful tool for improving the performance and responsiveness of a program, but it also introduces additional complexity and requires careful management to avoid issues such as race conditions and synchronization problems.Question 6. Explain deadlocks and race conditions. Answer :Deadlocks and race conditions are two types of concurrency issues that can occur in multithreaded programs.

a. Deadlocks: A deadlock occurs when two or more threads are blocked, waiting for each other to release a resource, resulting in a situation where no thread can make progress. In other words, each thread is waiting for another thread to release a resource it needs, resulting in a deadlock. Deadlocks can occur in situations where multiple threads are trying to access shared resources such as memory or locks.

For example, consider two threads, A and B, where thread A holds a lock on resource 1 and is waiting to acquire a lock on resource 2, while thread B holds a lock on resource 2 and is waiting to acquire a lock on resource 1. Neither thread can proceed, resulting in a deadlock.

b.Race conditions: A race condition occurs when the behavior of a program depends on the timing and order of thread execution, leading to unpredictable and often incorrect behavior. In other words, the output of the program depends on which thread executes first and how long each thread takes to execute. Race conditions can occur when multiple threads access shared resources such as memory or files without proper synchronization.

For example, consider two threads, A and B, where thread A reads a variable, modifies it, and writes it back, while thread B reads the same variable, modifies it, and writes it back. If both threads access the variable at the same time without proper synchronization, the final value of the variable may be unpredictable and depend on the timing and order of the thread execution.

To avoid deadlocks and race conditions, multithreaded programs need to carefully manage shared resources and use synchronization mechanisms such as locks, semaphores, and condition variables to ensure that threads access shared resources in a safe and coordinated manner.

 