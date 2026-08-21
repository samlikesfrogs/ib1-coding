#2
# a = int(input("give me an integer: "))
#b = int(input("another: "))
#if a == b:
#    output = a**2 + b**2
#else:
#    output = a + b
#print(output)

#3
#x=7
#for i in range(10,38):
#    if i == x + 3:
#        print(i, end=" ")
#        x+=3

#y=1000
#for i in range(50):
#    y-=2
#    print(y, end=" ")

#for i in range(1, 21):
#    if i%2==0:
#        i=-1
#    else:
#        i=1 
#    print(i, end=" ")

#for i in range(1, 61):
#    if i%3==0:
#        i=9
#    else:
#        i=7
#    print(i, end=" ")

#4
#total = int(input("card total: "))
#if total < 17:
#    action = "hit"
#elif total >= 17 and total <= 21:
#    action = "stay"
#else:
#    action = "bust"
#print(action)

#5
#a=int(input("int: "))
#b=int(input("int: "))
#x = 0

#if a >= 100 and b <= 50:
#    x=1
#print(x)

#if (a >= 100 or b >= 100) and (b<= 50 or a <= 50):
#    x =1
#print(x)

#6
#w=int(input("give weight: "))
#p=3

#if w>2 and w <=5:
#    for i in range(w-2):
#        p+=2
#elif w>5:
#    for i in range(w-2):
#            p+=3
#print(p)

#7
#n=1
#while not (n**3-16)%47 == 0:
#    n+=1
#print(n)

#8
#a = int(input("nonnegative int pls: "))
#x=1
#for i in range(a):
#    x*=3
#print(x)

#9
#previous = 0
#current = 0
#t = 0
#biggest = 0
#while t <= 100:
#    current = t*(t-20)*(t-100)+120000
#    if previous-current > biggest:
#        biggest = (previous-current)
#        time = t
#    previous = current
#    t+=1
#print(time)


