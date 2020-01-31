#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:12:09 2020

@author: lupin
"""

country = input('請出入國籍：')
age = int(input('請輸入年齡:'))
a=['台灣','臺灣','中華民國','Taiwan']
b=['美國','USA','America']
if country in a:
    if age >= 18:
        print('已達可考駕照年齡')
    else:
        print('未達考照年齡，不可考照')
elif country in b:
   if age >= 16:
        print('已達可考駕照年齡')
   else:
        print('未達考照年齡，不可考照')
else:
    print('本程式國籍僅可輸入台灣或美國，請重新輸入')
