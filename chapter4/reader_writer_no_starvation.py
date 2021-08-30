# scenario setup and assertions
readers = []
writers = []

num_writers = 0
allowed_readers = []


def read():
    assert num_writers == 0 or pid() in allowed_readers, \
            f"{pid()} is a new reader, but a writer is waiting"
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
writers_mutex = Semaphore(1)

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


## Thread writer
writers_mutex.wait()
    if num_writers == 0:
        allowed_readers = readers
        mutex.wait()
    num_writers += 1
writers_mutex.signal()
write()
finish_writing()
writers_mutex.wait()
    num_writers -= 1
    if num_writers == 0:
        mutex.signal()
writers_mutex.signal()
balk()
