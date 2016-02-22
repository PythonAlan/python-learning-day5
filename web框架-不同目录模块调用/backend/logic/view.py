#!/usr/bin/env python3
#antuor:Alan
from backend.db.sql_api import select
def home():
    print("Welcome to youtube.com")
    q_data = select('user','eee')
    print("query res:",q_data)
def movie():
    print("It 's movie pages")



