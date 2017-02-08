import pyeconfindata.isource as source
import quandl

class QuandlSource(source.ISource):
    def __init__(self, authtoken):
        self.authtoken = authtoken

    def get_data(self, query, post_action = None):
        data = quandl.get(query.target, authtoken = self.authtoken,
                   start_date = query.start_date, end_date = query.end_date)

        if post_action != None:
            return post_action(data)

        return data
