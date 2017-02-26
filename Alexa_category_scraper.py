"""
Alexa Category Wise Scraper
@author: agungor2
"""




from bs4 import BeautifulSoup
import pandas
from urllib.request import urlopen
b = BeautifulSoup(urlopen("http://www.alexa.com/topsites/category").read())
paragraph = b.find_all('div', {'class':'tableContainer'})
n_p=[]

#Alexa main categories

for p in paragraph:
   print(p.find_all('li'))
   n_p.append(p.find_all('li'))
at=n_p[0]
category=[]
for element in range(len(at)):
    category.append(str(at[element]).split('/')[4].split('"')[0])
    print(category)
    
#Sub Categories for each category
subcategory=[]
sitenumber=[]
for element in range(len(category)):
    kat='http://www.alexa.com/topsites/category/Top/'+str(category[element])
    b = BeautifulSoup(urlopen(kat).read())
    paragraph = b.find_all('div', {'class':'tableContainer'})
    
    n_p=[]
    for p in paragraph:
       print(p.find_all('li'))
       n_p.append(p.find_all('li'))
    at=n_p[0]
#    print(at)
    subcategory.append([])
    sitenumber.append([])
    subcategory[element].append(str(category[element]))
    sitenumber[element].append(str(category[element]))
    for e in range(len(at)):
        c=str(at[e]).split('/')[5].split('"')[0]
        subcategory[element].append(c)
        sitenumber[element].append(c+'-'+str(at[e]).split('(')[1].split(')')[0].replace(',', ''))
#        print(subcategory)
        print(sitenumber)

#Now we need to scrap top websites for each subcategory

for i in range(len(category)-1):
    for j in range(len(subcategory[i])-1):
        temp=int(sitenumber[i][j+1].split()[1])
#        Pick the subcategories that have more than 50 websites
        if temp >50:
            kat='http://www.alexa.com/topsites/category/Top/'+str(category[i])+'/'+str(subcategory[i][j+1])
            b = BeautifulSoup(urlopen(kat).read())
            paragraph = b.find_all('div', {'class':'tableContainer'})
            n_p=[]
            for p in paragraph:
    #           print(p.find_all('li'))
               n_p.append(p.find_all('li'))
            at=n_p[0]
#            print(kat)

        
        
sites=[]
#appended_data = []
#data = pandas.DataFrame([])
for i in range(len(country_code)):
    kat='http://www.alexa.com/topsites/countries/'+country_code[i]
    b = BeautifulSoup(urlopen(kat).read())
    category = b.find_all('div', {'class':'td DescriptionCell'})
    sites.append([])
    sites[i].append(category[i])
    for p in category:
       print(p.a.text)
       sites[i].append(p.a.text)
#    appended_data = pandas.concat(sites[i], names=country_list[i],axis=0,ignore_index=True)

df = pandas.DataFrame(sites)
df1 = df.transpose()
df2=df1.iloc[:50][:50]
df2.to_csv('topsites.csv', sep=',')