import math
#First statement explaining the different options
print("This is a finance calculator")
print("""
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
      """)
newVariable=1
#Store the option selected either bond or investment
calculator_Option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")


#If option equals to bond uppercase
if calculator_Option.upper() == ("BOND"):
    value=int(input("Please enter the present value of the house: "))
    rate=int(input("Please enter the Interest rate %: "))
    duration=int(input("Please enter the number of months to repay the bond: "))

    p=value
    i= (rate/100)/12
    n= duration

    repayment = (i * p)/(1-(1+i)**(-n))
    print("Your Bond repayment amount is: {}".format(repayment))

    
#Else if option is equal to investment uppercase 
elif calculator_Option.upper() ==("INVESTMENT"):
    deposit=int(input("Please enter the amount of money to deposit: "))
    rate=int(input("Please enter the interest rate %:"))
    years=int(input("Enter how many years you intent to invest: "))
    interest=input("Please enter if you would like Simple or Compound Interest: ")
    
#Calculating simple interest if entered by user
    if interest.upper() == "SIMPLE":
#converting to formula symbols fo ease of use
        r=rate/100
        p=deposit
        t=years
        a= p * (1 + r*t)
        print("Your final answer for Simple interest is {}.".format(a))

#Calculating compound interest
    elif interest.upper() == "COMPOUND":
        r=rate/100
        p=deposit
        t=years
        a=p*math.pow((1+r),t)
        print("Your final answer for Compound interest is {}.".format(a))



#otherwise error is the outcome
else:
    print("ERROR!! You must only enter one of the 2 options with no spaces or special characters")

    

