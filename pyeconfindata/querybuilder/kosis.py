from pyeconfindata.iquerybuilder import IQueryBuilder
from enum import Enum

class LoadType(Enum):
    TIME_SERIES = 1
    CROSS_SECTIONAL =2

class Frequency(Enum):
    DAILY = 'D'
    WEEKLY = 'W'
    MONTHLY = 'M'
    QUARTERLY = 'Q'
    HALPYEARLY = 'H'
    YEARLY = 'Y'

class KosisQueryBuilder(IQueryBuilder):

    required_fields_name \
        = ['orgid', 'itemid', 'tableid', 'format', 'load_type',
        'data_frequency', 'option1']

    def __init__(self, apikey, **kwargs):
        self.__query_base = "http://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList"
        self.__apikey = apikey
        self._keyarg_mapping(kwargs)

### 필수 필드
    def with_orgid(self, orgid):
        self.orgid = orgid
        return self

    def with_itemid(self, itemid):
        self.itemid = itemid
        return self

    def with_tableid(self, tableid):
        self.tableid = tableid
        return self

    def with_format(self, format):
        self.format = format
        return self

    def with_load_type(self, load_type:LoadType):
        self.load_type = load_type
        return self

    def with_frequency(self, frequency:Frequency):
        self.frequency = frequency
        return self

    def with_start_date(self, start_date):
        self.start_date = start_date
        return self

    def with_end_date(self, end_date):
        self.end_date = end_date
        return self

    def with_data_count(self, data_count):
        self.data_count = data_count
        return self

    def with_option1(self, option1):
        self.option1 = option1
        return self
## 선택필드
    def with_option2(self, option):
        self.option2 = option
        return self
    def with_option3(self, option):
        self.option3 = option
        return self
    def with_option4(self, option):
        self.option4 = option
        return self
    def with_option5(self, option):
        self.option5 = option
        return self
    def with_option6(self, option):
        self.option6 = option
        return self
    def with_option7(self, option):
        self.option7 = option
        return self
    def with_option8(self, option):
        self.option8 = option
        return self
   
    
    def build(self):
        query = self.__query_base
        query += self._query_block('apiKey', self.__apikey)
        query += self._query_block('orgId', self.orgid)
        query += self._query_block('tblId', self.tableid)
        query += self._query_block('itmId', self.itemid)
        query += self._query_block('loadGubun', self.load_type.value)
        query += self._query_block('prdSe', self.frequency.value)
        query += self._query_block('format', self.format)
        if self.format == 'json':
            query += self._query_block('jsonVD', 'Y')
        query += self._query_block('objL1', self.option1)

        if self._check_date_or_count():
            if self.start_date and self.end_date:
                query += self._query_block('startPrdDe', self.start_date)
                query += self._query_block('endPrdDe', self.end_date)
            else:
                query += self._query_block('newEstPrdCnt', self.data_count)
        else:
            query += self._query_block('newEstPrdCnt', 10)

        query += self._build_options()
        return query

    def _query_block(self, key, value):
        return "&{}={}".format(key, value)

    def _keyarg_mapping(self, kwargs):
        for key in kwargs.keys():
            setattr(self, format(key), kwargs[key])

    def _check_requried_field(self):

        false_state = False
        for field_name in self.required_fields_name:
            if not hasattr(self, field_name):
                print("{} missing".format(field_name))
                false_state = True

        if false_state:
            return False
        return True

    def _check_date_or_count(self):
        if not self.start_date and not self.end_date and not self.data_count:
            print("date or data count must be specified")
            return False
        return True

    def _build_options(self):
        ret_val = ''
        for i in range(2, 9):
            field_name = 'option{}'.format(i)
            if(hasattr(self, field_name)):
                ret_val += self._query_block('objL{}'.format(i), getattr(self, field_name))

        return ret_val