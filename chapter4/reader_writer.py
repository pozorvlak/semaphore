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


## Thread reader * 2
read()
finish_reading()
balk()


## Thread writer * 2
write()
finish_writing()
balk()
