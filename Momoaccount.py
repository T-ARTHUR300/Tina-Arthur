customer = {
    "phone" : "020123456",
    "name" : "Accra boy",
    "pin" : 1234,
    "balance" : 500

}

customer1 = {
    "phone" : "024123456",
    "name" : "cutter",
    "pin" : 600,
    "balance" : 1000000

}

vendor = {
    "phone": "024111122",
    "name": "kofi",
    "pin": 1000,
    "balance": 100025
    
}

telco = {
    "code": 171

}

def deposit():
    code = eval(input("enter telco code: "))
    if code == telco['code']:
        number = input('enter phone number: ')
        if number == customer['phone']:
            amount = eval(input('enter amount to deposit: '))
            if amount >= 1:
                customer['balance'] = customer['balance'] + amount
                print('transaction successful.')
                print('amount deposited is: ', amount)
            else:
                print('enter amount more 1 cedis.')

    else:
        print('enter number again.')


def witdrawal():
    code = eval(input('enter telco code: '))
    if code == telco['code']:
        number = input('enter your number:  ')
        if number == customer['phone']:
            amount = eval(input('enter the amount to witdraw: '))
            if amount >= 1:
                pin = eval(input('enter pin to proceed: '))
                if pin == customer['pin']:
                    venNpin = eval(input('enter vendor pin: '))
                    if venNpin == vendor['pin']:
                        customer['balance'] = customer['balance'] - amount
                        print('transaction successful.')
                        print('amount witdrawed is: ', amount)
        else:
            print('enter the correct number.')
    else:
        print('is not ok')


def transfer():
    code = eval(input('enter telco code: '))
    if code == telco['code']:
        senderNumber = input("enter sender's number: ")
        if senderNumber == customer1['phone']:
            amount = eval(input("enter amount to send: "))
            if amount >= 5:
                vendPin = eval(input("enter vendor's pin: "))
                if vendPin == vendor['pin']:
                    print('transaction successful')
                    vendor['balance']= vendor['balance'] - amount
                    customer['balance'] = customer['balance'] - amount
                    customer1['balance'] = customer1['balance'] + amount
                    print('amount transferred is: ', amount)

deposit()
print('your new balance is: ', customer['balance'])
witdrawal()
print('your new balance is: ', customer['balance'])
transfer()
print('your new balance is: ', customer['balance'])

