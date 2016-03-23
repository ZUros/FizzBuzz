i = int(raw_input("Vnesi stevilo do katerega naj steje med 1 in 100: "))
#prvi del programa
while 1>i>100:
    if i<1:
        print ("Vpisi vecje stevilo.")
    if i > 100:
        print ("Vpisi manjse stevilo")
#drugi del programa
else:
    for x in xrange(1,i+1):
        if x%3!=0 and x%5!=0:
            print x
        if (x%3 == 0 and x%5 == 0):
            print ("FizzBuzz")
        elif x%3 == 0:
            print ("Fizz")
        elif x%5 == 0:
            print ("Buzz")


