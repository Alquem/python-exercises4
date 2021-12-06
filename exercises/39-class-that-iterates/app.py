def gen(n):
    for i in range(n):
        if i % 7 == 0:
            yield i

N = int(input())
for i in gen(N):
    print(i)