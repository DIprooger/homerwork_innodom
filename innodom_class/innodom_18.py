def shift(numbers, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            numbers.append(numbers.pop(0))
    else:
        for i in range(steps):
            numbers.insert(0, numbers.pop())


nums = [4, 5, 6, 7, 8, 9, 0]
print(nums)

shift(nums, -2)
print(nums)

shift(nums, 3)
print(nums)


s = input('Enter text: ')
length = len(s)
numbers = []
i = 0

while i < length:
    s_int = ''
    while i < length and '0' <= s[i] <= '9':
        s_int += s[i]
        i += 1
    i += 1
    if s_int != '':
        numbers.append(int(s_int))

print(numbers)
