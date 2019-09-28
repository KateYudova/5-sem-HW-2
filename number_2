"""
Home Work 2, exercise 2.
"""
def hashh(l, k):
    summ = 0
    for i in range(k):
        summ = ord(l[i]) - ord('a') + summ + 10
    return summ % 100
maxi = 0
t = 0
h = 0
ind = 0
ind_max = 0
a = [[] for i in range(100)]
k = input()
while len(k) > 0:
    p = k.split()
    for i in range(len(p)):
        a[hashh(p[i], len(p[i]))].append(p[i])
    k = input()
for j in range(0, len(a)):
    a[j] = sorted(a[j])
for j in range(0, len(a)):
    if len(a[j])-1 == 0:
        if maxi == 1:
            t = 1
        elif maxi < 1:
            t = 0
            maxi = 1
            ind_max = a[j][0]
    for i in range(0, len(a[j])-1):
        if a[j][i] != a[j][i+1] and h == 1:
            ind = a[j][i]
        if a[j][i] == a[j][i+1]:
            ind = a[j][i]
            h = h+1
        if a[j][i] != a[j][i+1]:
            if h == maxi:
                h = 0
                t = 1
            elif h > maxi:
                t = 0
                maxi = h
                h = 0
                ind_max = ind
    if h == maxi:
        t = 1
    if h > maxi:
        t = 0
        maxi = h
        ind_max = ind
    h = 0
if t == 0:
    print (ind_max)
else:
    print ('-')
