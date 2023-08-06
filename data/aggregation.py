import requests
import json
import os
import time,datetime

def updateJsonFile( path, data ):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Actual temperature
waterData = {}
url = 'https://data.bs.ch/api/v2/catalog/datasets/100046/records?order_by=startzeitpunkt%20DESC&limit=2&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

if d['records'][0]['record']['fields']['rus_w_o_s3_te'] is not None:
    waterData['actualValue'] = d['records'][0]['record']['fields']['rus_w_o_s3_te']
    waterData['lastUpdate'] = d['records'][0]['record']['fields']['startzeitpunkt']
else:
    print('newest temp is null we take next older one')
    if d['records'][1]['record']['fields']['rus_w_o_s3_te'] is not None:
        waterData['actualValue'] = d['records'][1]['record']['fields']['rus_w_o_s3_te']
        waterData['lastUpdate'] = d['records'][1]['record']['fields']['startzeitpunkt']
    else: 
        print('no valid temp')
        waterData['actualValue'] = 0
        waterData['lastUpdate'] = None

# Weekly data
waterData['chart'] = {}
waterData['chart']['week'] = []
url = 'https://data.bs.ch/api/v2/catalog/datasets/100046/records?select=avg(rus_w_o_s3_te)%20as%20temp&where=startzeitpunkt%3E%3Dnow(days%3D-7)&group_by=range(startzeitpunkt%2C%2012%20hour)%20as%20time&limit=900&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldT = ''
for e in d['records']:
    if  e['record']['fields']['temp'] is not None:
        waterData['chart']['week'].append(e['record']['fields']['temp'])
        oldT = e['record']['fields']['temp']
    else:
        waterData['chart']['week'].append(oldT | 0)

# Monthly data
waterData['chart']['month'] = []
url = 'https://data.bs.ch/api/v2/catalog/datasets/100046/records?select=avg(rus_w_o_s3_te)%20as%20temp&where=startzeitpunkt%3E%3Dnow(days%3D-30)&group_by=range(startzeitpunkt,2days)%20as%20time&limit=900&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldT = ''
for e in d['records']:
    if e['record']['fields']['temp'] is not None:
        waterData['chart']['month'].append(e['record']['fields']['temp'])
        oldT = e['record']['fields']['temp']
    else:
        waterData['chart']['month'].append(oldT | 0)

updateJsonFile( 'data/data/waterData.json', waterData)

# Air temperature
airData = {}
url = 'https://data.bs.ch/api/v2/catalog/datasets/100009/records?select=meta_airtemp%20as%20temp&where=name_original="0340A010"&limit=1&pretty=false&timezone=UTC&order_by=record_timestamp%20DESC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

try:
    d['records'][0]['record']['fields']['temp']
except NameError:
    print('air temp not defined')
    try: 
        d['records'][1]['record']['fields']['rus_w_o_s3_te']
    except NameError:
        print('last air temp not defined')
        airData['actualValue'] = 0
        airData['lastUpdate'] = None
    else:
        airData['actualValue'] = d['records'][1]['record']['fields']['temp']
        airData['lastUpdate'] = d['records'][1]['record']['timestamp']
else:
    airData['actualValue'] = d['records'][0]['record']['fields']['temp']
    airData['lastUpdate'] = d['records'][0]['record']['timestamp']

# Weekly data
airData['chart'] = {}
airData['chart']['week'] = []
url = 'https://data.bs.ch/api/v2/catalog/datasets/100009/records?select=avg(meta_airtemp)%20as%20temp&where=name_original="0340A010"%20and%20record_timestamp%3E%3Dnow(days%3D-7)&group_by=range(record_timestamp%2C%206%20hour)%20as%20time&limit=900&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldT = ''
for e in d['records']:
    try:
        e['record']['fields']['temp']
    except NameError:
        airData['chart']['week'].append(oldT | 0)
    else:
        airData['chart']['week'].append(e['record']['fields']['temp'])
        oldT = e['record']['fields']['temp']

# Monthly data
airData['chart']['month'] = []
url = 'https://data.bs.ch/api/v2/catalog/datasets/100009/records?select=avg(meta_airtemp)%20as%20temp&where=name_original="0340A010"%20and%20record_timestamp%3E%3Dnow(days%3D-30)&group_by=range(record_timestamp,2days)%20as%20time&limit=900&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldT = ''
for e in d['records']:
    try:
        e['record']['fields']['temp']
    except NameError:
        airData['chart']['month'].append(oldT | 0)
    else:
        airData['chart']['month'].append(e['record']['fields']['temp'])
        oldT = e['record']['fields']['temp']

updateJsonFile( 'data/data/airData.json', airData)

# Water level
levelData = {}
url = 'https://data.bs.ch/api/records/1.0/analyze?dataset=100089&y.pegel.func=AVG&y.pegel.expr=pegel&precision=year&x=timestamp&sort=-x&exclude.pegel=0'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
lastAvg = d[1]['pegel']

url = 'https://data.bs.ch/api/v2/catalog/datasets/100089/records?select=pegel&limit=1&pretty=false&timezone=UTC&order_by=record_timestamp%20DESC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
try:
    d['records'][0]['record']['fields']['pegel']
except NameError:
    print('level not defined')
    levelData['actualValue'] = 0
    levelData['lastUpdate'] = None
else:
    levelData['actualValue'] = d['records'][0]['record']['fields']['pegel'] - lastAvg
    levelData['lastUpdate'] = d['records'][0]['record']['timestamp']

# Weekly data
levelData['chart'] = {}
levelData['chart']['week'] = []
url = 'https://data.bs.ch/api/v2/catalog/datasets/100089/records?select=avg(pegel)%20as%20pegel&where=record_timestamp%3E%3Dnow(days%3D-7)&group_by=range(record_timestamp%2C%206%20hour)%20as%20time&limit=900&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldT = ''
for e in d['records']:
    try:
        e['record']['fields']['pegel']
    except NameError:
        levelData['chart']['week'].append(oldT | 0)
    else:
        levelData['chart']['week'].append(e['record']['fields']['pegel'])
        oldT = e['record']['fields']['pegel']

# Monthly data
levelData['chart']['month'] = []
url = 'https://data.bs.ch/api/v2/catalog/datasets/100089/records?select=avg(pegel)%20as%20pegel&where=record_timestamp%3E%3Dnow(days%3D-30)&group_by=range(record_timestamp,2days)%20as%20time&limit=900&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldT = ''
for e in d['records']:
    try:
        e['record']['fields']['pegel']
    except NameError:
        levelData['chart']['month'].append(oldT | 0)
    else:
        levelData['chart']['month'].append(e['record']['fields']['pegel'])
        oldT = e['record']['fields']['pegel']

updateJsonFile( 'data/data/levelData.json', levelData)


# Quality data
qualityData = {}

qualityData['quality'] = 2

# Global radiation
# Weekly data
globalRadiationData = {}
globalRadiationData['measure'] = 'globalRadiation'
globalRadiationData['chart'] = {}
globalRadiationData['chart']['week'] = []
url = 'https://data.bs.ch/api/v2/catalog/datasets/100254/records?select=gre000d0%20as%20globalRadiation&limit=7&pretty=false&timezone=UTC&order_by=date%20DESC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldD = ''
for e in d['records']:
    try:
        e['record']['fields']['globalRadiation']
    except NameError:
        globalRadiationData['chart']['week'].append(oldD | 0)
    else:
        globalRadiationData['chart']['week'].append(e['record']['fields']['globalRadiation'])
        oldD = e['record']['fields']['globalRadiation']

qualityData['lastUpdate'] = d['records'][0]['record']['timestamp']

globalRadiationLast72h = globalRadiationData['chart']['week'][0] + globalRadiationData['chart']['week'][1] + globalRadiationData['chart']['week'][2]
globalRadiationLast48h = globalRadiationData['chart']['week'][0] + globalRadiationData['chart']['week'][1]

# Monthly data
globalRadiationData['chart']['month'] = []
url = 'https://data.bs.ch/api/v2/catalog/datasets/100254/records?select=avg(gre000d0)%20as%20globalRadiation&order_by=date%20DESC&group_by=range(date,2days)%20as%20date&limit=15&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldD = ''
for e in d['records']:
    try:
        e['record']['fields']['globalRadiation']
    except NameError:
        globalRadiationData['chart']['month'].append(oldD | 0)
    else:
        globalRadiationData['chart']['month'].append(e['record']['fields']['globalRadiation'])
        oldD = e['record']['fields']['globalRadiation']

qualityData['data'] = []
qualityData['data'].append(globalRadiationData)


# Rain
# Weekly data
rainData = {}
rainData['measure'] = 'rain'
rainData['chart'] = {}
rainData['chart']['week'] = []
url = "https://data.bs.ch/api/v2/catalog/datasets/100009/records?select=max(meta_rain24h_sum)%20as%20rain&where=name_original=\"034001AF\"&limit=7&pretty=false&timezone=UTC&order_by=date%20DESC&group_by=date_format(dates_max_date, 'yyyyMMdd') as date"
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldD = ''
for e in d['records']:
    try:
        e['record']['fields']['rain']
    except NameError:
        rainData['chart']['week'].append(oldD | 0)
    else:
        rainData['chart']['week'].append(e['record']['fields']['rain'])
        oldD = e['record']['fields']['rain']

maxRainLast72h = rainData['chart']['week'][0]
maxRainLast48h = maxRainLast72h
if rainData['chart']['week'][1] > maxRainLast72h:
    maxRainLast72h = rainData['chart']['week'][1]
if rainData['chart']['week'][2] > maxRainLast72h:
    maxRainLast72h = rainData['chart']['week'][2]
if rainData['chart']['week'][1] > maxRainLast48h:
    maxRainLast48h = rainData['chart']['week'][1]
if rainData['chart']['week'][2] > maxRainLast48h:
    maxRainLast48h = rainData['chart']['week'][2]

# Monthly data
rainData['chart']['month'] = []
url = 'https://data.bs.ch/api/v2/catalog/datasets/100009/records?select=avg(meta_rain24h_sum)%20as%20rain&where=name_original=\"034001AF\"&limit=15&pretty=false&timezone=UTC&order_by=date%20DESC&group_by=range(dates_max_date,2days) as date'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldD = ''
for e in d['records']:
    try:
        e['record']['fields']['rain']
    except NameError:
        rainData['chart']['month'].append(oldD | 0)
    else:
        rainData['chart']['month'].append(e['record']['fields']['rain'])
        oldD = e['record']['fields']['rain']

qualityData['data'].append(rainData)

# Quality value
dailyRainTreshold = 2.5
dailyRadiationTreshold = 200

print(f'dailyRainTreshold: {dailyRainTreshold}')
print(f'dailyRadiationTreshold: {dailyRadiationTreshold}')
print(f'maxRainLast72h: {maxRainLast72h}')
print(f'maxRainLast48h: {maxRainLast48h}')
print(f'globalRadiationLast72h: {globalRadiationLast72h}')
print(f'globalRadiationLast48h: {globalRadiationLast48h}')

if maxRainLast72h < dailyRainTreshold and globalRadiationLast72h > ( dailyRadiationTreshold * 3 ):
    qualityData['quality'] = 3
elif maxRainLast48h < dailyRainTreshold and globalRadiationLast48h > ( dailyRadiationTreshold * 2 ):
    qualityData['quality'] = 2
else:
    qualityData['quality'] = 1

updateJsonFile( 'data/data/qualityData.json', qualityData)

