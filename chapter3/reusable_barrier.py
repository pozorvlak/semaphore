n = 4
count = 0
mutex = Semaphore(1)
turnstile1 = Semaphore(0)
turnstile2 = Semaphore(1)
laps = {'A-' + str(i): 0 for i in range(n)}

## Thread A * 4
# Rendezvous
laps[pid()] += 1
mutex.wait()
    count = count + 1
    if count == n: turnstile2.wait()
    if count == n: turnstile1.signal()
mutex.signal()
turnstile1.wait()
turnstile1.signal()

# Critical point
assert max(laps.values()) == min(laps.values()), laps

mutex.wait()
    count -= 1
    if count == 0: turnstile1.wait()
    if count == 0: turnstile2.signal()
mutex.signal()
turnstile2.wait()
turnstile2.signal()

balk()
