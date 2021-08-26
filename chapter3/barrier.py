finished = Semaphore(-5)
thread_finished = Semaphore(0)
arrived = Semaphore(-4)
all_arrived = Semaphore(0)

## Thread 1
arrived.signal()
all_arrived.wait()
print("Thread 1 finished!")
finished.signal()
thread_finished.wait()

## Thread 2
arrived.signal()
all_arrived.wait()
print("Thread 2 finished!")
finished.signal()
thread_finished.wait()

## Thread 3
arrived.signal()
all_arrived.wait()
print("Thread 3 finished!")
finished.signal()
thread_finished.wait()

## Thread 4
arrived.signal()
all_arrived.wait()
print("Thread 4 finished!")
finished.signal()
thread_finished.wait()

## Thread barrier
arrived.wait()
all_arrived.signal()
all_arrived.signal()
all_arrived.signal()
all_arrived.signal()
print("Barrier reached!")
finished.signal()
thread_finished.wait()

## Thread killer
finished.wait()
print("All threads have finished!")
exit()
