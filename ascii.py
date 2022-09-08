n = int(input())
for i in range(n):
    sentence = input()

values = []

for i in sentence:
    values.append(ord(i))

max = max(values)
min = min(values)
difference = max - min

print(difference)