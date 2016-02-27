#!/usr/bin/env python3
#antuor:Alan

name = input("请输入你的名称来查询订单:")
with open("orders.txt") as f:
    for line in f:
        if name in line:
            print(line)