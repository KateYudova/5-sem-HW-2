"""
Home Work 2, exercise 1.
"""
a = input()
i = 0
flag = 0
k = 0
z = 0
t = ''
while i == 0:
    j = 0
    t = t+a[z]
    z = z+1
    if len(a)%len(t) == 0:
        k = 0
        flag = 1
        while j < len(a)//len(t):
            for i in range(len(t)):
                if t[i] == a[k*len(t)+i]:
                    flag = 1
                else:
                    flag = 0
                    break
            k = k + 1
            i = 0
            j = j + 1
            if flag == 0:
                break
        if flag == 1:
            print(k)
            break
    if len(t) == len(a):
        k = 1
        i = 1
        print(k)
