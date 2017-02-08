import pyeconfindata.isource as source
import json
import requests
import pandas as pd
from pyeconfindata.querybuilder.kosis import KosisQueryBuilder

class KosisSource(source.ISource):

    def get_data(self, query:KosisQueryBuilder, post_action = None):
        url = query.build()
        res = requests.get(url)
        data = json.loads(res.content.decode())

        if post_action != None:
            return post_action(data)

        return self.data_refining(data)

    def data_refining(data):
        tmp_data = [{'Date' : d['PRD_DE'], 'Value': d['DT']} for d in data]
        return pd.DataFrame(data=tmp_data)