
WantedDamageReduction = 28
#Ive done it, Ive completed the generic EHP calculator.
for x in range(100):
    x = x + 1#Convert 0 to 1
    x = x*321.4#just get some bigger numbers, it used to be 500 but I decided to use some random number because you might argue this only works for multiples of 100
    EHP = x#Duplucate the variable
    EHP_Calc = 0#Set a variable to 0 so I can use it in this while Loop
    while EHP_Calc < x:#Keep on looping, until EHP is greater than x
        EHP = EHP + 0.0001#continuously increase x by a really small number
        EHP_Calc = EHP * ((100-WantedDamageReduction)/100)#Calculate damage reduction

    Percent_of_each_other = (EHP/x)*100#Calculate what percentage EHP is of x
    print("HP: " + str(x)  + " EHP: " + str(EHP) + " %" + str(Percent_of_each_other))#print
    
    EHP2 = x * ((10000/(100-WantedDamageReduction))/100)#Use the formula I created
    Percent_of_each_other2 = (EHP2/x)*100#Calculate what percentage EHP2 is of x
    print("HP: " + str(x) + " EHP: " + str(EHP2) + " %" + str(Percent_of_each_other2))#print

    EHP3 = (100*x)/(100-WantedDamageReduction)#I went ahead and simplified it in Symbolab for you so its easier to read
    Percent_of_each_other3 = (EHP3/x)*100#Calculate what percentage EHP2 is of x
    print("HP: " + str(x) + " EHP: " + str(EHP3) + " %" + str(Percent_of_each_other3))#print
