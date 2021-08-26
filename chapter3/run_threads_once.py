finished = Semaphore(-4)
thread_finished = Semaphore(0)

## Thread A
print("Thread A finished")
finished.signal()
thread_finished.wait()

## Thread B
print("Thread A finished")
finished.signal()
thread_finished.wait()

## Thread C
print("Thread A finished")
finished.signal()
thread_finished.wait()

## Thread D
print("Thread A finished")
finished.signal()
thread_finished.wait()

## Thread killer
finished.wait()
print("All threads have finished!")
# exit()
thread_finished.wait()
