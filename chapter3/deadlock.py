n = 5
count = 0
mutex = Semaphore(1)
barrier = Semaphore(0)

## Thread A * 5
# Rendezvous

mutex.wait()
    count = count + 1
    if count == n: barrier.signal()

    barrier.wait()
    barrier.signal()

mutex.signal()

# critical point
