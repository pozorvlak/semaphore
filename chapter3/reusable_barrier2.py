n = 4
barrier = Barrier(n)
laps = {'A-' + str(i): 0 for i in range(n)}

## Thread A * 4
# Rendezvous
laps[pid()] += 1
barrier.phase1()

# Critical point
assert max(laps.values()) == min(laps.values()), laps

barrier.phase2()

balk()
