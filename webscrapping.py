import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
url='https://www.hubertiming.com/results/2019MH50'
#url='http://phn.net'
html=urlopen(url)
soup=BeautifulSoup(html,'lxml')
#type soup
#get the title
title=soup.title
print(title)
#print out text
text=soup.get_text()
print(text)
#print(text)
#hyper link=a
soup.find_all('a')
#href=Short for hypertext reference, HREF is an HTML attribute that is used either to link to another web page,
#or a different portion of the same page.
all_link =soup.find_all('a')
for link in all_link:
    print(link.get('href'))
    #print first 10 row for sunity check= tr
rows=soup.find_all('tr')
print(rows[:10])
#remove those who are not useful,data store in row_td
for row in rows:
    row_td=row.find_all('td')
    print(row_td)
#type(row_td)
for row in rows:
    row_td=row.find_all('td')
    print(row_td)
#type(row_td)
str_cell=str(row_td)
cleantext=BeautifulSoup(str_cell,'html5lib').get_text()
print(cleantext)
import re
list_rows=[]
for row in rows:
    cells=row.find_all('td')
    str_cells=str(cells)
    clean=re.compile('.?<\/w*>')
    clean2=(re.sub(clean,'',str_cells))
    print(clean2)
    list_rows.append(clean2)
#print(clean2)
print(list_rows)
#type(clean)
df=pd.DataFrame(list_rows)
df.head(20)
#data munipation and cleang
df1=df[0].str.split(',',expand=True)
df1.head(10)
df1[0]=df1[0].str.strip('[')
df1[0]=df1[0].str.strip(']')
df1[1]=df1[1].str.strip('[')
df1[13]=df1[13].str.strip(']')
df1.head(20)
col_labels=soup.find_all('th')
col_labels
all_header=[]
col_str=str(col_labels)
cleantext2=BeautifulSoup(col_str,'lxml').get_text()
all_header.append(cleantext2)
print(all_header)
df2=pd.DataFrame(all_header)
df2
df3=df2[0].str.split(',',expand=True)
df3.head()
frames=[df3,df1]
df4=pd.concat(frames)
df4.head()
df5=df4.rename(columns=df4.iloc[0])
df.head()
df6=df5.dropna(axis=0)
df7=df6.drop(df6.index[0])
df7.head(20)
df7.rename(columns={'[Place': 'Place'},inplace=True)
df7.rename(columns={' Team]': 'Team'},inplace=True)
#df7.drop([0])
df7.reset_index(drop=True)#for making data line
