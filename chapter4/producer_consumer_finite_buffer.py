handled = set()

class Event:

    def __init__(self, counter):
        self.counter = counter

    def __repr__(self):
        return f"<Event {self.counter}>"

    def process(self):
        handled.add(self)

max_events = 10
event_queue = [Event(i) for i in range(max_events)]

def waitForEvent():
    return event_queue.pop(0) if len(event_queue) > 0 else None


class Buffer:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def get(self):
        if len(self) == 0:
            return None
        return self.queue.pop(0)

    def add(self, value):
        self.queue.append(value)
        assert len(self) <= self.size, "Event added to full buffer"

    def full(self):
        return len(self) >= self.size

    def __len__(self):
        return len(self.queue)


bufferSize = 2
buffer = Buffer(bufferSize)
buffer_space = Semaphore(bufferSize)
mutex = Semaphore(1)
events_available = Semaphore(0)

num_producers = 2
producers_finished_mutex = Semaphore(1)
all_producers_finished = Semaphore(0)
producers_finished_count = 0

num_consumers = 2
consumers_finished_mutex = Semaphore(1)
all_consumers_finished = Semaphore(0)
consumers_finished_count = 0


## Thread producer * 2
self.event = waitForEvent()
if self.event is not None:
    buffer_space.wait()
    mutex.wait()
        buffer.add(self.event)
        print(f"{self.event} ADDED TO BUFFER by {pid()}")
    mutex.signal()
    events_available.signal()
    balk()
else:
    producers_finished_mutex.wait()
        producers_finished_count += 1
        if producers_finished_count == num_producers:
            all_producers_finished.signal()
    producers_finished_mutex.signal()


## Thread consumer * 2
events_available.wait()
mutex.wait()
    self.event = buffer.get()
mutex.signal()
buffer_space.signal()
if self.event is not None:
    self.event.process()
    print(f"{self.event} HANDLED by {pid()}")
    balk()
else:
    consumers_finished_mutex.wait()
        consumers_finished_count += 1
        if consumers_finished_count == num_consumers:
            all_consumers_finished.signal()
    consumers_finished_mutex.signal()


## Thread queue drainer
all_producers_finished.wait()
while len(buffer) > 0:
    print(f"{len(buffer)} events left to process, signalling")
    events_available.signal()
while consumers_finished_count < num_consumers:
    events_available.signal()


## Thread checker
all_consumers_finished.wait()
num_unhandled = max_events - len(handled)
assert num_unhandled == 0, f"{num_unhandled} events not handled"
