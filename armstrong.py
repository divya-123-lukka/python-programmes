n = int(input())

s = 0
t = n

while t > 0:
    d = t % 10
    s += d ** 3
    t //= 10

if s == n:
    print("Armstrong")
else:
    print("Not Armstrong")
