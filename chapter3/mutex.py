mutex = Semaphore(1)
count = 0

## Thread A
mutex.wait()
a_temp = count
count = a_temp + 1
mutex.signal()

## Thread B
mutex.wait()
b_temp = count
count = b_temp + 1
mutex.signal()
