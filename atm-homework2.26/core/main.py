#!/usr/bin/env python3
#antuor:Alan

import os,sys
from core import transaction

def run():
    while True:
        try:
            accountFileInput = input("请输入你的用户文件名：")
            infile = open(accountFileInput)
            lines = infile.readlines()
            infile.close()
            break
        except:
            print("很抱歉ATM程序不能识别你的用户文件信息{},请重新输入!".format(accountFileInput))
    atm = transaction.ATM(lines)
    while True:
        try:
            password = input("请输入信用卡密码：")
            atm.verifyPassword(password)
            break
        except transaction.InvalidPasswordError:
            print("密码输入有误，重新输入!")
            continue
    transaction.printMenu()
    selection = eval(input("请选择需要进行的操作：").strip())
    while selection != 5:
        if selection == 1:
            print("\033[31;1m您卡上的余额：${}\033[0m\n".format(atm.getBalance(password)))
            transaction.printMenu()
            selection = eval(input("请选择需要进行的操作："))
        elif selection == 2:
            while True:
                try:
                    funds = input("请输入取款金额：")
                    atm.withDraw(password,funds)
                    transaction.printMenu()
                    selection = eval(input("请选择需要进行的操作："))
                    break
                except transaction.InvalidDataError:
                    print("请输入正确的取款金额！")
                    continue
                except transaction.InsufficientFundsError:
                    print("很抱歉取款金额大于信用额度，请重新输入取款金额！")
                    continue

        elif selection == 3:
            while True:
                try:
                    funds = input("请输入存款金额：")
                    atm.deposit(password,funds)
                    transaction.printMenu()
                    selection = eval(input("请选择需要进行的操作："))
                    break
                except transaction.InvalidDataError:
                    print("请输入正确的取款金额！")
                    continue
        elif selection ==4:
            while True:
                try:
                    funds = input("请输入转账金额：")
                    atm.transfer(password,funds)
                    transaction.printMenu()
                    selection = eval(input("请选择需要进行的操作："))
                    break
                except transaction.InvalidDataError:
                    print("请输入正确的转账金额！")
                    continue
    print("感谢使用ATM,欢迎下次光临！")
    updatedData = atm.outPutData()
    with open('accountsUpdated.txt','w') as outFile:
        for line in updatedData:
            outFile.write(line + '\n')
    os.rename('accounts.txt','accountsbackup.txt')
    os.rename('accountsUpdated.txt','accounts.txt')






























