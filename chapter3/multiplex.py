capacity = Semaphore(2)

## Thread A
capacity.wait()
print("A is in the room")
capacity.signal()
print("A has left the building")

## Thread B
capacity.wait()
print("B is in the room")
capacity.signal()
print("B has left the building")

## Thread C
capacity.wait()
print("C is in the room")
capacity.signal()
print("C has left the building")
