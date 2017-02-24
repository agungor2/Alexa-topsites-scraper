# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:11:48 2017

@author: agungor2
"""
from bs4 import BeautifulSoup
import pandas
from urllib.request import urlopen
b = BeautifulSoup(urlopen("http://www.alexa.com/topsites/countries").read())
paragraphs = b.find_all('div', {'class':'tableContainer'})
n_p=[]

for p in paragraphs:
   print(p.find_all('li'))
   n_p.append(p.find_all('li'))
at=n_p[0]
country_list=[]
country_code=[]
for element in range(len(at)):
    country_code.append(str(str(at[element]).split('/')[3]).split('"')[0])
#    print(country_code)
    country_list.append(str(at[element]).split('/')[3].split('"')[1].split('<')[0].split('>')[1])
#    print(country_list)
sites=[]
#appended_data = []
#data = pandas.DataFrame([])
for i in range(len(country_code)):
    kat='http://www.alexa.com/topsites/countries/'+country_code[i]
    b = BeautifulSoup(urlopen(kat).read())
    paragraphs = b.find_all('div', {'class':'td DescriptionCell'})
    sites.append([])
    sites[i].append(country_list[i])
    for p in paragraphs:
       print(p.a.text)
       sites[i].append(p.a.text)
#    appended_data = pandas.concat(sites[i], names=country_list[i],axis=0,ignore_index=True)

df = pandas.DataFrame(sites)
df1 = df.transpose()
df2=df1.iloc[:50][:50]
df2.to_csv('topsites.csv', sep=',')