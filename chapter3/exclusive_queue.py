leaders = followers = 0
mutex = Semaphore(1)
leaderQueue = Semaphore(0)
followerQueue = Semaphore(0)
rendezvous = Semaphore(0)
first_leader = None
first_follower = None
partners = {}
def dance(me, other, partners):
    partners[me] = other
    if other in partners:
        assert partners[other] == me, f"{other} is already taken"
    print(me + " is dancing with " + other)

## Thread leader * 2
mutex.wait()
    leaders += 1
    leaderQueue.signal()
    first_leader = pid()
mutex.signal()
followerQueue.wait()
dance(pid(), first_follower, partners)
mutex.wait()
    leaders -= 1
mutex.signal()
rendezvous.wait()

## Thread follower * 2
mutex.wait()
    followers += 1
    followerQueue.signal()
    first_follower = pid()
mutex.signal()
leaderQueue.wait()
# dance(pid(), first_leader, partners)
mutex.wait()
    followers -= 1
mutex.signal()
rendezvous.wait()
