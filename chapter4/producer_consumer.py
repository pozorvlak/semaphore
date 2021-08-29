class Event:
    event_counter = 0
    def __init__(self, counter):
        self.counter = counter

    def process(self):
        print(f"Event {self.counter} processed")

    @classmethod
    def waitForEvent(cls):
        cls.event_counter += 1
        return cls(cls.event_counter)


class Buffer:
    def __init__(self):
        self.queue = []

    def get(self):
        return self.queue.pop(0)

    def add(self, value):
        self.queue.append(value)

buffer = Buffer()
mutex = Semaphore(0)
events_available = Semaphore(0)

## Thread producer * 2
event = Event.waitForEvent()
mutex.wait()
    buffer.add(event)
mutex.signal()

## Thread consumer * 2
mutex.wait()
    event = buffer.get()
mutex.signal()
event.process()
