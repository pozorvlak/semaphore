# scenario setup and assertions
readers = []
writers = []

def read():
    assert writers == [], f"{pid()} tried to read while {writers} were writing"
    readers.append(pid())


def finish_reading():
    readers.remove(pid())


def write():
    assert writers == [], f"{pid()} tried to write while {writers} were writing"
    assert readers == [], f"{pid()} tried to write while {readers} were reading"
    writers.append(pid())


def finish_writing():
    writers.remove(pid())

# synchronisation variables
mutex = Semaphore(1)
readers_mutex = Semaphore(1)
num_readers = 0

## Thread reader * 2
readers_mutex.wait()
    if num_readers == 0:
        mutex.wait()
    num_readers += 1
readers_mutex.signal()
read()
finish_reading()
readers_mutex.wait()
    num_readers -= 1
    if num_readers == 0:
        mutex.signal()
readers_mutex.signal()
balk()


## Thread writer * 2
mutex.wait()
write()
finish_writing()
mutex.signal()
balk()
