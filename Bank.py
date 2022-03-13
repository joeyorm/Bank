# Joey Ortega Mandia INSO CIIC3015 BANK ACCOUNT
User = str.title(input('What is your name? '))
number = 1
totaldeposit =0
totalwithdraw=0
totalfailwithdraw=0
totalfaildeposit=0
totaldepositamount=0
totalamountwith=0
totalfee= 0
totalfeeamount=0
totalfailwithdrawamount=0 
fee = 5

# This is what i used to mitigate round off error i searched for it in stackoverflow
def rounder(n):
    return int(n * 100) / 100

print('\nHey there ' + User + ", let's setup your bank account.")
Account = input('Enter your account name here: ')


# Here i made it so the user can"t have their name as their account name.
while str.lower(User) == str.lower(Account):
    print("\nSorry for the inconvenience, you can't enter YOUR username in your ACCOUNT name.")
    
    Account = input('Enter your account name here: ')
    print('')

Balance = input('What is your starting Balance?: ')
while Balance == str(Balance):
    try:
        Balance = float(Balance)
        if float(Balance) < 0:
            while float(Balance) < 0:
                print('')
                print("Sorry for the inconvenience, your starting Balance cant be negative. Please try again.")
                Balance = input('What is your starting Balance?: ')
                print('')
    except ValueError:
        print("Sorry for the inconvenience, that value can't be accepted. Please try again")
        Balance = input('What is your starting Balance?: ')
    if float(Balance) < 0:
        while float(Balance) < 0:
            print('')
            print("Sorry for the inconvenience, your starting Balance cant be negative. Please try again.")
            Balance = input('What is your starting Balance?: ')
            print('')

while number < 3 or number != 3:
    for i in ['Account: ' + str.upper(Account), 'Balance: $' + str(Balance), 'Here are your options ' + User + ':',
              '1) Deposit', '2) Withdraw', '3) Quit']:
        print(i)
    number = str.lower(input('What would you like to do?: '))
    if number == '1' or number == 'd' or number == 'deposit' or number == 1:
        number = 1
        Deposited = input('How much do you want to deposit?: ')
        while Deposited == str(Deposited):
            try:
                Deposited = float(Deposited)
                if Deposited < 0:
                    print("Sorry for the inconveniece, you can't deposit a negative number, try again.")
                    totalfaildeposit += 1
                    Deposited = input('How much do you want to deposit?: ')
            except ValueError:
                print("Sorry for the inconvenience, that value can't be accepted.")
                totalfaildeposit += 1
                Deposited = input('How much do you want to deposit?: ')
        if Deposited >= 0:
            Balance = rounder(Balance + Deposited)
            totaldepositamount = totaldepositamount + Deposited
            totaldeposit += 1
            for i in ['You have successfully deposited $' + str(rounder(Deposited)) + ' into your bank account.',
                      'You have deposited ' + str(totaldeposit) + ' times.', ""]:
                print(i)
    elif number == '2' or number == 'withdraw' or number == 'w' or number == 2:
        number = 2
        Withdrawed = input('How much do you want to withdraw?: ')
        while Withdrawed == str(Withdrawed):
            try:
                Withdrawed = float(Withdrawed)
            except ValueError:
                print('Sorry for the inconvenience, such value cant be accepted.')
                Withdrawed = input('How much do you want to withdraw?: ')
        Balance = rounder(Balance - abs(Withdrawed))
        if Balance >= 0:
            totalwithdraw += 1
            for i in ["", "You've successfully withdrawed $" + str(rounder(Withdrawed)) + ' from your bank account,'
                      ' ' + str.title(Account),
                      " You have withdrawn " + str(totalwithdraw) + " times.", '']:
                print(i)
                totalamountwith += (abs(Withdrawed)) / 2
        elif Balance < 0:
            for i in ["Sorry for the inconvenience, you can't withdraw more than what you currently have, ",
                      "Because of this you've been charged with a 5 dollar fee. Please try again. ", '']:
                print(i)
            totalfailwithdraw += 1
            totalfailwithdrawamount += abs(Withdrawed)
            totalfee += 1
            totalfeeamount += fee
            Balance = rounder(Balance + abs(Withdrawed))
            Balance = rounder(Balance - fee)
            if Balance < 0:
                print('Please deposit into your bank account to cover your debt.')
    elif number == '3' or number == 'quit' or number == 'q' or number == 3:
        # here i made a lot of statements, containing the information of the bank account
        for i in ['', "Here is your bank statement " + User + ".", "", "You've made " + str(totaldeposit) +
                                                                       " deposits totaling: $" + str(
            rounder(totaldepositamount)) + '', "You've made "
                                               + str(totalfaildeposit) + " failed deposits.",
                  "You've made " + str(totalwithdraw) +
                  " withdraws totaling: $" + str(rounder(totalamountwith)), "You've made " + str(totalfailwithdraw) +
                                                                            " failed withdraws totaling: $" + str(
                rounder(totalfailwithdrawamount)),
                  "You've been charged with " + str(rounder(totalfee)) + " fees, totaling: $" +
                  str(rounder(totalfeeamount)), "Your balance: $" + str(Balance), "Have a good day " +
                                                                                  str(User) + '!']:
            print(i)
        number = 3
    # if any problem occurs this else statement should take care of it by repeating the loop and saying 'error'
    else:
        for i in ["Sorry for the inconvenience, that option doesn't exist. Please try again.", '']:
            print(i)
            number = 0



