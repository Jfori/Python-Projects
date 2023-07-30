import time

A = time.time()
local = time.ctime(1650119429)

#6th april - 1649255429
#16th april - 1650119429

##print(local)



hour = local[11]+local[12]
minute = local[14] + local[15]
second = local[17]+local[18]

hour = int(hour)
minute = int(minute)
second = int(second)

totalSeconds = hour * 3600 + minute * 60 + second

newHrs = totalSeconds // 3600
newMins = (totalSeconds % 3600) // 60
newSecs = (totalSeconds % 3600) % 60

##print(hour, minute, second)
##print(totalSeconds)
##print(newHrs)
##print(newMins)
##print(newSecs)

def Testing():
    a = ['1','2', '3']
    l = 2
    e = a[l-1]
    f = 9
    g = 10
    b = f + g
    return e, b

def Testing2():
    c, d = Testing()
    print(c)
    print(d)

Testing2()
