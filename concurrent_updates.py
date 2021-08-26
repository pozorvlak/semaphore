temp, count = 0, 0
a_count, b_count = 0, 0

## Thread A
temp = count
count = temp + 1
a_count += 1
print(count, a_count + b_count)

## Thread B
temp = count
count = temp + 1
b_count += 1
