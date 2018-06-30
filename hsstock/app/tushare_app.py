# -*- coding: UTF-8 -*-
#import tushare as ts
import logging
import time
import sqlalchemy as sa
import pandas as pd

from apscheduler.schedulers.blocking import BlockingScheduler

from hsstock.service.store_service import StoreService
from hsstock.utils.app_logging import setup_logging
from hsstock.utils.date_util import DateUtil
import hsstock.utils.tick_deco  as tick
from hsstock.service.tushare_service import TUShare_service

sched = BlockingScheduler()

@tick.clock()
def change_df_filed_type(df,fields,type,old,new):
    """
    inefficient
    :param df:
    :param fields:
    :param old:
    :param new:
    :return:
    """
    # try:
    #     for field in fields:
    #         index =  0
    #         for item in df[field].values:
    #             if df[field][index] == old:
    #                 df[field][index] = new
    #             else:
    #                 df[field][index] = type((df[field][index]))
    #             index += 1
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # finally:
    #     print(df)
    return df

@sched.scheduled_job('interval',seconds=10)
def timed_job():
    storeservice = StoreService()
    logging.info("fetch latest_news, starting")
    df = ts.get_latest_news()
    table = 'ts2_latest_news'
    storeservice.insert_many(table, df)
    logging.info("fetch latest_news, end")


def main():
    # fetch industry catalog
    storeservice = StoreService()
    ts = TUShare_service()

    # logging.info("fetch industry catalog, starting")
    # df = ts.get_industry_classified()
    # table='ts2_industry_classified'
    # storeservice.insert_many(table, df)
    # logging.info("fetch industry catalog, end")
    #
    # logging.info("fetch concept_classified, starting")
    # df = ts.get_concept_classified()
    # table = 'ts2_concept_classified'
    # storeservice.insert_many(table, df)
    # logging.info("fetch concept_classified, end")
    #
    # logging.info("fetch area_classified, starting")
    # df = ts.get_area_classified()
    # table = 'ts2_area_classified'
    # storeservice.insert_many(table, df)
    # logging.info("fetch area_classified, end")
    #
    # logging.info("fetch sme_classified, starting")
    # df = ts.get_sme_classified()
    # table = 'ts2_sme_classified'
    # storeservice.insert_many(table, df)
    # logging.info("fetch sme_classified, end")
    #
    # logging.info("fetch gem_classified, starting")
    # df = ts.get_gem_classified()
    # table = 'ts2_gem_classified'
    # storeservice.insert_many(table, df)
    # logging.info("fetch gem_classified, end")
    #
    # logging.info("fetch st_classified, starting")
    # df = ts.get_st_classified()
    # table = 'ts2_st_classified'
    # storeservice.insert_many(table, df)
    # logging.info("fetch st_classified, end")
    #
    # logging.info("fetch hs300s, starting")
    # df = ts.get_hs300s()
    # table = 'ts2_hs300s'
    # storeservice.insert_many(table, df)
    # logging.info("fetch hs300s, end")
    #
    # logging.info("fetch sz50s, starting")
    # df = ts.get_sz50s()
    # table = 'ts2_sz50s'
    # storeservice.insert_many(table, df)
    # logging.info("fetch sz50s, end")
    #
    # logging.info("fetch zz500s, starting")
    # df = ts.get_zz500s()
    # table = 'ts2_zz500s'
    # storeservice.insert_many(table, df)
    # logging.info("fetch zz500s, end")
    #
    # try:
    #     logging.info("Forbidden,fetch terminated, starting")
    #     df = ts.get_terminated()
    #     table = 'ts2_terminated'
    #     if df != None:
    #         storeservice.insert_many(table, df)
    #     logging.info("fetch terminated, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    #
    # try:
    #     logging.info("fetch suspended, starting")
    #     df = ts.get_suspended()
    #     table = 'ts2_suspended'
    #     if df != None:
    #         storeservice.insert_many(table, df)
    #     logging.info("fetch suspended, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    #
    # logging.info("fetch stock_basics, starting")
    # df = ts.get_stock_basics()
    # table = 'ts2_stock_basics'
    # # replace will fail
    # storeservice.insert_many(table, df, 'append', True,'code')
    # logging.info("fetch stock_basics, end")
    #
    # try:
    #     logging.info("fetch report_data, starting")
    #     for year in range(2010,2019):
    #         for quarter in range(1,5):
    #             df = ts.get_report_data(year,quarter)
    #             df['year'] = year
    #             df['quarter'] = quarter
    #             table = 'ts2_report_data'
    #             storeservice.insert_many(table, df)
    #     logging.info("fetch report_data, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')
    #
    # try:
    #     logging.info("fetch get_profit_data, starting")
    #     for year in range(2010, 2019):
    #         for quarter in range(1, 5):
    #             df = ts.get_profit_data(year, quarter)
    #             df['year'] = year
    #             df['quarter'] = quarter
    #             table = 'ts2_profit_data'
    #             storeservice.insert_many(table, df)
    #     logging.info("fetch get_profit_data, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')
    #
    # try:
    #     logging.info("fetch operation_data, starting")
    #     for year in range(2010, 2019):
    #         for quarter in range(1, 5):
    #             df = ts.get_operation_data(year, quarter)
    #             df['year'] = year
    #             df['quarter'] = quarter
    #             table = 'ts2_operation_data'
    #             storeservice.insert_many(table, df)
    #     logging.info("fetch operation_data, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')
    #
    # try:
    #     logging.info("fetch growth_data, starting")
    #     for year in range(2010, 2019):
    #         for quarter in range(1, 5):
    #             df = ts.get_growth_data(year, quarter)
    #             df['year'] = year
    #             df['quarter'] = quarter
    #             table = 'ts2_growth_data'
    #             storeservice.insert_many(table, df)
    #     logging.info("fetch growth_data, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')
    #
    # try:
    #     logging.info("fetch debtpaying_data, starting")
    #     for year in range(2010, 2019):
    #         for quarter in range(1, 5):
    #             df = ts.get_debtpaying_data(year, quarter)
    #             df['year'] = year
    #             df['quarter'] = quarter
    #             table = 'ts2_debtpaying_data'
    #             #change_df_filed_type(df,["currentratio","quickratio","cashration","icratio","sheqratio","adratio"],float,'--',0.0)
    #             storeservice.insert_many(table, df)
    #     logging.info("fetch debtpaying_data, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')
    #
    # try:
    #     logging.info("fetch cashflow_data, starting")
    #     for year in range(2010, 2019):
    #         for quarter in range(1, 5):
    #             df = ts.get_cashflow_data(year, quarter)
    #             df['year'] = year
    #             df['quarter'] = quarter
    #             table = 'ts2_cashflow_data'
    #             storeservice.insert_many(table, df)
    #     logging.info("fetch cashflow_data, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')
    #
    # logging.info("fetch deposit_rate, starting")
    # df = ts.get_deposit_rate()
    # table = 'ts2_deposit_rate'
    # storeservice.insert_many(table, df)
    # logging.info("fetch deposit_rate, end")
    #
    # logging.info("fetch load_rate, starting")
    # df = ts.get_loan_rate()
    # table = 'ts2_loan_rate'
    # storeservice.insert_many(table, df)
    # logging.info("fetch loan_rate, end")
    #
    # logging.info("fetch loarrr, starting")
    # df = ts.get_rrr()
    # table = 'ts2_rrr'
    # storeservice.insert_many(table, df)
    # logging.info("fetch rrr, end")
    #
    # logging.info("fetch money_supply, starting")
    # df = ts.get_money_supply()
    # table = 'ts2_money_supply'
    # storeservice.insert_many(table, df)
    # logging.info("fetch money_supply, end")
    #
    # logging.info("fetch money_supply_bal, starting")
    # df = ts.get_money_supply_bal()
    # table = 'ts2_money_supply_bal'
    # storeservice.insert_many(table, df)
    # logging.info("fetch money_supply_bal, end")
    #
    # logging.info("fetch gdp_year, starting")
    # df = ts.get_gdp_year()
    # table = 'ts2_gdp_year'
    # storeservice.insert_many(table, df)
    # logging.info("fetch gdp_year, end")
    #
    # logging.info("fetch gdp_quarter, starting")
    # df = ts.get_gdp_quarter()
    # table = 'ts2_gdp_quarter'
    # storeservice.insert_many(table, df)
    # logging.info("fetch gdp_quarter, end")
    #
    # logging.info("fetch gdp_for, starting")
    # df = ts.get_gdp_for()
    # table = 'ts2_gdp_for'
    # storeservice.insert_many(table, df)
    # logging.info("fetch gdp_for, end")
    #
    # logging.info("fetch gdp_pull, starting")
    # df = ts.get_gdp_pull()
    # table = 'ts2_gdp_pull'
    # storeservice.insert_many(table, df)
    # logging.info("fetch gdp_pull, end")
    #
    # logging.info("fetch gdp_contrib, starting")
    # df = ts.get_gdp_contrib()
    # table = 'ts2_gdp_contrib'
    # storeservice.insert_many(table, df)
    # logging.info("fetch gdp_contrib, end")
    #
    # logging.info("fetch cpi, starting")
    # df = ts.get_cpi()
    # table = 'ts2_cpi'
    # storeservice.insert_many(table, df)
    # logging.info("fetch cpi, end")
    #
    # logging.info("fetch ppi, starting")
    # df = ts.get_ppi()
    # table = 'ts2_ppi'
    # storeservice.insert_many(table, df)
    # logging.info("fetch ppi, end")
    #
    # logging.info("fetch latest_news, starting")
    # df = ts.get_latest_news()
    # table = 'ts2_latest_news'
    # storeservice.insert_many(table, df)
    # logging.info("fetch latest_news, end")


    # try:
    #     logging.info("fetch profit_data, starting")
    #     for year in range(2010, 2019):
    #         df = ts.profit_data(year, top=100)
    #         df['year'] = year
    #         table = 'ts2_pre_profit_data'
    #         storeservice.insert_many(table, df)
    #     logging.info("fetch profit_data, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')

    # try:
    #     logging.info("fetch forecast_data, starting")
    #     for year in range(2010, 2019):
    #         for quarter in range(1,5):
    #             df = ts.forecast_data(year, quarter)
    #             df['year'] = year
    #             df['quarter'] = quarter
    #             table = 'ts2_forecast_data'
    #             storeservice.insert_many(table, df)
    #     logging.info("fetch forecast_data, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')


    # logging.info("fetch xsg_data, starting")
    # df = ts.xsg_data()
    # table = 'ts2_xsg_data'
    # storeservice.insert_many(table, df)
    # logging.info("fetch xsg_data, end")
    #
    # try:
    #     logging.info("fetch fund_holdings, starting")
    #     for year in range(2010, 2019):
    #         for quarter in range(1,5):
    #             df = ts.fund_holdings(year, quarter)
    #             df['year'] = year
    #             df['quarter'] = quarter
    #             table = 'ts2_fund_holdings'
    #             storeservice.insert_many(table, df)
    #     logging.info("fetch fund_holdings, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')
    #
    # logging.info("fetch new_stocks, starting")
    # df = ts.new_stocks()
    # table = 'ts2_new_stocks'
    # storeservice.insert_many(table, df)
    # logging.info("fetch new_stocks, end")
    #
    # try:
    #     logging.info("fetch hist_data, three years, starting")
    #     code = '600848'
    #     df = ts.get_hist_data(code)
    #     df = df.reset_index(level=[0])
    #     df['code'] = code
    #     table = 'ts2_hist_data'
    #     storeservice.insert_many(table, df)
    #     logging.info("fetch hist_data, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')
    #
    # try:
    #     logging.info("fetch h_data, three years,hfq,None,qfq starting")
    #     code = '600848'
    #     df = ts.get_h_data(code,autype='hfq',end='2018-06-28',start='2015-07-01')
    #     df['code'] = code
    #     df = df.reset_index(level=[0])
    #     table = 'ts2_h_data'
    #     storeservice.insert_many(table, df)
    #
    #     df = ts.get_h_data(code, autype='hfq', end='2015-06-30', start='2012-07-01')
    #     df['code'] = code
    #     df = df.reset_index(level=[0])
    #     table = 'ts2_h_data'
    #     storeservice.insert_many(table, df)
    #
    #     logging.info("fetch h_data, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')
    #
    #
    # try:
    #     logging.info("fetch today_all,  starting")
    #     df = ts.get_today_all()
    #     date = time.strftime('%Y-%m-%d', time.localtime())
    #     df['date'] = date
    #     df = df.reset_index(level=[0])
    #     table = 'ts2_today_all'
    #     storeservice.insert_many(table, df)
    #     logging.info("fetch today_all, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')
    #
    # try:
    #     logging.info("fetch tick_data,  starting")
    #
    #     code = '002049'
    #     df = ts.get_tick_data(code, DateUtil.getDatetimeYesterdayStr( DateUtil.getDatetimeToday()))
    #     df['date'] = DateUtil.getTodayStr()
    #     df['code'] = code
    #     df = df.reset_index(level=[0])
    #     del df['index']
    #     storeservice.insert_many('ts2_tick_data', df)
    #
    #     logging.info("fetch tick_data, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')
    #
    # try:
    #     logging.info("fetch realtime_quotes,  starting")
    #
    #     df = ts.get_realtime_quotes(['002049','002624'])
    #     df['date'] = DateUtil.getTodayStr()
    #     df = df.reset_index(level=[0])
    #     del df['index']
    #     table = 'ts2_realtime_quotes'
    #     storeservice.insert_many(table, df)
    #
    #     df = ts.get_realtime_quotes(['sh', 'sz', 'hs300', 'sz50', 'zxb', 'cyb'])
    #     df['date'] = DateUtil.getTodayStr()
    #     df = df.reset_index(level=[0])
    #     del df['index']
    #     table = 'ts2_realtime_quotes'
    #     storeservice.insert_many(table, df)
    #
    #     logging.info("fetch realtime_quotes, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')
    #
    # try:
    #     logging.info("fetch today_ticks,  starting")
    #
    #     code = '601333'
    #     df = ts.get_today_ticks(code)
    #     df['date'] = DateUtil.getTodayStr()
    #     df['code'] = code
    #     df = df.reset_index(level=[0])
    #     del df['index']
    #     table = 'ts2_today_ticks'
    #     storeservice.insert_many(table, df)
    #
    #     logging.info("fetch today_ticks, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')
    #
    # try:
    #     logging.info("fetch index,  starting")
    #
    #     df = ts.get_index()
    #     df['date'] = DateUtil.getTodayStr()
    #     df = df.reset_index(level=[0])
    #     del df['index']
    #     table = 'ts2_index'
    #     storeservice.insert_many(table, df)
    #
    #     logging.info("fetch index, end")
    # except IOError as err:
    #     logging.error("OS|error: {0}".format(err))
    # else:
    #     print('success')

    try:
        logging.info("fetch sina_dd,  starting")

        df = ts.get_sina_dd('000063',date='2018-06-27',vol=400)
        df['date'] = DateUtil.getTodayStr()
        table = 'ts2_sina_dd'
        storeservice.insert_many(table, df)

        df = ts.get_sina_dd('000063', date='2018-06-25',vol=400)
        df['date'] = '2018-06-25'
        table = 'ts2_sina_dd'
        storeservice.insert_many(table, df)

        logging.info("fetch sina_dd, end")
    except IOError as err:
        logging.error("OS|error: {0}".format(err))
    else:
        print('success')


    try:
        logging.info("test change field type,  starting")

        df = pd.DataFrame({'A': ['-','1.0'],'B':['-','-']})
        #df['A'][0] = 1
        df = change_df_filed_type(df,['A','B'], float,'-',0.0)
        table='aaaaa'
        storeservice.insert_many(table, df)
        logging.info("test change field type, end")
    except IOError as err:
        logging.error("OS|error: {0}".format(err))
    else:
        print('success')



if __name__ == "__main__":
    setup_logging()
    main()
    #sched.start()

