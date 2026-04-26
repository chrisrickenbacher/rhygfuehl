import requests
import json
import os
import time,datetime

def updateJsonFile( path, data ):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Actual temperature
waterData = {}
url = 'https://data.bs.ch/api/v2/catalog/datasets/100046/records?order_by=endezeitpunkt%20DESC&limit=2&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

if d['records'][0]['record']['fields']['rus_w_o_s3_te'] is not None:
    waterData['actualValue'] = d['records'][0]['record']['fields']['rus_w_o_s3_te']
    waterData['lastUpdate'] = d['records'][0]['record']['fields']['endezeitpunkt']
else:
    print('newest temp is null we take next older one')
    if d['records'][1]['record']['fields']['rus_w_o_s3_te'] is not None:
        waterData['actualValue'] = d['records'][1]['record']['fields']['rus_w_o_s3_te']
        waterData['lastUpdate'] = d['records'][1]['record']['fields']['endezeitpunkt']
    else: 
        print('no valid temp')
        waterData['actualValue'] = 0
        waterData['lastUpdate'] = None

# Weekly data
waterData['chart'] = {}
waterData['chart']['week'] = []
url = 'https://data.bs.ch/api/v2/catalog/datasets/100046/records?select=avg(rus_w_o_s3_te)%20as%20temp&where=endezeitpunkt%3E%3Dnow(days%3D-7)&group_by=range(endezeitpunkt%2C%2012%20hour)%20as%20time&limit=900&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldT = 0
for e in d['records']:
    if  e['record']['fields']['temp'] is not None:
        waterData['chart']['week'].append(e['record']['fields']['temp'])
        oldT = e['record']['fields']['temp']
    else:
        waterData['chart']['week'].append(oldT)

# Monthly data
waterData['chart']['month'] = []
url = 'https://data.bs.ch/api/v2/catalog/datasets/100046/records?select=avg(rus_w_o_s3_te)%20as%20temp&where=endezeitpunkt%3E%3Dnow(days%3D-30)&group_by=range(endezeitpunkt,2days)%20as%20time&limit=900&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldT = 0
for e in d['records']:
    if e['record']['fields']['temp'] is not None:
        waterData['chart']['month'].append(e['record']['fields']['temp'])
        oldT = e['record']['fields']['temp']
    else:
        waterData['chart']['month'].append(oldT)

updateJsonFile( 'data/data/waterData.json', waterData)

# Air temperature
airStationId = '034003A7' # Rheinpromenade 2
airData = {}
url = f'https://data.bs.ch/api/v2/catalog/datasets/100009/records?select=dates_max_date%20as%20date%2C%20meta_airtemp%20as%20temp&where=name_original="{airStationId}"&limit=1&pretty=false&timezone=UTC&order_by=dates_max_date%20DESC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

try:
    d['records'][0]['record']['fields']['temp']
except (KeyError, IndexError):
    print('air temp not defined')
    try: 
        airData['actualValue'] = d['records'][1]['record']['fields']['temp']
        airData['lastUpdate'] = d['records'][1]['record']['fields']['date']
    except (KeyError, IndexError):
        print('last air temp not defined')
        airData['actualValue'] = 0
        airData['lastUpdate'] = None
else:
    airData['actualValue'] = d['records'][0]['record']['fields']['temp']
    airData['lastUpdate'] = d['records'][0]['record']['fields']['date']

# Weekly data
airData['chart'] = {}
airData['chart']['week'] = []
url = f'https://data.bs.ch/api/v2/catalog/datasets/100009/records?select=avg(meta_airtemp)%20as%20temp&where=name_original="{airStationId}"%20and%20dates_max_date%3E%3Dnow(days%3D-7)&group_by=range(dates_max_date%2C%206%20hour)%20as%20time&limit=900&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldT = 0
for e in d['records']:
    try:
        val = e['record']['fields']['temp']
        if val is not None:
            airData['chart']['week'].append(val)
            oldT = val
        else:
            airData['chart']['week'].append(oldT)
    except KeyError:
        airData['chart']['week'].append(oldT)

# Monthly data
airData['chart']['month'] = []
url = f'https://data.bs.ch/api/v2/catalog/datasets/100009/records?select=avg(meta_airtemp)%20as%20temp&where=name_original="{airStationId}"%20and%20dates_max_date%3E%3Dnow(days%3D-30)&group_by=range(dates_max_date,2days)%20as%20time&limit=900&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldT = 0
for e in d['records']:
    try:
        val = e['record']['fields']['temp']
        if val is not None:
            airData['chart']['month'].append(val)
            oldT = val
        else:
            airData['chart']['month'].append(oldT)
    except KeyError:
        airData['chart']['month'].append(oldT)

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

url = 'https://data.bs.ch/api/v2/catalog/datasets/100089/records?select=pegel&limit=1&pretty=false&timezone=UTC&order_by=timestamp%20DESC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
try:
    levelData['actualValue'] = d['records'][0]['record']['fields']['pegel'] - lastAvg
    levelData['lastUpdate'] = d['records'][0]['record']['timestamp']
except (KeyError, IndexError):
    print('level not defined')
    levelData['actualValue'] = 0
    levelData['lastUpdate'] = None

# Weekly data
levelData['chart'] = {}
levelData['chart']['week'] = []
url = 'https://data.bs.ch/api/v2/catalog/datasets/100089/records?select=avg(pegel)%20as%20pegel&where=timestamp%3E%3Dnow(days%3D-7)&group_by=range(timestamp%2C%206%20hour)%20as%20time&limit=900&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldT = 0
for e in d['records']:
    try:
        val = e['record']['fields']['pegel']
        if val is not None:
            levelData['chart']['week'].append(val)
            oldT = val
        else:
            levelData['chart']['week'].append(oldT)
    except KeyError:
        levelData['chart']['week'].append(oldT)

# Monthly data
levelData['chart']['month'] = []
url = 'https://data.bs.ch/api/v2/catalog/datasets/100089/records?select=avg(pegel)%20as%20pegel&where=timestamp%3E%3Dnow(days%3D-30)&group_by=range(timestamp,2days)%20as%20time&limit=900&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldT = 0
for e in d['records']:
    try:
        val = e['record']['fields']['pegel']
        if val is not None:
            levelData['chart']['month'].append(val)
            oldT = val
        else:
            levelData['chart']['month'].append(oldT)
    except KeyError:
        levelData['chart']['month'].append(oldT)

updateJsonFile( 'data/data/levelData.json', levelData)


# Quality data
qualityData = {}
qualityData['quality'] = 2

# Global radiation
globalRadiationData = {'measure': 'globalRadiation', 'chart': {'week': [], 'month': []}}
url = 'https://data.bs.ch/api/v2/catalog/datasets/100254/records?select=gre000d0%20as%20globalRadiation&limit=7&pretty=false&timezone=UTC&order_by=date%20DESC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldD = 0
for e in d['records']:
    try:
        val = e['record']['fields']['globalRadiation']
        if val is not None:
            globalRadiationData['chart']['week'].append(val)
            oldD = val
        else:
            globalRadiationData['chart']['week'].append(oldD)
    except KeyError:
        globalRadiationData['chart']['week'].append(oldD)

qualityData['lastUpdate'] = d['records'][0]['record']['timestamp']

# Monthly radiation
url = 'https://data.bs.ch/api/v2/catalog/datasets/100254/records?select=avg(gre000d0)%20as%20globalRadiation&order_by=date%20DESC&group_by=range(date,2days)%20as%20date&limit=15&pretty=false&timezone=UTC'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldD = 0
for e in d['records']:
    try:
        val = e['record']['fields']['globalRadiation']
        if val is not None:
            globalRadiationData['chart']['month'].append(val)
            oldD = val
        else:
            globalRadiationData['chart']['month'].append(oldD)
    except KeyError:
        globalRadiationData['chart']['month'].append(oldD)

# Rain data
rainData = {'measure': 'rain', 'chart': {'week': [], 'month': []}}
url = "https://data.bs.ch/api/v2/catalog/datasets/100009/records?select=max(meta_rain24h_sum)%20as%20rain&where=name_original=\"034001AF\"&limit=7&pretty=false&timezone=UTC&order_by=date%20DESC&group_by=date_format(dates_max_date, 'yyyyMMdd') as date"
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldD = 0
for e in d['records']:
    try:
        val = e['record']['fields']['rain']
        if val is not None:
            rainData['chart']['week'].append(val)
            oldD = val
        else:
            rainData['chart']['week'].append(oldD)
    except KeyError:
        rainData['chart']['week'].append(oldD)

# Monthly rain
url = 'https://data.bs.ch/api/v2/catalog/datasets/100009/records?select=avg(meta_rain24h_sum)%20as%20rain&where=name_original=\"034001AF\"&limit=15&pretty=false&timezone=UTC&order_by=date%20DESC&group_by=range(dates_max_date,2days) as date'
try: 
    resp = requests.get(url=url)
    d = resp.json()
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

oldD = 0
for e in d['records']:
    try:
        val = e['record']['fields']['rain']
        if val is not None:
            rainData['chart']['month'].append(val)
            oldD = val
        else:
            rainData['chart']['month'].append(oldD)
    except KeyError:
        rainData['chart']['month'].append(oldD)

# Quality calculation (using Newest at index 0)
dailyRadiationTreshold = 170
r0 = rainData['chart']['week'][0] if len(rainData['chart']['week']) > 0 else 0
r1 = rainData['chart']['week'][1] if len(rainData['chart']['week']) > 1 else 0
r2 = rainData['chart']['week'][2] if len(rainData['chart']['week']) > 2 else 0
rainImpact = (r0 * 1.0) + (r1 * 0.5) + (r2 * 0.25)

uv0 = globalRadiationData['chart']['week'][0] if len(globalRadiationData['chart']['week']) > 0 else 0
uv1 = globalRadiationData['chart']['week'][1] if len(globalRadiationData['chart']['week']) > 1 else 0
uv2 = globalRadiationData['chart']['week'][2] if len(globalRadiationData['chart']['week']) > 2 else 0
uvBonus = (uv0 + uv1 + uv2) / (3 * dailyRadiationTreshold)

# Base quality based on rain/UV
level = 1
if rainImpact < 0.5 or (r0 < 1.0 and rainImpact < 2.0 and uvBonus > 1.2):
    level = 3
elif rainImpact < 3.5 or (r0 < 2.0 and rainImpact < 5.0 and uvBonus > 1.0):
    level = 2

# Temperature-based safety caps
# < 14°C: Discouraged (Cold shock) - based on LATEST temp
# 14-18°C: Max "Good" (Fresh) - based on LATEST temp
# > 22°C (48h Avg): Max "Good" (Bacterial growth) - based on SUSTAINED heat
waterTempLatest = waterData.get('actualValue', 0)

# Calculate 48h average from the last 4 data points (each is a 12h average)
# Chart week currently has newest data at index 0
recentTemps = waterData['chart']['week'][:4]
waterTemp48hAvg = sum(recentTemps) / len(recentTemps) if recentTemps else waterTempLatest

if waterTempLatest < 14.0:
    level = 1
elif (waterTempLatest < 18.0 or waterTemp48hAvg > 22.0) and level > 2:
    level = 2

qualityData['quality'] = level

# REVERSE chart data for 'Old -> New' display
globalRadiationData['chart']['week'].reverse()
globalRadiationData['chart']['month'].reverse()
rainData['chart']['week'].reverse()
rainData['chart']['month'].reverse()

qualityData['data'] = [globalRadiationData, rainData]
updateJsonFile( 'data/data/qualityData.json', qualityData)
