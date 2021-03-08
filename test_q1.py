def pi():
    pi = 0   #sets pi 0
    n = 4
    d = 1
    x = input("enter terms to use")   #lets user set terms (1000000 is close)
    x = int(x)   #user input to int for use
    for i in range (1,x):    #range starts at 1 increments to input
        a = 2 * (i % 2) - 1  #equation to actually create the pi number
        pi += a * n / d
        d += 2
    print(pi)   #prints calculated pi
    
pi()