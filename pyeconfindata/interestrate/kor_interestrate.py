"""
:::: 코드 ::::
CD: 4000
국고채(1년): 3006
국고채(3년): 3000
국고채(5년): 3007
국고채(10년): 3013
국고채(20년): 3014
국고채(30년): 3017
국고채(50년): 3018
회사차(무보증3년) AA-: 3009
회사채(무보증3년) BBB-: 3010
"""
#TODO : 6개까지 밖에 못가져 오는 문제 해결

code_map = {
        'CD91' : 4000,
        '1Y':3006,
        '3Y':3000,
        '5Y':3007,
        '10Y':3013,
        '20Y':3014,
        '30Y':3017,
        '50Y':3018,
        '3Y_AA-':3009,
        '3Y_BBB-':3010
        }
import requests

def kor_yield_historical_kofia(target):
    codes = [code_map.get(t) for t in target]

    query = build_query('20150123', '20170120', codes)
    res = requests.post("http://www.kofiabond.or.kr/proframeWeb/XMLSERVICES/", data=query)
    df = toDf(res.text, target)
    return df

def build_query(start_date, end_date, codes):
    query = '<?xml version="1.0" encoding="utf-8"?><message>' \
            + '<proframeHeader><pfmAppName>BIS-KOFIABOND</pfmAppName>' \
            + '<pfmSvcName>BISLastAskPrcROPSrchSO</pfmSvcName><pfmFnName>listTrm</pfmFnName>' \
            + '</proframeHeader>  <systemHeader></systemHeader><BISComDspDatDTO>' \
            + '<val1>DD</val1>'
    # appending start and end dates
    query += '<val2>{}</val2>'.format(start_date)
    query += '<val3>{}</val3>'.format(end_date)
    query += '<val4>1530</val4>'

    index = 5
    for code in codes:
        query += '<val{}>{}</val{}>'.format(index, code, index)
        index += 1

    query += '</BISComDspDatDTO></message>'
    return query

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse
from lxml import etree
import pandas as pd

def toDf(xmlstring, headers):
    root = ET.fromstring(xmlstring)
    dates = []
    retDict = {}

    for h in headers:
        retDict[h] = []

    skip_index = 1
    for data in root.iter('BISComDspDatDTO'):
        if skip_index <= 2:
            skip_index += 1
            continue

        dates.append(data.find('val1').text)
        index = 2
        for h in headers:
            retDict[h].append(data.find('val{}'.format(index)).text)
            index += 1

    return pd.DataFrame(retDict, index=dates).reindex_axis(headers, axis=1)
