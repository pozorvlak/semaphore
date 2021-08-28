leaders = followers = 0
mutex = Semaphore(1)
leaderQueue = Semaphore(0)
followerQueue = Semaphore(0)
# barrier = Barrier(2)
rendezvous = Semaphore(0)
dancers = {}
def dance(me, position, dancers):
    assert position not in dancers
    dancers[position] = me
    if 'leader' in dancers and 'follower' in dancers:
        print(f"The handsome {dancers['leader']} is dancing with the lovely {dancers['follower']}")

## Thread leader * 2
mutex.wait()
    if followers > 0:
        followers -= 1
        followerQueue.signal()
    else:
        leaders += 1
        mutex.signal()
        leaderQueue.wait()
    # dance(pid(), 'leader', dancers)
    # barrier.phase1()
    # del dancers['leader']
    # barrier.phase2()
    rendezvous.wait()
mutex.signal()

## Thread follower * 2
mutex.wait()
    if leaders > 0:
        leaders -= 1
        leaderQueue.signal()
    else:
        followers += 1
        mutex.signal()
        followerQueue.wait()
    # dance(pid(), 'follower', dancers)
    # barrier.phase1()
    # del dancers['follower']
    # barrier.phase2()
    rendezvous.signal()
