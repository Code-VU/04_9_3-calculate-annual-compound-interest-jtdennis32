def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundInterest()
    def calculateCompoundInterest():
        print("Compound Interest:", calculate_compound_interest())
        print("---")

        print("Compound Interest:", calculate_compound_interest())
        print("---")

        print("Compound Interest:", calculate_compound_interest())
    

    def calculate_compound_interest():
        client_one_principal = float(input("Principle (amount): "))
        client_one_time = float(input("Time:               "))
        client_one_rate = float(input("Rate:               "))

        amnt = client_one_principal*(1+client_one_rate/100)**client_one_time
        compoundinterest = amnt - client_one_principal

        return(round(compoundinterest,2))
    
    calculateCompoundInterest()
    
   
        


 #print("Compound Interest: "+str(intrest))

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
