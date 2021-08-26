n = 4
count = 0
mutex = Semaphore(1)
barrier = Semaphore(0)
finished_mutex = Semaphore(1)
finished_count = 0
thread_finished = Semaphore(0)
all_finished = Semaphore(0)

## Thread 1
print("Thread 1 at rendezvous")
mutex.wait()
count = count + 1
mutex.signal()
if count < n :
    barrier.wait()
else:
    barrier.signal(count)
print("Thread 1 finished!")
finished_mutex.wait()
finished_count += 1
finished_mutex.signal()
thread_finished.signal()
all_finished.wait()

## Thread 2
print("Thread 2 at rendezvous")
mutex.wait()
count = count + 1
mutex.signal()
if count < n:
    barrier.wait()
else:
    barrier.signal(count)
print("Thread 2 finished!")
finished_mutex.wait()
finished_count += 1
finished_mutex.signal()
thread_finished.signal()
all_finished.wait()

## Thread 3
print("Thread 3 at rendezvous")
mutex.wait()
count = count + 1
mutex.signal()
if count < n:
    barrier.wait()
else:
    barrier.signal(count)
print("Thread 3 finished!")
finished_mutex.wait()
finished_count += 1
finished_mutex.signal()
thread_finished.signal()
all_finished.wait()

## Thread 4
print("Thread 4 at rendezvous")
mutex.wait()
count = count + 1
mutex.signal()
if count < n:
    barrier.wait()
else:
    barrier.signal(count)
print("Thread 4 finished!")
finished_mutex.wait()
finished_count += 1
finished_mutex.signal()
thread_finished.signal()
all_finished.wait()

## Thread killer
thread_finished.wait()
if finished_count == n:
    print("All threads have finished!")
    exit()
balk()
