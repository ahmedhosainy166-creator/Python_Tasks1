# task3
print("-------Welcom to ATM--------")

correct_pin = 1234
balance = 5000
entered_pin = int(input("Enter your password :"))

if entered_pin == correct_pin :
    Select_Transaction = input("(Withdraw/Check Balance):")
   
    if Select_Transaction == "Check Balance":
        print(f"Available Balance : {balance}")
    
    if Select_Transaction == "Withdraw":
       Enter_Amount = int(input("Please enter the amount :"))
   
       if Enter_Amount > balance :
            print("Sorry, insufficient balance")
   
       else:
             remaining = balance - Enter_Amount
             print(f"Transaction successful. Your remaining balance is: {remaining}")    

else :
    print("Wrong PIN, transaction denied")

