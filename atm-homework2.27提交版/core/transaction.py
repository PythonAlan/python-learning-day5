#!/usr/bin/env python3
#antuor:Alan
import datetime
from conf import settings

class ATM():
    '''
    Collection of :class:`交易操作` objects.
    '''

    def __init__(self, accountInfo):
        '''
        passed in a list of lines from a file, records user data in a dictionary.

        :param: accountInfo: Customer 's account information

        '''
        self.userData = {}
        for line in accountInfo:
            data = line.strip('\n').split()
            self.userData[data[0]] = list(data[1:])



    def verifyPassword(self, pin):
        '''
        verify if a user/pin combination is valid.  Raises InvalidPinError if the pin isn't stored in the ATM
        :param pin: Password of credit card

        '''
        if pin in self.userData:
            data = self.userData[pin]
            actualPinOwner = data[0] + " " + data[1]
            print("Hello {}, welcome back!\n".format(actualPinOwner))

        else:
            raise InvalidPinError("The pin [{}] is not contained in this ATM.".format(pin))


    def getBalance(self, pin):
        '''
        show the balance of the credit card in the ATM
        :param pin: Password of credit card
        :return:
        '''
        if pin in self.userData:
            data = self.userData[pin]
            return eval(data[2])



    def withDraw(self, pin, amount):
        '''
        withdraw a amount of money from the credit card in the ATM
        :param pin: Password of credit card
        :param amount: The amount of money need to withdraw
        :return:
        '''

        try:
            amount = eval(amount)
        except:
            raise InvalidDataError("很抱歉请输入正确的取款金额.")

        if pin in self.userData:
            data = self.userData[pin]
            interest = settings.TRANSACTION_TYPE['withdraw']['interest']*amount
            newAmount = eval(data[2]) - amount - interest
            if newAmount < 0:
                raise InsufficientFundsError("很抱歉，交易失败：余额不足！")
            else:
                data[2] = str(newAmount)
                print("\033[42;1m交易成功：取款${} 手续费${}\033[0m".format(amount,interest))


    def deposit(self, pin, amount):
        '''
        deposit a amount of money in the credit card in the ATM
        :param pin: Password of credit card
        :param amount: The amount of money need to deposit
        :return:
        '''

        try:
            amount = eval(amount)
        except:
            raise InvalidDataError("很抱歉请输入正确的存款金额.")

        if pin in self.userData:
            data = self.userData[pin]
            newAmount = eval(data[2]) + amount
            data[2] = str(newAmount)
            print("\033[42;1m交易成功：存款${}\033[0m".format(amount))

    def outPutData(self):
        '''
        out put the data of transaction
        :return:
        '''
        lineList = []

        for pin in self.userData:
            data = [pin]
            data.extend(self.userData[pin])
            constructed = " ".join(data)
            lineList.append(constructed)

        return lineList
    def transfer(self,pin,amount):
        '''
        transfer a amount of money to other payee
        :param pin: Password of credit card
        :param amount: The amount of money need to transfer
        :return:
        '''
        try:
            amount = eval(amount)
        except:
            raise InvalidDataError("很抱歉请输入正确的转账金额.")

        if pin in self.userData:
            data = self.userData[pin]
            interest = settings.TRANSACTION_TYPE['transfer']['interest']*amount
            newAmount = eval(data[2]) - amount - interest
            if newAmount < 0:
                raise InsufficientFundsError("很抱歉，交易失败：余额不足！")
            else:
                data[2] = str(newAmount)
                print("\033[42;1m交易成功：转账${} 手续费${}\033[0m".format(amount,interest))

'''可以再扩展一个转账功能'''

class InvalidDataError(Exception):
    '''
    Collection of :class:`invalid data`
    '''

    def __init__(self, message):
        super().__init__(message)


class InvalidPasswordError(Exception):
    '''
    Collection of :class:`invalid password`
    '''

    def __init__(self, message):
        super().__init__(message)

class InsufficientFundsError(Exception):
    '''
    Collection of :class:`insufficient funds`
    '''

    def __init__(self, message):
        super().__init__(message)

def printMenu():
    '''
    Go to the ATM menu
    :return:
    '''

    menu ="""
    ---------ALAN BANK ATM-------------
    请输入需要进行的操作:
    1.\t查询余额
    2.\t取款
    3.\t存款
    4.\t转账
    5.\t商城
    6.\t退出

    -----%s-----
    """% datetime.datetime.now()
    print(menu)

























