#!/usr/bin/env python3
#antuor:Alan
import datetime

TRANSACTION_TYPE = {                           #交易类型
    'repay':{'interest':0},   #还款 0利息，可以改
    'withdraw':{'interest':0.03},
    'transfer':{'interest':0.01},
    'consume':{'interest':0},

}

