#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:54:27 2019

@author: manzars
"""

import requests
import pandas
from selenium import webdriver
from bs4 import BeautifulSoup
req = webdriver.FirefoxProfile()
req.set_preference("javascript.enabled", True)
driver = webdriver.Firefox(req)
base = 'http://shta.sg/index.php/en/membership-4/members-directory?start='
file = open('assignment.csv', 'w')
header = 'Compay name, email, Telephone, Address\n'
file.write(header)
for i in range(13):
    driver.get(base + str(i))
    html = driver.execute_script('return document.documentElement.outerHTML')
    soup = BeautifulSoup(html, 'lxml')
    div = soup.findAll('div', {'class': 'icon-box'})
    for element in div:
        email, telephone, name, address = 'NaN', 'NaN', 'NaN', 'NaN'
        try:
            email = element.a.text
            #print(email)
        except:
            email = 'NaN'
            #print(email)
            
        name = element.h3.text
        #print(name)
        
        try:
            telephone = element.text.split('Fax')[0].split('Tel:')[1]
            if(len(telephone) == 0):
                telephone = 'NaN'
            #print(telephone)
        except:
            telephone = 'NaN'
            #print(telephone)
        try:
            address = element.text.split('Tel')[0].split(name)[-1]
            if(len(address) == 0):
                address = element.text.split('\n\n')[-2].replace('\n', '')
            #print(address)
        except:
            address = 'NaN'
            #print(address)
        print(name.replace('\n', ''), email.replace('\n', ''), address.replace('\n', ''), telephone.replace('\n', ''))
        file.write(name.replace('\n', '').replace(', ', '') + ',' + email.replace('\n', '').replace(',', '') + ',' + telephone.replace('\n', '').replace(',', '') + ',' + address.replace('\n', '').replace(',', '') + '\n')
        
        
file.close()
f = pandas.read_csv('assignment.csv')