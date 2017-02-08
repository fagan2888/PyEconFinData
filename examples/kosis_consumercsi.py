from pyeconfindata.querybuilder import (
    KosisQueryBuilder, Frequency, LoadType)
from pyeconfindata.source import KosisSource
import json

query_dict = {
    'orgid': '301',
    'tableid': 'DT_040Y002',
    'itemid': '13103112548999+',
    'frequency': Frequency.MONTHLY,
    'load_type': LoadType.TIME_SERIES,
    'format': 'json',
    'option1': '13102112548CSI_CODE.FME+',
    'option2': '13102112548CSI_PART.99988+',
    'start_date': '201609',
    'end_date': '201612'
}

settings = open("./data/kosis_settings.json").read()
auth_key = json.loads(settings)['authKey']

builder = KosisQueryBuilder(auth_key, **query_dict)

kosis_source = KosisSource()
data = kosis_source.get_data(builder)
print(data)
