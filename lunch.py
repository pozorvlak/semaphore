lunch = Semaphore(1)

## Thread Alice

print("Alice is monitoring the power plant")
lunch.wait() # Alice is hungry
print("Alice is having lunch")
lunch.signal() # Alice has finished lunch


## Thread Bob

print("Bob is monitoring the power plant")
lunch.wait() # Bob is hungry
print("Bob is having lunch")
lunch.signal() # Bob has finished lunch
