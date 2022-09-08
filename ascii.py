n = int(input())
for i in range(n):
    sentence = input()

values = []

for i in sentence:
    values.append(ord(i))

mx = max(values)
mn = min(values)
difference = mx - mn

print(difference)