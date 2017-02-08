import unittest
import pyeconfindata.querybuilder as qb


class TestKosisQueryBuilder(unittest.TestCase):
    def test_buildWithBuilderPattern(self):
        builder = qb.KosisQueryBuilder('testkey')
        builder.with_itemid('13103112548999+') \
        .with_option1('13102112548CSI_CODE.FME+') \
        .with_option2('13102112548CSI_PART.99988+') \
        .with_format('json') \
        .with_frequency(qb.Frequency.MONTHLY) \
        .with_start_date('201609') \
        .with_end_date('201612') \
        .with_load_type(qb.LoadType.TIME_SERIES) \
        .with_orgid('301') \
        .with_tableid('DT_040Y002')

        query = builder.build()
        print(query)
        self.assertEqual("http://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=testkey&orgId=301&tblId=DT_040Y002&itmId=13103112548999+&loadGubun=1&prdSe=M&format=json&jsonVD=Y&objL1=13102112548CSI_CODE.FME+&startPrdDe=201609&endPrdDe=201612&objL2=13102112548CSI_PART.99988+", query)

    def test_buildWithKeywordArg(self):
        query_dict = {
            'itemid':'13103112548999+',
            'option1':'13102112548CSI_CODE.FME+',
            'option2':'13102112548CSI_PART.99988+',
            'format':'json',
            'frequency': qb.Frequency.MONTHLY,
            'start_date':'201609',
            'end_date':'201612',
            'load_type':qb.LoadType.TIME_SERIES,
            'orgid': '301',
            'tableid':'DT_040Y002'
        }

        builder = qb.KosisQueryBuilder('testkey', **query_dict)
        query = builder.build()
        print(query)
        self.assertEqual("http://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=testkey&orgId=301&tblId=DT_040Y002&itmId=13103112548999+&loadGubun=1&prdSe=M&format=json&jsonVD=Y&objL1=13102112548CSI_CODE.FME+&startPrdDe=201609&endPrdDe=201612&objL2=13102112548CSI_PART.99988+", query)

if __name__ == '__main__':
    unittest.main()