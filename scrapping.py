Importing
Libraries
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = 'https://www.commonfloor.com/hyderabad-property/for-sale'
page = requests.get(URL)
page.status_code
htmlcode = page.text
htmlcode
soup = BeautifulSoup(htmlcode)
print(soup.prettify())
for i in range(1, 10):
    print('https://www.commonfloor.com/hyderabad-property/for-sale?page={}'.format(i))
Extractiing
from website
% % time
price = []
agents = []
features_1 = []

post_time = []

title = []

for i in range(1, 31):
    URL = 'https://www.commonfloor.com/hyderabad-property/for-sale?page={}'.format(i)

    page = requests.get(URL)
    htmlCode = page.text

    soup = BeautifulSoup(htmlCode)

    for x in soup.find_all('div', attrs={'class': 'snb-tile new-booking impressionAd'}):

        post_date = x.find('div', attrs={'class': 'posteddate'})
        if post_date is None:
            post_time.append(np.NaN)
        else:
            post_time.append(post_date.text)
        ###################################################################################

        prices = x.find('span', attrs={'class': 's_p'})
        if prices is None:
            price.append(np.NaN)
        else:
            price.append(prices.text)
        ##################################################################################

        title_name = x.find('div', attrs={'class': 'st_title'})
        if title_name is None:
            title.append(np.NaN)
        else:
            title.append(title_name.text)

        ################################################################################

        agent = x.find('div', attrs={'class': 'infownertext'})
        if agent is None:
            agents.append(np.NaN)
        else:
            agents.append(agent.text)
        ##############################################################################

        features = x.find('a', attrs={'class': 'snblink clearfix'})
        if features is None:
            features_1.append(np.NaN)
        else:
            features_1.append(features.text)

Data
Frame
df = pd.DataFrame(
    {'title': title, 'prices': price, 'features': features_1, "booking_start": post_time, 'organizing': agents})
df.head()
df.shape
df.info()
# df.to_csv("commonfloor.csv", index=False)

import pandas as pd
import numpy as np
import re

df = pd.read_csv("commonfloor.csv")
df.head(8)
title
prices
features
booking_start
organizing
0    \n3BHK
Apartment
for Sale in Kondapur\nIncor V...\n 1.41 Cr    \n\n\nCarpet Area\n\n 1850 sq.ft...Posted: 25
days
ago    \nAgent: \nRamana\n
1    \n4BHK
Apartment
for Sale in Shaikpet\nSalarpu...\n 3.04 Cr    \n\n\nCarpet Area\n\n 2224 sq.ft...Posted: 20
days
ago    \nBuilder: \nSalarpuria
Sattva
Group\n
2    \n
3
BHK
Apartment
for Sale in Jeedimetla\nEss...\n 74.02 L    \n\n\nCarpet Area\n\n 1260 sq.ft...Posted: 26
days
ago    \nAgent: \nHyderabad
Marketing
Team\n
3    \nNot
Furnished
2
BHK
Apartment
for Sale in Po...    \n 52.57 L    \n\n\nCarpet Area\n\n 914 sq.ft (...Posted: 18
days
ago    \nAgent: \nHyderabad
Marketing
Team\n
4    \nSemi
Furnished
2
BHK
Apartment
for Sale in Pa...    \n 30 L    \n\n\nCarpet Area\n\n 1200 sq.ft...Posted: Today    \nAgent: \nMarisetti
Saidaiah\n
5    \n2BHK
Villa
for Sale in Indresham\nIndresham\...\n 52 L    \n\n\nCarpet Area\n\n 800 sq.ft (...Posted: Today    \nAgent: \nShiv
Shankar\n
6    \n2BHK
Villa
for Sale in Indresham\nIndresham\...\n 52 L    \n\n\nCarpet Area\n\n 800 sq.ft (...Posted: Today    \nAgent: \nShiv
Shankar\n
7    \n4BHK
Apartment
for Sale in Nanakramguda\nNan...\n 1.70 Cr    \n\n\nCarpet Area\n\n 1816 sq.ft...Posted: Today    \nAgent: \nRnaveen\n
df.shape
Using
regex
to
modifying
the
columns
regex = "@\s(\d*)"
df['cost_per_sqft'] = df['features'].apply(lambda x: re.findall(regex, x))
df.head()
title
prices
features
booking_start
organizing
cost_per_sqft
0    \n3BHK
Apartment
for Sale in Kondapur\nIncor V...\n 1.41 Cr    \n\n\nCarpet Area\n\n 1850 sq.ft...Posted: 25
days
ago    \nAgent: \nRamana\n[7622]
1    \n4BHK
Apartment
for Sale in Shaikpet\nSalarpu...\n 3.04 Cr    \n\n\nCarpet Area\n\n 2224 sq.ft...Posted: 20
days
ago    \nBuilder: \nSalarpuria
Sattva
Group\n[13692]
2    \n
3
BHK
Apartment
for Sale in Jeedimetla\nEss...\n 74.02 L    \n\n\nCarpet Area\n\n 1260 sq.ft...Posted: 26
days
ago    \nAgent: \nHyderabad
Marketing
Team\n[5875]
3    \nNot
Furnished
2
BHK
Apartment
for Sale in Po...    \n 52.57 L    \n\n\nCarpet Area\n\n 914 sq.ft (...Posted: 18
days
ago    \nAgent: \nHyderabad
Marketing
Team\n[5753]
4    \nSemi
Furnished
2
BHK
Apartment
for Sale in Pa...    \n 30 L    \n\n\nCarpet Area\n\n 1200 sq.ft...Posted: Today    \nAgent: \nMarisetti
Saidaiah\n[2500]
regex = r'(\d*)\ssq.ft'

df['plot_area'] = df['features'].apply(lambda x: re.findall(regex, x))
df.head()
title
prices
features
booking_start
organizing
cost_per_sqft
plot_area
0    \n3BHK
Apartment
for Sale in Kondapur\nIncor V...\n 1.41 Cr    \n\n\nCarpet Area\n\n 1850 sq.ft...Posted: 25
days
ago    \nAgent: \nRamana\n[7622][1850]
1    \n4BHK
Apartment
for Sale in Shaikpet\nSalarpu...\n 3.04 Cr    \n\n\nCarpet Area\n\n 2224 sq.ft...Posted: 20
days
ago    \nBuilder: \nSalarpuria
Sattva
Group\n[13692][2224]
2    \n
3
BHK
Apartment
for Sale in Jeedimetla\nEss...\n 74.02 L    \n\n\nCarpet Area\n\n 1260 sq.ft...Posted: 26
days
ago    \nAgent: \nHyderabad
Marketing
Team\n[5875][1260]
3    \nNot
Furnished
2
BHK
Apartment
for Sale in Po...    \n 52.57 L    \n\n\nCarpet Area\n\n 914 sq.ft (...Posted: 18
days
ago    \nAgent: \nHyderabad
Marketing
Team\n[5753][914]
4    \nSemi
Furnished
2
BHK
Apartment
for Sale in Pa...    \n 30 L    \n\n\nCarpet Area\n\n 1200 sq.ft...Posted: Today    \nAgent: \nMarisetti
Saidaiah\n[2500][1200]
df.plot_area = df.plot_area.apply(lambda x: ''.join(x))
df.cost_per_sqft = df.cost_per_sqft.apply(lambda x: ''.join(x))
df.head()
title
prices
features
booking_start
organizing
cost_per_sqft
plot_area
0    \n3BHK
Apartment
for Sale in Kondapur\nIncor V...\n 1.41 Cr    \n\n\nCarpet Area\n\n 1850 sq.ft...Posted: 25
days
ago    \nAgent: \nRamana\n
7622
1850
1    \n4BHK
Apartment
for Sale in Shaikpet\nSalarpu...\n 3.04 Cr    \n\n\nCarpet Area\n\n 2224 sq.ft...Posted: 20
days
ago    \nBuilder: \nSalarpuria
Sattva
Group\n
13692
2224
2    \n
3
BHK
Apartment
for Sale in Jeedimetla\nEss...\n 74.02 L    \n\n\nCarpet Area\n\n 1260 sq.ft...Posted: 26
days
ago    \nAgent: \nHyderabad
Marketing
Team\n
5875
1260
3    \nNot
Furnished
2
BHK
Apartment
for Sale in Po...    \n 52.57 L    \n\n\nCarpet Area\n\n 914 sq.ft (...Posted: 18
days
ago    \nAgent: \nHyderabad
Marketing
Team\n
5753
914
4    \nSemi
Furnished
2
BHK
Apartment
for Sale in Pa...    \n 30 L    \n\n\nCarpet Area\n\n 1200 sq.ft...Posted: Today    \nAgent: \nMarisetti
Saidaiah\n
2500
1200
Replace
0
with space values in numerical columns
df["plot_area"].replace(to_replace="", value="0", inplace=True)
df.plot_area=df.plot_area.astype(int)

regex=r'\d+\s*BHK\s[A-Za-z]+'
df['type_of_house'] = df['title'].apply( lambda x: re.findall(regex, x))
df.head()
title
prices
features
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
0    \n3BHK
Apartment
for Sale in Kondapur\nIncor V...\n 1.41 Cr    \n\n\nCarpet Area\n\n 1850 sq.ft...Posted: 25
days
ago    \nAgent: \nRamana\n
7622
1850[3
BHK
Apartment]
1    \n4BHK
Apartment
for Sale in Shaikpet\nSalarpu...\n 3.04 Cr    \n\n\nCarpet Area\n\n 2224 sq.ft...Posted: 20
days
ago    \nBuilder: \nSalarpuria
Sattva
Group\n
13692
2224[4
BHK
Apartment]
2    \n
3
BHK
Apartment
for Sale in Jeedimetla\nEss...\n 74.02 L    \n\n\nCarpet Area\n\n 1260 sq.ft...Posted: 26
days
ago    \nAgent: \nHyderabad
Marketing
Team\n
5875
1260[3
BHK
Apartment]
3    \nNot
Furnished
2
BHK
Apartment
for Sale in Po...    \n 52.57 L    \n\n\nCarpet Area\n\n 914 sq.ft (...Posted: 18
days
ago    \nAgent: \nHyderabad
Marketing
Team\n
5753
914[2
BHK
Apartment]
4    \nSemi
Furnished
2
BHK
Apartment
for Sale in Pa...    \n 30 L    \n\n\nCarpet Area\n\n 1200 sq.ft...Posted: Today    \nAgent: \nMarisetti
Saidaiah\n
2500
1200[2
BHK
Apartment]
regex = r'in\s[A-Za-z]+'
df['place'] = df['title'].apply(lambda x: re.findall(regex, x))
df.head()
title
prices
features
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
0    \n3BHK
Apartment
for Sale in Kondapur\nIncor V...\n 1.41 Cr    \n\n\nCarpet Area\n\n 1850 sq.ft...Posted: 25
days
ago    \nAgent: \nRamana\n
7622
1850[3
BHK
Apartment]    [ in Kondapur]
1    \n4BHK
Apartment
for Sale in Shaikpet\nSalarpu...\n 3.04 Cr    \n\n\nCarpet Area\n\n 2224 sq.ft...Posted: 20
days
ago    \nBuilder: \nSalarpuria
Sattva
Group\n
13692
2224[4
BHK
Apartment]    [ in Shaikpet]
2    \n
3
BHK
Apartment
for Sale in Jeedimetla\nEss...\n 74.02 L    \n\n\nCarpet Area\n\n 1260 sq.ft...Posted: 26
days
ago    \nAgent: \nHyderabad
Marketing
Team\n
5875
1260[3
BHK
Apartment]    [ in Jeedimetla]
3    \nNot
Furnished
2
BHK
Apartment
for Sale in Po...    \n 52.57 L    \n\n\nCarpet Area\n\n 914 sq.ft (...Posted: 18
days
ago    \nAgent: \nHyderabad
Marketing
Team\n
5753
914[2
BHK
Apartment]    [ in Pocharam]
4    \nSemi
Furnished
2
BHK
Apartment
for Sale in Pa...    \n 30 L    \n\n\nCarpet Area\n\n 1200 sq.ft...Posted: Today    \nAgent: \nMarisetti
Saidaiah\n
2500
1200[2
BHK
Apartment]    [ in Patancheru]
df.place = df.place.apply(lambda x: ''.join(x))
df.head()
title
prices
features
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
0    \n3BHK
Apartment
for Sale in Kondapur\nIncor V...\n 1.41 Cr    \n\n\nCarpet Area\n\n 1850 sq.ft...Posted: 25
days
ago    \nAgent: \nRamana\n
7622
1850[3
BHK
Apartment] in Kondapur
1    \n4BHK
Apartment
for Sale in Shaikpet\nSalarpu...\n 3.04 Cr    \n\n\nCarpet Area\n\n 2224 sq.ft...Posted: 20
days
ago    \nBuilder: \nSalarpuria
Sattva
Group\n
13692
2224[4
BHK
Apartment] in Shaikpet
2    \n
3
BHK
Apartment
for Sale in Jeedimetla\nEss...\n 74.02 L    \n\n\nCarpet Area\n\n 1260 sq.ft...Posted: 26
days
ago    \nAgent: \nHyderabad
Marketing
Team\n
5875
1260[3
BHK
Apartment] in Jeedimetla
3    \nNot
Furnished
2
BHK
Apartment
for Sale in Po...    \n 52.57 L    \n\n\nCarpet Area\n\n 914 sq.ft (...Posted: 18
days
ago    \nAgent: \nHyderabad
Marketing
Team\n
5753
914[2
BHK
Apartment] in Pocharam
4    \nSemi
Furnished
2
BHK
Apartment
for Sale in Pa...    \n 30 L    \n\n\nCarpet Area\n\n 1200 sq.ft...Posted: Today    \nAgent: \nMarisetti
Saidaiah\n
2500
1200[2
BHK
Apartment] in Patancheru

regex = r'\s[A-Za-z]+'
df['place'] = df['place'].apply(lambda x: re.findall(regex, x))
df.head()
title
prices
features
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
0    \n3BHK
Apartment
for Sale in Kondapur\nIncor V...\n 1.41 Cr    \n\n\nCarpet Area\n\n 1850 sq.ft...Posted: 25
days
ago    \nAgent: \nRamana\n
7622
1850[3
BHK
Apartment]    [Kondapur]
1    \n4BHK
Apartment
for Sale in Shaikpet\nSalarpu...\n 3.04 Cr    \n\n\nCarpet Area\n\n 2224 sq.ft...Posted: 20
days
ago    \nBuilder: \nSalarpuria
Sattva
Group\n
13692
2224[4
BHK
Apartment]    [Shaikpet]
2    \n
3
BHK
Apartment
for Sale in Jeedimetla\nEss...\n 74.02 L    \n\n\nCarpet Area\n\n 1260 sq.ft...Posted: 26
days
ago    \nAgent: \nHyderabad
Marketing
Team\n
5875
1260[3
BHK
Apartment]    [Jeedimetla]
3    \nNot
Furnished
2
BHK
Apartment
for Sale in Po...    \n 52.57 L    \n\n\nCarpet Area\n\n 914 sq.ft (...Posted: 18
days
ago    \nAgent: \nHyderabad
Marketing
Team\n
5753
914[2
BHK
Apartment]    [Pocharam]
4    \nSemi
Furnished
2
BHK
Apartment
for Sale in Pa...    \n 30 L    \n\n\nCarpet Area\n\n 1200 sq.ft...Posted: Today    \nAgent: \nMarisetti
Saidaiah\n
2500
1200[2
BHK
Apartment]    [Patancheru]

regex = r'\d+'
df['booking_start'] = df['booking_start'].apply(lambda x: re.findall(regex, x))
df.type_of_house = df.type_of_house.apply(lambda x: ''.join(x))
df.place = df.place.apply(lambda x: ''.join(x))
df.place = df.place.apply(lambda x: ''.join(x))
regex = r'\d'
df['type_BHK'] = df['type_of_house'].apply(lambda x: re.findall(regex, x))
df.head()
title
prices
features
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
0    \n3BHK
Apartment
for Sale in Kondapur\nIncor V...\n 1.41 Cr    \n\n\nCarpet Area\n\n 1850 sq.ft...[25]    \nAgent: \
    nRamana\n
7622
1850
3
BHK
Apartment
Kondapur[3]
1    \n4BHK
Apartment
for Sale in Shaikpet\nSalarpu...\n 3.04 Cr    \n\n\nCarpet Area\n\n 2224 sq.ft...[20]    \nBuilder: \
    nSalarpuria
Sattva
Group\n
13692
2224
4
BHK
Apartment
Shaikpet[4]
2    \n
3
BHK
Apartment
for Sale in Jeedimetla\nEss...\n 74.02 L    \n\n\nCarpet Area\n\n 1260 sq.ft...[26]    \nAgent: \
    nHyderabad
Marketing
Team\n
5875
1260
3
BHK
Apartment
Jeedimetla[3]
3    \nNot
Furnished
2
BHK
Apartment
for Sale in Po...    \n 52.57 L    \n\n\nCarpet Area\n\n 914 sq.ft (...[18]    \nAgent: \
    nHyderabad
Marketing
Team\n
5753
914
2
BHK
Apartment
Pocharam[2]
4    \nSemi
Furnished
2
BHK
Apartment
for Sale in Pa...    \n 30 L    \n\n\nCarpet Area\n\n 1200 sq.ft...[]    \nAgent: \
    nMarisetti
Saidaiah\n
2500
1200
2
BHK
Apartment
Patancheru[2]
df.type_BHK = df.type_BHK.apply(lambda x: ''.join(x))
df.head()
title
prices
features
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
0    \n3BHK
Apartment
for Sale in Kondapur\nIncor V...\n 1.41 Cr    \n\n\nCarpet Area\n\n 1850 sq.ft...[25]    \nAgent: \
    nRamana\n
7622
1850
3
BHK
Apartment
Kondapur
3
1    \n4BHK
Apartment
for Sale in Shaikpet\nSalarpu...\n 3.04 Cr    \n\n\nCarpet Area\n\n 2224 sq.ft...[20]    \nBuilder: \
    nSalarpuria
Sattva
Group\n
13692
2224
4
BHK
Apartment
Shaikpet
4
2    \n
3
BHK
Apartment
for Sale in Jeedimetla\nEss...\n 74.02 L    \n\n\nCarpet Area\n\n 1260 sq.ft...[26]    \nAgent: \
    nHyderabad
Marketing
Team\n
5875
1260
3
BHK
Apartment
Jeedimetla
3
3    \nNot
Furnished
2
BHK
Apartment
for Sale in Po...    \n 52.57 L    \n\n\nCarpet Area\n\n 914 sq.ft (...[18]    \nAgent: \
    nHyderabad
Marketing
Team\n
5753
914
2
BHK
Apartment
Pocharam
2
4    \nSemi
Furnished
2
BHK
Apartment
for Sale in Pa...    \n 30 L    \n\n\nCarpet Area\n\n 1200 sq.ft...[]    \nAgent: \
    nMarisetti
Saidaiah\n
2500
1200
2
BHK
Apartment
Patancheru
2
Removing
unwanted
columns
df.drop('features', axis=1, inplace=True)
df.head()
title
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
0    \n3BHK
Apartment
for Sale in Kondapur\nIncor V...\n 1.41 Cr[25]    \nAgent: \
    nRamana\n
7622
1850
3
BHK
Apartment
Kondapur
3
1    \n4BHK
Apartment
for Sale in Shaikpet\nSalarpu...\n 3.04 Cr[20]    \nBuilder: \
    nSalarpuria
Sattva
Group\n
13692
2224
4
BHK
Apartment
Shaikpet
4
2    \n
3
BHK
Apartment
for Sale in Jeedimetla\nEss...\n 74.02 L[26]    \nAgent: \
    nHyderabad
Marketing
Team\n
5875
1260
3
BHK
Apartment
Jeedimetla
3
3    \nNot
Furnished
2
BHK
Apartment
for Sale in Po...    \n 52.57 L[18]    \nAgent: \
    nHyderabad
Marketing
Team\n
5753
914
2
BHK
Apartment
Pocharam
2
4    \nSemi
Furnished
2
BHK
Apartment
for Sale in Pa...    \n 30 L[]    \nAgent: \
    nMarisetti
Saidaiah\n
2500
1200
2
BHK
Apartment
Patancheru
2
df.drop('title', axis=1, inplace=True)
df.head(12)
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
0    \n
1.41
Cr[25]    \nAgent: \nRamana\n
7622
1850
3
BHK
Apartment
Kondapur
3
1    \n
3.04
Cr[20]    \nBuilder: \nSalarpuria
Sattva
Group\n
13692
2224
4
BHK
Apartment
Shaikpet
4
2    \n
74.02
L[26]    \nAgent: \nHyderabad
Marketing
Team\n
5875
1260
3
BHK
Apartment
Jeedimetla
3
3    \n
52.57
L[18]    \nAgent: \nHyderabad
Marketing
Team\n
5753
914
2
BHK
Apartment
Pocharam
2
4    \n
30
L[]    \nAgent: \nMarisetti
Saidaiah\n
2500
1200
2
BHK
Apartment
Patancheru
2
5    \n
52
L[]    \nAgent: \nShiv
Shankar\n
6500
800
2
BHK
Villa
Indresham
2
6    \n
52
L[]    \nAgent: \nShiv
Shankar\n
6500
800
2
BHK
Villa
Indresham
2
7    \n
1.70
Cr[]    \nAgent: \nRnaveen\n
9374
1816
4
BHK
Apartment
Nanakramguda
4
8    \n
2.24
Cr[]    \nAgent: \nRnaveen\n
9374
2400
4
BHK
Apartment
Nanakramguda
4
9    \n
1.16
Cr[]    \nAgent: \nMarisetti
Saidaiah\n
4500
2580
4
BHK
Villa
Beeramguda
4
10    \n
39.69
L[]    \nAgent: \nMarisetti
Saidaiah\n
3000
1323
2
BHK
Apartment
Patancheru
2
11    \n
84.03
L[]    \nAgent: \nMarisetti
Saidaiah\n
4949
1698
3
BHK
Apartment
Pragathi
3

df.booking_start = df.booking_start.apply(lambda x: ''.join(x))
df["booking_start"].value_counts().sum()

df.head(10)
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
0    \n
1.41
Cr
25    \nAgent: \nRamana\n
7622
1850
3
BHK
Apartment
Kondapur
3
1    \n
3.04
Cr
20    \nBuilder: \nSalarpuria
Sattva
Group\n
13692
2224
4
BHK
Apartment
Shaikpet
4
2    \n
74.02
L
26    \nAgent: \nHyderabad
Marketing
Team\n
5875
1260
3
BHK
Apartment
Jeedimetla
3
3    \n
52.57
L
18    \nAgent: \nHyderabad
Marketing
Team\n
5753
914
2
BHK
Apartment
Pocharam
2
4    \n
30
L        \nAgent: \nMarisetti
Saidaiah\n
2500
1200
2
BHK
Apartment
Patancheru
2
5    \n
52
L        \nAgent: \nShiv
Shankar\n
6500
800
2
BHK
Villa
Indresham
2
6    \n
52
L        \nAgent: \nShiv
Shankar\n
6500
800
2
BHK
Villa
Indresham
2
7    \n
1.70
Cr        \nAgent: \nRnaveen\n
9374
1816
4
BHK
Apartment
Nanakramguda
4
8    \n
2.24
Cr        \nAgent: \nRnaveen\n
9374
2400
4
BHK
Apartment
Nanakramguda
4
9    \n
1.16
Cr        \nAgent: \nMarisetti
Saidaiah\n
4500
2580
4
BHK
Villa
Beeramguda
4
Total
scraped
data
df
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
0    \n
1.41
Cr
25    \nAgent: \nRamana\n
7622
1850
3
BHK
Apartment
Kondapur
3
1    \n
3.04
Cr
20    \nBuilder: \nSalarpuria
Sattva
Group\n
13692
2224
4
BHK
Apartment
Shaikpet
4
2    \n
74.02
L
26    \nAgent: \nHyderabad
Marketing
Team\n
5875
1260
3
BHK
Apartment
Jeedimetla
3
3    \n
52.57
L
18    \nAgent: \nHyderabad
Marketing
Team\n
5753
914
2
BHK
Apartment
Pocharam
2
4    \n
30
L        \nAgent: \nMarisetti
Saidaiah\n
2500
1200
2
BHK
Apartment
Patancheru
2
    ...........................
527    \n
89
L
10    \nAgent: \nHyderabad
Marketing
Team\n
9214
966
2
BHK
Apartment
Gandipet
2
528    \n
1.84
Cr
10    \nAgent: \nHyderabad
Marketing
Team\n
10421
1767
1
BHK
Villa
Srisailam
1
529    \n
1.40
Cr
23    \nAgent: \nVikas
Triwedi
Esolis\n
10903
1284
3
BHK
Apartment
Nallagandla
3
530    \n
70.45
L
4    \nAgent: \nHyderabad
Marketing
Team\n
6874
1025
2
BHK
Apartment
Tellapur
2
531    \n
1.23
Cr
4    \nAgent: \nHyderabad
Marketing
Team\n
7500
1644
3
BHK
Apartment
Trimulgherry
3
532
rows × 8
columns

df.shape
df.info()
df.isnull().sum()
Checking
null
values
df[df.type_of_house == '']
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
62    \n
1.40
Cr
1    \nAgent: \nManikanta
properties\n
5000
2800
Hayat
177    \n
17.34
Cr
4    \nAgent: \nHyderabad
Marketing
Team\n
17501
9908
Jubilee
202    \n
1.06
Cr
4    \nAgent: \nHyderabad
Marketing
Team\n
6019
1761
Attapur
210    \n
9.84
Cr
4    \nAgent: \nHyderabad
Marketing
Team\n
17496
5624
Jubilee
289    \n
1.06
Cr
4    \nAgent: \nHyderabad
Marketing
Team\n
6019
1761
Attapur
338    \n
1.06
Cr
4    \nAgent: \nHyderabad
Marketing
Team\n
6019
1761
Attapur
df["type_BHK"].replace(to_replace="", value="3", inplace=True)
df.type_BHK = df.type_BHK.astype(int)
df.head()
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
0    \n
1.41
Cr
25    \nAgent: \nRamana\n
7622
1850
3
BHK
Apartment
Kondapur
3
1    \n
3.04
Cr
20    \nBuilder: \nSalarpuria
Sattva
Group\n
13692
2224
4
BHK
Apartment
Shaikpet
4
2    \n
74.02
L
26    \nAgent: \nHyderabad
Marketing
Team\n
5875
1260
3
BHK
Apartment
Jeedimetla
3
3    \n
52.57
L
18    \nAgent: \nHyderabad
Marketing
Team\n
5753
914
2
BHK
Apartment
Pocharam
2
4    \n
30
L        \nAgent: \nMarisetti
Saidaiah\n
2500
1200
2
BHK
Apartment
Patancheru
2
df[df.type_BHK == '']
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
df["cost_per_sqft"].replace(to_replace="", value="0", inplace=True)
df.cost_per_sqft = df.cost_per_sqft.astype(float)
df.head()
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
0    \n
1.41
Cr
25    \nAgent: \nRamana\n
7622.0
1850
3
BHK
Apartment
Kondapur
3
1    \n
3.04
Cr
20    \nBuilder: \nSalarpuria
Sattva
Group\n
13692.0
2224
4
BHK
Apartment
Shaikpet
4
2    \n
74.02
L
26    \nAgent: \nHyderabad
Marketing
Team\n
5875.0
1260
3
BHK
Apartment
Jeedimetla
3
3    \n
52.57
L
18    \nAgent: \nHyderabad
Marketing
Team\n
5753.0
914
2
BHK
Apartment
Pocharam
2
4    \n
30
L        \nAgent: \nMarisetti
Saidaiah\n
2500.0
1200
2
BHK
Apartment
Patancheru
2
df[df.type_BHK == '']
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK

df.info()

df.prices = df.prices.apply(lambda x: x.replace('\n', '') if '' in x else x)
df.drop(df[df['prices'] == '          Call For Price        '].index, inplace=True)
df['prices'] = df['prices'].apply(lambda x: float(x.replace('L', '')) * 100000 if 'L' in x else
float(x.replace('Cr', '')) * 10000000 if 'Cr' in x else float(x))
df['prices'] = df['prices'].astype(float)
df['prices']
df.organizing = df.organizing.apply(lambda x: x.replace('\n', '') if '' in x else x)

df.info()
df.head()
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
0
14100000.0
25
Agent: Ramana
7622.0
1850
3
BHK
Apartment
Kondapur
3
1
30400000.0
20
Builder: Salarpuria
Sattva
Group
13692.0
2224
4
BHK
Apartment
Shaikpet
4
2
7402000.0
26
Agent: Hyderabad
Marketing
Team
5875.0
1260
3
BHK
Apartment
Jeedimetla
3
3
5257000.0
18
Agent: Hyderabad
Marketing
Team
5753.0
914
2
BHK
Apartment
Pocharam
2
4
3000000.0
Agent: Marisetti
Saidaiah
2500.0
1200
2
BHK
Apartment
Patancheru
2
df["booking_start"].replace(to_replace="", value="0", inplace=True)
df.booking_start = df.booking_start.astype(int)
df.head(10)
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
0
14100000.0
25
Agent: Ramana
7622.0
1850
3
BHK
Apartment
Kondapur
3
1
30400000.0
20
Builder: Salarpuria
Sattva
Group
13692.0
2224
4
BHK
Apartment
Shaikpet
4
2
7402000.0
26
Agent: Hyderabad
Marketing
Team
5875.0
1260
3
BHK
Apartment
Jeedimetla
3
3
5257000.0
18
Agent: Hyderabad
Marketing
Team
5753.0
914
2
BHK
Apartment
Pocharam
2
4
3000000.0
0
Agent: Marisetti
Saidaiah
2500.0
1200
2
BHK
Apartment
Patancheru
2
5
5200000.0
0
Agent: Shiv
Shankar
6500.0
800
2
BHK
Villa
Indresham
2
6
5200000.0
0
Agent: Shiv
Shankar
6500.0
800
2
BHK
Villa
Indresham
2
7
17000000.0
0
Agent: Rnaveen
9374.0
1816
4
BHK
Apartment
Nanakramguda
4
8
22400000.0
0
Agent: Rnaveen
9374.0
2400
4
BHK
Apartment
Nanakramguda
4
9
11600000.0
0
Agent: Marisetti
Saidaiah
4500.0
2580
4
BHK
Villa
Beeramguda
4

df.info()

df["type_of_house"] = df["type_of_house"].apply(lambda x: x.replace(' ', ''))
df
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
0
14100000.0
25
Agent: Ramana
7622.0
1850
3
BHKApartment
Kondapur
3
1
30400000.0
20
Builder: Salarpuria
Sattva
Group
13692.0
2224
4
BHKApartment
Shaikpet
4
2
7402000.0
26
Agent: Hyderabad
Marketing
Team
5875.0
1260
3
BHKApartment
Jeedimetla
3
3
5257000.0
18
Agent: Hyderabad
Marketing
Team
5753.0
914
2
BHKApartment
Pocharam
2
4
3000000.0
0
Agent: Marisetti
Saidaiah
2500.0
1200
2
BHKApartment
Patancheru
2
    ...........................
527
8900000.0
10
Agent: Hyderabad
Marketing
Team
9214.0
966
2
BHKApartment
Gandipet
2
528
18400000.0
10
Agent: Hyderabad
Marketing
Team
10421.0
1767
1
BHKVilla
Srisailam
1
529
14000000.0
23
Agent: Vikas
Triwedi
Esolis
10903.0
1284
3
BHKApartment
Nallagandla
3
530
7045000.0
4
Agent: Hyderabad
Marketing
Team
6874.0
1025
2
BHKApartment
Tellapur
2
531
12300000.0
4
Agent: Hyderabad
Marketing
Team
7500.0
1644
3
BHKApartment
Trimulgherry
3
531
rows × 8
columns

droping
unwanted
rows
df.drop(df[df["type_of_house"] == ""].index, inplace=True)
df.head()
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
0
14100000.0
25
Agent: Ramana
7622.0
1850
3
BHKApartment
Kondapur
3
1
30400000.0
20
Builder: Salarpuria
Sattva
Group
13692.0
2224
4
BHKApartment
Shaikpet
4
2
7402000.0
26
Agent: Hyderabad
Marketing
Team
5875.0
1260
3
BHKApartment
Jeedimetla
3
3
5257000.0
18
Agent: Hyderabad
Marketing
Team
5753.0
914
2
BHKApartment
Pocharam
2
4
3000000.0
0
Agent: Marisetti
Saidaiah
2500.0
1200
2
BHKApartment
Patancheru
2

visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
df
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
0
14100000.0
25
Agent: Ramana
7622.0
1850
3
BHKApartment
Kondapur
3
1
30400000.0
20
Builder: Salarpuria
Sattva
Group
13692.0
2224
4
BHKApartment
Shaikpet
4
2
7402000.0
26
Agent: Hyderabad
Marketing
Team
5875.0
1260
3
BHKApartment
Jeedimetla
3
3
5257000.0
18
Agent: Hyderabad
Marketing
Team
5753.0
914
2
BHKApartment
Pocharam
2
4
3000000.0
0
Agent: Marisetti
Saidaiah
2500.0
1200
2
BHKApartment
Patancheru
2
    ...........................
527
8900000.0
10
Agent: Hyderabad
Marketing
Team
9214.0
966
2
BHKApartment
Gandipet
2
528
18400000.0
10
Agent: Hyderabad
Marketing
Team
10421.0
1767
1
BHKVilla
Srisailam
1
529
14000000.0
23
Agent: Vikas
Triwedi
Esolis
10903.0
1284
3
BHKApartment
Nallagandla
3
530
7045000.0
4
Agent: Hyderabad
Marketing
Team
6874.0
1025
2
BHKApartment
Tellapur
2
531
12300000.0
4
Agent: Hyderabad
Marketing
Team
7500.0
1644
3
BHKApartment
Trimulgherry
3
525
rows × 8
columns

df["type_BHK"].value_counts()
Defining
rooms
using
histogram
fig = plt.subplots(figsize=(8, 6))
sns.distplot(df['type_BHK'], hist=True, rug=False, color="r")

Booking
using
kde
plot
fig = plt.subplots(figsize=(10, 6))
sns.kdeplot(data=df, x="booking_start", hue="type_BHK", multiple="stack")

Defining
outliers
fig = plt.subplots(figsize=(17, 8))
sns.boxplot(x='type_of_house', y='plot_area', data=df)

plot
area
by
barplot
fig = plt.subplots(figsize=(12, 8))
sns.barplot(x="type_BHK", y="plot_area", data=df)

import matplotlib.pyplot as plt

# plt.figure(figsize=(20,10)
# explode = [0,0,0,0,0]
plt.pie(df["type_BHK"].value_counts(), startangle=90, autopct="%.3f",
        labels=["1", "2", "3", "4", "5"])
plt.title('Distribution of BHK in the total city', fontsize=30)

visualization
using
plotly
! pip
install
plotly
pip
install
cufflinks
from plotly.offline import init_notebook_mode, iplot
import plotly.figure_factory as ff
import cufflinks

cufflinks.go_offline()
cufflinks.set_config_file(world_readable=True, theme='pearl')
import plotly.graph_objs as go
import plotly
from plotly import tools

init_notebook_mode(connected=True)

df
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
0
14100000.0
25
Agent: Ramana
7622.0
1850
3
BHKApartment
Kondapur
3
1
30400000.0
20
Builder: Salarpuria
Sattva
Group
13692.0
2224
4
BHKApartment
Shaikpet
4
2
7402000.0
26
Agent: Hyderabad
Marketing
Team
5875.0
1260
3
BHKApartment
Jeedimetla
3
3
5257000.0
18
Agent: Hyderabad
Marketing
Team
5753.0
914
2
BHKApartment
Pocharam
2
4
3000000.0
0
Agent: Marisetti
Saidaiah
2500.0
1200
2
BHKApartment
Patancheru
2
    ...........................
527
8900000.0
10
Agent: Hyderabad
Marketing
Team
9214.0
966
2
BHKApartment
Gandipet
2
528
18400000.0
10
Agent: Hyderabad
Marketing
Team
10421.0
1767
1
BHKVilla
Srisailam
1
529
14000000.0
23
Agent: Vikas
Triwedi
Esolis
10903.0
1284
3
BHKApartment
Nallagandla
3
530
7045000.0
4
Agent: Hyderabad
Marketing
Team
6874.0
1025
2
BHKApartment
Tellapur
2
531
12300000.0
4
Agent: Hyderabad
Marketing
Team
7500.0
1644
3
BHKApartment
Trimulgherry
3
525
rows × 8
columns

Price
of
houses
# df.prices.iplot(
#     kind='hist',
#     bins=100,
#     xTitle='prices in all the rows',
#     color = 'green',
#     linecolor='black',
#     yTitle='count',
#     title='price of houses ')
Available
areas
using
bar
plot
# px.bar(df,x="place",y="plot_area")

Scatter
plot
import plotly.express as px

px.scatter(df, x="place", y="plot_area", size_max=20)
# df.booking_start.iplot(
#     kind='hist',
#     bins=100,
#     xTitle='booking start days ago',
#     color = 'black',
#     linecolor='white',
#     yTitle='count',
#     title='booking')
import plotly

Express as px
fig = px.scatter(df, x="plot_area", y="place", color="no_of_rooms")
fig.show()
File
"<ipython-input-73-bd0f54a2e0d6>", line
1
import plotly

Express as px
           ^
           SyntaxError: invalid
syntax

A
person
wants
a
Villa
Here
we
will
give
information
about
villas
with their priorities
df_pie=df[(df["plot_area"] >= 3000) & (df["plot_area"] <= 5000)]
df_pie.head()
prices    booking_start    organizing    cost_per_sqft    plot_area    type_of_house    place    type_BHK
24    34100000.0    0    Agent: Rnaveen
10396.0
3280
4
BHKApartment
Himayath
4
51
39200000.0
3
Agent: square
10889.0
3600
3
BHKVilla
Mokila
3
54
13600000.0
18
Agent: Rajineesh
4300.0
3180
4
BHKVilla
Beeramguda
4
74
45000000.0
18
Agent: Marketing
Team
12500.0
3600
4
BHKApartment
Banjara
4
108
15600000.0
18
Agent: Rajineesh
4300.0
3630
4
BHKVilla
Beeramguda
4
import matplotlib.pyplot as plt

plt.figure(figsize=(15, 12))
explode = [0, 0, 0.1]
plt.pie(df_pie["type_of_house"].value_counts(), startangle=90, autopct="%.3f",
        labels=["4BHKApartment", "3BHKVilla", "4BHKVilla"], shadow=True, explode=explode)
plt.title('Distribution of 4BHK-Villa,3BHK-Villa and 4BHK-Apartment', fontsize=35)

df_v = df[(df["type_of_house"] == "4BHKVilla")]
df_v
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
9
11600000.0
0
Agent: Marisetti
Saidaiah
4500.0
2580
4
BHKVilla
Beeramguda
4
54
13600000.0
18
Agent: Rajineesh
4300.0
3180
4
BHKVilla
Beeramguda
4
108
15600000.0
18
Agent: Rajineesh
4300.0
3630
4
BHKVilla
Beeramguda
4
113
40000000.0
10
Agent: Rnaveen
8333.0
4800
4
BHKVilla
Begumpet
4
227
63000000.0
4
Agent: Hyderabad
Marketing
Team
17365.0
3628
4
BHKVilla
Tellapur
4
325
9033000.0
26
Agent: Hyderabad
Marketing
Team
7013.0
1288
4
BHKVilla
Rampally
4
383
40400000.0
4
Agent: Hyderabad
Marketing
Team
10625.0
3808
4
BHKVilla
Shamshabad
4
391
63000000.0
4
Agent: Hyderabad
Marketing
Team
17365.0
3628
4
BHKVilla
Tellapur
4
399
7500000.0
39
Builder: CHANDRAKANTH
REDDY
5000.0
1500
4
BHKVilla
Maheshwaram
4
402
11600000.0
0
Agent: Marisetti
Saidaiah
4500.0
2580
4
BHKVilla
Beeramguda
4
443
40000000.0
5
Agent: Hyderabad
Marketing
Team
14409.0
2776
4
BHKVilla
Tellapur
4
459
63000000.0
18
Agent: Hyderabad
Marketing
Team
16579.0
3800
4
BHKVilla
Kismatpur
4
508
240000000.0
23
Agent: Rnaveen
41379.0
5800
4
BHKVilla
Nanakramguda
4
509
240000000.0
23
Agent: Rnaveen
41667.0
5760
4
BHKVilla
Puppalaguda
4
fig = plt.subplots(figsize=(10, 8))
sns.kdeplot(data=df_v, x="plot_area", hue="organizing", multiple="stack")

fig = plt.subplots(figsize=(12, 10))
sns.barplot(x="place", y="plot_area", data=df_v)

df_v1 = df_v[(df_v["plot_area"] >= 2000) & (df_v["plot_area"] <= 5000)]
df_v1
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
9
11600000.0
0
Agent: Marisetti
Saidaiah
4500.0
2580
4
BHKVilla
Beeramguda
4
54
13600000.0
18
Agent: Rajineesh
4300.0
3180
4
BHKVilla
Beeramguda
4
108
15600000.0
18
Agent: Rajineesh
4300.0
3630
4
BHKVilla
Beeramguda
4
113
40000000.0
10
Agent: Rnaveen
8333.0
4800
4
BHKVilla
Begumpet
4
227
63000000.0
4
Agent: Hyderabad
Marketing
Team
17365.0
3628
4
BHKVilla
Tellapur
4
383
40400000.0
4
Agent: Hyderabad
Marketing
Team
10625.0
3808
4
BHKVilla
Shamshabad
4
391
63000000.0
4
Agent: Hyderabad
Marketing
Team
17365.0
3628
4
BHKVilla
Tellapur
4
402
11600000.0
0
Agent: Marisetti
Saidaiah
4500.0
2580
4
BHKVilla
Beeramguda
4
443
40000000.0
5
Agent: Hyderabad
Marketing
Team
14409.0
2776
4
BHKVilla
Tellapur
4
459
63000000.0
18
Agent: Hyderabad
Marketing
Team
16579.0
3800
4
BHKVilla
Kismatpur
4
df_v2 = df_v1[(df_v1["prices"] >= 20000000) & (df_v1["prices"] <= 40000000)]
df_v2
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
113
40000000.0
10
Agent: Rnaveen
8333.0
4800
4
BHKVilla
Begumpet
4
443
40000000.0
5
Agent: Hyderabad
Marketing
Team
14409.0
2776
4
BHKVilla
Tellapur
4

A
person
wants
a
Apartment
Here
we
will
give
information
about
Apartments
with their priorities
df_A=df[(df["type_of_house"] == "3BHKApartment")]
df_A
prices    booking_start    organizing    cost_per_sqft    plot_area    type_of_house    place    type_BHK
0    14100000.0    25    Agent: Ramana
7622.0
1850
3
BHKApartment
Kondapur
3
2
7402000.0
26
Agent: Hyderabad
Marketing
Team
5875.0
1260
3
BHKApartment
Jeedimetla
3
11
8403000.0
0
Agent: Marisetti
Saidaiah
4949.0
1698
3
BHKApartment
Pragathi
3
14
4500000.0
0
Agent: Marisetti
Saidaiah
3000.0
1500
3
BHKApartment
Patancheru
3
20
7537000.0
0
Agent: Rnaveen
5625.0
1340
3
BHKApartment
Osman
3
    ...........................
515
10800000.0
10
Agent: Hyderabad
Marketing
Team
8212.0
1327
3
BHKApartment
Gandipet
3
519
14100000.0
25
Agent: Ramana
7622.0
1850
3
BHKApartment
Kondapur
3
525
9000000.0
10
Agent: Hyderabad
Marketing
Team
7550.0
1192
3
BHKApartment
Nallagandla
3
529
14000000.0
23
Agent: Vikas
Triwedi
Esolis
10903.0
1284
3
BHKApartment
Nallagandla
3
531
12300000.0
4
Agent: Hyderabad
Marketing
Team
7500.0
1644
3
BHKApartment
Trimulgherry
3
215
rows × 8
columns

df_A1 = df_A[(df_A["prices"] >= 20000000) & (df_A["prices"] <= 50000000)]
df_A1
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
52
26500000.0
2
Agent: Rnaveen
13750.0
1928
3
BHKApartment
Himayath
3
146
35400000.0
4
Agent: Hyderabad
Marketing
Team
16668.0
2128
3
BHKApartment
Kokapet
3
157
22400000.0
4
Agent: Hyderabad
Marketing
Team
16668.0
1348
3
BHKApartment
Kokapet
3
255
22500000.0
4
Agent: Hyderabad
Marketing
Team
8765.0
2567
3
BHKApartment
Narsingi
3
359
21800000.0
4
Agent: Hyderabad
Marketing
Team
9998.0
2182
3
BHKApartment
Punjagutta
3
466
21800000.0
26
Agent: anjan
12111.0
1800
3
BHKApartment
Kondapur
3
468
20700000.0
26
Agent: pawan
12545.0
1650
3
BHKApartment
Kondapur
3
496
24700000.0
20
Builder: Salarpuria
Sattva
Group
12651.0
1958
3
BHKApartment
Shaikpet
3
513
28500000.0
10
Agent: Hyderabad
Marketing
Team
10656.0
2680
3
BHKApartment
Kondapur
3
fig = plt.subplots(figsize=(12, 10))
sns.distplot(df_A['plot_area'], kde=True, rug=False, color="red")

import warnings

warnings.filterwarnings('ignore')
fig = plt.subplots(figsize=(10, 8))
sns.kdeplot(data=df_A1, x="plot_area", hue="place", multiple="stack")

# df_A1.plot_area.iplot(
#     kind='hist',
#     bins=100,
#     xTitle='plot_area in all the rows',
#     color = 'green',
#     linecolor='black',
#     yTitle='count',
#     title='plot_area  ')
df_A2 = df_A1[(df_A1["plot_area"] >= 2500) & (df_A1["plot_area"] <= 4000)]
df_A2
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
255
22500000.0
4
Agent: Hyderabad
Marketing
Team
8765.0
2567
3
BHKApartment
Narsingi
3
513
28500000.0
10
Agent: Hyderabad
Marketing
Team
10656.0
2680
3
BHKApartment
Kondapur
3
df_A3 = df_A2[df_A2["cost_per_sqft"] >= 10000]
df_A3
prices
booking_start
organizing
cost_per_sqft
plot_area
type_of_house
place
type_BHK
513
28500000.0
10
Agent: Hyderabad
Marketing
Team
10656.0
2680
3
BHKApartment
Kondapur
3






