#1
#if ((sun:=input("is the sun shining? ") == "yes") and (time:=int(input("what is the current time? "))) >= 10 or time <= 16):
#    x="pls use sunscreen"
#else:
#    x="you're good"
#print(x)

#2
#a = str(input("give pos int: "))
#b = str(input("give pos int: "))
#if a[-1] == b[-1]:
#    x = True
#else:
#    x = False
#print(x)

#3
#n=0
#s=int(input("give pos int: "))
#while ((n**3) - (10*(n**2))) <= s:
#    n+=1
#print(f'the smallest value that makes the expression true is {n}. the expression equals {((n**3) - (10*(n**2)))}')

#4
#a=int(input("pos int 1: "))
#b = int(input("pos int 2: "))
#x=1
#while not (x%a == 0 and x%b == 0):
#    x+=1
#print(f'smallest pos int divisible by both is {x}')

#6
#potentialPrime = int(input("give pos int: "))
#x=1
#factors=0
#for i in range(potentialPrime):
#    if potentialPrime%x==0:
#        factors +=1
#    x+=1
#if factors != 2:
#    prime = False
#else:
#    prime = True
#print(prime)
    
#7
#if (a and b) or (not a and b)

#8
#numOfPrimes = 0
#potentialPrime=1
#primeList = []

#while potentialPrime < 100:
#    x=1
#   factors = 0
#    potentialPrime +=1
#    for i in range(1, potentialPrime):
#        if potentialPrime%x==0:
#            factors +=1
#        x+=1
#    if factors == 2:
#        primeList.append(potentialPrime)
#print(primeList)

#while numOfPrimes != 100:
#    x=1
#    factors = 0
#    potentialPrime +=1
#    for i in range(1, potentialPrime):
#        if potentialPrime%x==0:
#            factors +=1
#        x+=1
#    if factors == 2:
#        primeList.append(potentialPrime)
#        numOfPrimes+=1
#print(primeList)

#9
#potentialPerfect = 1
#perfectList = []
#while potentialPerfect < 10000:
#    total = sum([i for i in range(1, potentialPerfect) if potentialPerfect%i==0])
#    if total==potentialPerfect:
#        perfectList.append(potentialPerfect)
#    potentialPerfect+=1
#print(perfectList)

#10 
#1 what
#2 huh
# math sl frfr
