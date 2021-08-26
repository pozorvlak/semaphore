n = 4
count = 0
mutex = Semaphore(1)
barrier = Semaphore(0)

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
