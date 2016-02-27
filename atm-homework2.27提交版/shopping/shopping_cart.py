#!/usr/bin/env python3
#antuor:Alan

import datetime

products = {
    1:["iphone 6s",5400,100],
    2:["macbook pro",15000,100],
    3:["Hat",20,100],
    4:["T-shirt",45,100],
    5:["Trouser",50,100],
    6:["Mouse",28,100],
    7:["Keyboad",25,100],
}

def timeStamped(fmt = ' Date %Y-%m-%d '):
    '''
    time of order
    :param fmt: time format
    :return:
    '''
    return datetime.datetime.now().strftime(fmt)


class Item(object):
    '''
    Collection of :class:`products` objects.
    '''
    def __init__(self,unq_id,name,price,qty):
        '''
        初始化变量
        :param unq_id: ID of item
        :param name: Product name
        :param price: Price of product
        :param qty: Quantity of product
        :return:
        '''
        self.unq_id = unq_id
        self.name = name
        self.price = price
        self.qty = qty
class Cart(object):
    '''
    Collection of : class:'shopping' objects.
    '''
    def __init__(self):
        '''
        初始化商品列表
        :return:
        '''
        self.content =dict()
    def update(self,item):
        '''
        update item list
        :param item: Products
        :return:
        '''
        if item.unq_id not in self.content:
            self.content.update({item.unq_id:item}) #good
            return
    def get_total(self):
        '''
        calculate the money
        :return:
        '''
        return sum([v.price * v.qty for i , v in self.content.items()])
    def get_num_items(self):
        '''
        calculate the quantity of purchasing
        :return:
        '''
        return sum([v.qty for i ,v in self.content.items()])
    def remove_item(self,key):
        '''
        cancel items
        :param key: Index of product
        :return:
        '''
        self.content.pop(key)
    def show_menu(self):
        '''
        show the shopping menu
        :return:
        '''
        menu = """
        ****信用卡商城****
        1."商品展示"
        2."开始购买"
        3."生成订单"
        4."购物车结算"
        """
        print(menu)
        return int(input("请输入选择:"))



def run_shopping():
    '''
    deal all shopping operation
    :return:
    '''
    cart = Cart()
    running =True

    while running:
        selection = cart.show_menu()
        if selection == 1:
            print("{:<8} {:<15} {:<10} {:<10}".format("ID","Product","Price","Qty"))
            for k,v in products.items():
                label,num,qty=v
                print("{:<8} {:<15} {:<10} {:<10}".format(k,label,num,qty))
        elif selection == 2:
            chose = input("请输入商品编号:")
            qty = input("请输入购买数量:")

            for k,v in products.items():
                if k==int(chose):
                    name,price,qty = v
                    item = Item(chose,name,price,qty)
                    cart.update(item)
        elif selection ==3:
            if cart.get_num_items()==0:
                print("请输入购买数量!")
                continue

            cust_name = input("请输入你的名称:")
            cust_address = input("请输入你的收货地址:")
            cust_mob = input("请输入你的联系方式:")
            with open("orders.txt","a") as myfile:
                t = timeStamped()
                total=str(cart.get_total())
                myfile.write("\n")
                myfile.write("%s"%cust_name)
                myfile.write("%s"%cust_address)
                myfile.write("%s"%cust_mob)
                myfile.write("    %s"%total)
                myfile.write(t)
                print("************* Bill **************")
                print("{0}   {1}   {2}".format(cust_name,cust_address,cust_mob))
                print("{:<8} {:<15} {:<10} {:<10}".format("ID","Product","Price","Qty"))
                for k,v in cart.content.items():
                    print("{:<8} {:<15} {:<10} {:<10}".format(k,v.product_name,v.price,v.qty))
                print("Total :%s " % cart.get_total())

                break

        else :
            if cart.get_num_items()==0:
                print("你的购物车里还没有商品!")
                continue
            else:
                print("你有 %d 件商品在你的购物车，总金额为：$ %d" %(cart.get_num_items(),cart.get_total()))
                print("{:<8} {:<15} {:<10} {:<10}".format("ID","Product","Price","Qty"))
                for k,v in cart.content.items():
                    print("{:<8} {:<15} {:<10} {:<10}".format(k,v.product_name,v.price,v.qty))






















