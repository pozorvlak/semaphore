# scenario setup and assertions
readers = []
writers = []

num_writers = 0
num_readers = 0
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
readSwitch = Semaphore(1)
roomEmpty = Semaphore(1)
turnstile = Semaphore(1)
writers_mutex = Semaphore(1)  # Used for synchronising assert variables

## Thread reader * 2
turnstile.wait()
turnstile.signal()
readSwitch.wait()
    if num_readers == 0:
        roomEmpty.wait()
    num_readers += 1
readSwitch.signal()
read()
finish_reading()
readSwitch.wait()
    num_readers -= 1
    if num_readers == 0:
        roomEmpty.signal()
readSwitch.signal()
balk()


## Thread writer
turnstile.wait()
writers_mutex.wait()
    if num_writers == 0:
        allowed_readers = readers
    num_writers += 1
writers_mutex.signal()
roomEmpty.wait()
write()
finish_writing()
turnstile.signal()
roomEmpty.signal()
writers_mutex.wait()
    num_writers -= 1
writers_mutex.signal()
balk()
