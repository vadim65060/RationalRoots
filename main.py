n = int(input('n='))
ratios = []
alf = 'ABCDEFGHIKLMNOPQRSTVXYZ'
for i in range(n + 1):
    ratios.append(int(input(alf[i] + '=')))

mbq = []
for i in range(1, ratios[0] + 1):
    if ratios[0] % i == 0:
        mbq.append(i)
print('q:', mbq)

mbp = []
for i in range(1, ratios[-1] + 1):
    if ratios[0] % i == 0:
        mbp.append(i)
print('p:', mbp)

res = []
for p in mbp:
    for q in mbq:
        x = p / q
        sm = 0
        for i in range(n + 1):
            sm += ratios[i] * pow(x, (n - i))
        if sm == 0 and res.count(x) == 0:
            print(p, '/', q)
            res.append(x)