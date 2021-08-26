thread_count = 4
mutex = Semaphore(1)
finished = 0
thread_finished = Semaphore(0)
all_finished = Semaphore(0)

## Thread A
print("Thread A finished")
mutex.wait()
finished += 1
mutex.signal()
thread_finished.signal()
all_finished.wait()

## Thread B
print("Thread B finished")
mutex.wait()
finished += 1
mutex.signal()
thread_finished.signal()
all_finished.wait()

## Thread C
print("Thread C finished")
mutex.wait()
finished += 1
mutex.signal()
thread_finished.signal()
all_finished.wait()

## Thread D
print("Thread D finished")
mutex.wait()
finished += 1
mutex.signal()
thread_finished.signal()
all_finished.wait()

## Thread killer
thread_finished.wait()
if finished == thread_count:
    print("All threads have finished!")
    exit()
