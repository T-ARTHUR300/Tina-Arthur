
class atm:
    balance = 1000

    def __init__(self, pin):
        self.pin = pin
        
    
    
    def deposit(self):
        amount = eval(input('enter amount to deposit: '))
        self.balance = self.balance + amount
        print('your deposited amount is ', amount, '\n Your new balance is ', d1.balance)
        print('Transaction successful.')
    
    def atmPin(self):
        pin = input('enter pin to proceed: ')
        if len(pin) == 5:
            return
        else:
            print('enter correct number')

    def getBalance(self):
        self.balance = self.balance
        select = eval(input('select account. \n1: Savings \n2: current \nEnter: '))
        if select == 1:
            print(self.balance)
        elif select == 2:
            print(d1.balance)
        else:
            print('service not available')

    def transfer(self):
        amount = eval(input('enter amount to transfer: '))
        self.balance = self.balance - amount
        d1.balance = d1.balance + amount
        print(' verify amount to transfer:', amount)
        input("Press enter to Proceed.")
        print('transaction successful')
            

    def withdrawal(self):
        amount = eval(input('enter amount to withdraw: '))
        self.balance = self.balance - amount
        print(' verify amount to withdraw:', amount)
        input("Press enter to Proceed.")
        print('transaction successful')
            

    def atmProcess(self):
        print('Welcome to Python Bank \nATM Services.')
        print('tips for the day \ndo not disclose your pin to anyone to avoid theft.')
        d1.atmPin()
        choice = eval(input('Choose Service \n1: Deposit \n2: Withdrawal \n3: Check balance \n4: Transfer \nEnter:  '))
        if choice == 1:
            d1.deposit()
        elif choice == 2:
            d1.withdrawal()
        elif choice == 3:
            d1.getBalance()
        elif choice == 4:
            d1.transfer()

        else:
            print('you have entered a wrong number.')

        






class elecBill:
    #unitPrice = 0.7979
    vat = 0.1250
    natElecL = 0.0200
    striL = 0.0300
    nhilGet = 0.0500
    serCharg = 0.4075
    montBill = {}

    def __init__(self, unitPrice):
        self.unitPrice = 0.7979

    def meterRead(self):
        #self.prev = prev
        #self.cur = cur
        #prev = eval(input('Enter previous meter readings: '))
        #cur = eval(input('Enter current meter readings: '))
        if cur > prev:
            metread = cur - prev
            print(metread, 'kWh')

        else:
            return

    def monthBill(self):
        self.montBill = round((metread * self.unitPrice),3)
        #return monthBill 
        print('Bill is: ', self.montBill)

    def vatR(self):
        vaR = ((cur - prev) * self.unitPrice)
        self.va = round((self.vat * ((32*self.serCharg) + vaR)),2)
        print('Vat on bill: ', self.va)
    def natElecLe(self):
        nat = ((cur - prev) * self.unitPrice)
        self.natElec = round((self.natElecL * nat),2)
        print('National Electr. Levy: ', self.natElec)
    def striLi(self):
        light = ((cur - prev) * self.unitPrice)
        self.striLii = round((self.striL * light),2)
        print('street Light: ', self.striLii)
    def nhilGetF(self):
        get = ((cur - prev) * self.unitPrice)
        self.nhilGe = round((self.nhilGet * ((32*self.serCharg) + get)),2)
        print('NHIS and GETFUND Levy: ', self.nhilGe)
    def servChar(self):
        servCha = round((32 * self.serCharg),2)
        print('Service charges for 32days: ', servCha)
    def totalThisMonth(self):
        #current = ((cur -prev ) * self.unitPrice)
        #totalThisMont = round(((current) + (current * self.serCharg) + (current * self.nhilGet) + 
                        #(current * self.striL) + (current * self.natElecL) + (current * self.vat)),2)
        totalThisMont = round(((self.montBill) + (32 * self.serCharg) + ((self.montBill + (32 * self.serCharg)) * self.nhilGet) + (self.montBill * self.striL) + 
                                (self.montBill * self.natElecL) + (((self.montBill + (32 * self.serCharg)) * self.vat))),3)
        print('Total current bill: ', totalThisMont)


    
    def elecCal(self):
        choice = eval(input('choose 1: monthly calcuation \n2: other services \nEnter: '))
        if choice == 1:
            d.meterRead()
            d.monthBill()
            d.vatR()
            d.natElecLe()
            d.striLi()
            d.nhilGetF()
            d.servChar()
            d.totalThisMonth()
        elif choice == 2:
            choose = eval(input('1: NHIS and GETFUND \n2: Service charges \n3: Value Added Tax(VAT) \n4: Meter Readings \n5: Stright Light \n6: National Electrification Levy \n7: This Month Bill \n Enter: '))
            if choose ==1:
                d.nhilGetF()
            elif choose ==2:
                d.servChar()
            elif choose ==3:
                d.vatR()
            elif choose == 4:
                d.meterRead()
            elif choose == 5:
                d.striLi()
            elif choose == 6:
                d.natElecLe()
            else:
                print('Wrong selection.')
                    
            
            
            
        else:
            print('start again.')

#print('Electricity bill calculation.')
#prev = eval(input('Enter previous meter readings: '))
#cur = eval(input('Enter current meter readings: '))
#metread = cur - prev
#d = elecBill(0.7979)

#d.elecCal()

d1 = atm(1234)
d2 = atm(5678)


d1.atmProcess()

