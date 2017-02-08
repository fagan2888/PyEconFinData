import pandas as pd

import pyeconfindata.source.quandl as quandlsource
from pyeconfindata import MiniMock


def us_treasury_historical_quandl(source: quandlsource.QuandlSource, start_date, end_date, tenors = None) -> pd.DataFrame:
    all_tenors = ["M01", "M03", "M06", "Y01", "Y02", "Y03",
                  "Y05", "Y07", "Y10", "Y20", "Y30"]

    target_code = ["FED/RIFLGFCM01_N_B",
              "FED/RIFLGFCM03_N_B",
              "FED/RIFLGFCM06_N_B",
              "FED/RIFLGFCY01_N_B",
              "FED/RIFLGFCY02_N_B",
              "FED/RIFLGFCY03_N_B",
              "FED/RIFLGFCY05_N_B",
              "FED/RIFLGFCY07_N_B",
              "FED/RIFLGFCY10_N_B",
              "FED/RIFLGFCY20_N_B",
              "FED/RIFLGFCY30_N_B"]

    target_dict = dict(zip(all_tenors, target_code))

    if tenors == None:
        tenors = all_tenors

    target = [target_dict[t] for t in tenors]
    query = MiniMock(target= target, start_date= start_date, end_date= end_date)
    data = source.get_data(query)
    cols = ["FED/RIFLGFCM01_N_B - Value",
            "FED/RIFLGFCM03_N_B - Value",
            "FED/RIFLGFCM06_N_B - Value",
            "FED/RIFLGFCY01_N_B - Value",
            "FED/RIFLGFCY02_N_B - Value",
            "FED/RIFLGFCY03_N_B - Value",
            "FED/RIFLGFCY05_N_B - Value",
            "FED/RIFLGFCY07_N_B - Value",
            "FED/RIFLGFCY10_N_B - Value",
            "FED/RIFLGFCY20_N_B - Value",
            "FED/RIFLGFCY30_N_B - Value"]

    col_dict = dict(zip(cols, all_tenors))
    data = data.rename(columns=col_dict)
    return data