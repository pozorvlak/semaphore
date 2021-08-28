# We want to guarantee that a1 happens before b2 and b1 happens before a2
a1 = False
b1 = False
a1_sem = Semaphore(0)
b1_sem = Semaphore(0)

## Thread A
a1 = False
a1 = True # statement a1
a1_sem.signal()
b1_sem.wait()
assert b1 # statement a2

## Thread B
b1 = False
b1 = True # statement b1
b1_sem.signal()
a1_sem.wait()
assert a1 # statement b2
