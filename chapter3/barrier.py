n = 4
count = 0
mutex = Semaphore(1)
barrier = Semaphore(0)

## Thread A * 4
print("Thread " + pid() + " at rendezvous")
mutex.wait()
count = count + 1
mutex.signal()
if count == n : barrier.signal()
barrier.wait()
barrier.signal()
print("Thread " + pid() + " finished!")
