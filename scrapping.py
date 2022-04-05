import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
Title,Price,Rating,Features=[],[],[],[]
for i in range(1,43):
    url=('https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}'.format(i))
    page=requests.get(url)
    html_code=page.text
    soup=BeautifulSoup(html_code,"html.parser")
    for x in soup.find_all('div',attrs={'class':'_2kHMtA'}):
        product=x.find('div',attrs={'class':'_4rR01T'})
        if product is None:
            Title.append(np.NaN)
        else:
            Title.append(product.text)
        mrp=x.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
        if mrp is None:
            Price.append(np.NaN)
        else:
            Price.append(mrp.text)
        rate=x.find('div',attrs={'class':'_3LWZlK'})
        if rate is None:
            Rating.append(np.NaN)
        else:
            Rating.append(rate.text)
        components=x.find('ul',attrs={'class':'_1xgFaf'})
        if components is None:
            Features.append(np.NaN)
        else:
            Features.append(components.text)
dict={'Title':Title,'Price':Price,'Rating':Rating,'Features':Features}
df=pd.DataFrame(dict)
excel=df.to_excel('laptop_sales.xlsx',index=False)
print(df.shape)