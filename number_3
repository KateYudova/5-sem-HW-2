"""
Home Work 2, exercise 3.
"""
def number(g, y):
    """
    string number -> integer
    """
    c = g[y]
    num = ord(c)-ord('0')
    return num
def tel(L, num):
    """
    add letters and delete old elements
    """
    t = len(L)
    for j in range(t):
        if num == 1:
            return L
        elif num == 2:
            L.append(L[j] + "a")
            L.append(L[j] + "b")
            L.append(L[j] + "c")
        elif num == 3:
            L.append(L[j] + "d")
            L.append(L[j] + "e")
            L.append(L[j] + "f")
        elif num == 4:
            L.append(L[j] + "g")
            L.append(L[j] + "h")
            L.append(L[j] + "i")
        elif num == 5:
            L.append(L[j] + "j")
            L.append(L[j] + "k")
            L.append(L[j] + "l")
        elif num == 6:
            L.append(L[j] + "m")
            L.append(L[j] + "n")
            L.append(L[j] + "o")
        elif num == 7:
            L.append(L[j] + "p")
            L.append(L[j] + "q")
            L.append(L[j] + "r")
            L.append(L[j] + "s")
        elif num == 8:
            L.append(L[j] + "t")
            L.append(L[j] + "u")
            L.append(L[j] + "v")
        elif num == 9:
            L.append(L[j] + "w")
            L.append(L[j] + "x")
            L.append(L[j] + "y")
            L.append(L[j] + "z")
        elif num == 0:
            L.append(L[j] + " ")
    for j in range(t):
        L.pop(0)
    return L
def pr(L):
    """
    print list
    """
    print("[\"", " \"".join(L), " \"]", sep = "")
a = input()
l = [""]
i = 0
while i != len(a):
    k = number(a, i)
    l = tel(l, k)
    i = i + 1
pr(l)
