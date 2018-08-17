input()

a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = 0

for i in a:
	if not i in b:
		c += 1

print(c)