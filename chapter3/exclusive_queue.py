leader_mutex = Semaphore(1)
follower_mutex = Semaphore(1)
leader_present = Semaphore(0)
follower_present = Semaphore(0)
first_leader = None
first_follower = None
partners = {}
def dance(me, other, partners):
    partners[me] = other
    if other in partners:
        assert partners[other] == me, f"{other} is already taken"
    print(me + " is dancing with " + other)

## Thread leader * 10
leader_mutex.wait()
    first_leader = pid()
    leader_present.signal()
leader_mutex.signal()
follower_present.wait()
dance(pid(), first_follower, partners)

## Thread follower * 10
follower_mutex.wait()
    first_follower = pid()
    follower_present.signal()
follower_mutex.signal()
leader_present.wait()
dance(pid(), first_leader, partners)
