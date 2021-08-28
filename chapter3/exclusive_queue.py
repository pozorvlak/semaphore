leader_mutex = Semaphore(1)
follower_mutex = Semaphore(1)
leader_present = Semaphore(0)
follower_present = Semaphore(0)
first_leader = None
first_follower = None

## Thread leader * 10
leader_mutex.wait()
    first_leader = pid()
    leader_present.signal()
leader_mutex.signal()
follower_present.wait()
print(pid() + " is dancing with the lovely " + first_follower)

## Thread follower * 10
follower_mutex.wait()
    first_follower = pid()
    follower_present.signal()
follower_mutex.signal()
leader_present.wait()
print(pid() + " is dancing with the handsome " + first_leader)
