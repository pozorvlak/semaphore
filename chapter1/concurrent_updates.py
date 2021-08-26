a_temp, b_temp, count = 0, 0, 0
a_count, b_count = 0, 0

## Thread A
a_temp = count
count = a_temp + 1
a_count += 1
print(count, a_count + b_count)

## Thread B
b_temp = count
count = b_temp + 1
b_count += 1
