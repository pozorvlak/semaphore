leader = Semaphore(0)
follower = Semaphore(0)

## Thread leader * 10
leader.signal()
follower.wait()
# You dancin'?

## Thread follower * 10
follower.signal()
leader.wait()
# You askin'?
