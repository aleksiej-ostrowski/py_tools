a = [1000,2,2,2,2,2,2,2,7,7,7,7,2,2,2,2,2,2,2,3,4,5,6,2,5,-100000,7,7,7,7,7,7,7,7,7,7,7,7,7,7]

from bisect import insort_left

def schoorygin(a):
    a.sort()
    while 1:
        l = len(a)
        if l <= 2:
            return sum(a) / l
        b = (a[0] + a[-1]) * 0.5
        if (b <= a[1]):
            del a[0]
            continue
        if (b >= a[-2]):
            del a[-1] 
            continue
        del a[0]
        del a[-1]
        insort_left(a, b)

print a
print sum(a) / len(a)
print schoorygin(a)
