# -*- coding: UTF-8 -*-
import logging
import signal
import threading

from apscheduler.schedulers.blocking import BlockingScheduler

from hsstock.utils.app_logging import setup_logging
import hsstock.utils.tick_deco  as tick
from hsstock.service.tushare_service_new import TUShare_service
from hsstock.utils.date_util import DateUtil
import hsstock.tushare.stock.globals as globals

sched = BlockingScheduler()
ts = TUShare_service()
ts2 = TUShare_service()

"""
交易数据
    (ok)1:历史行情:近三年数据get_hist_data，全部数据用get_h_data
    (ok)1:复权数据:前复权，后复权，不复权，默认：前复权，不设定日期：获取近一年数据，设定日期：最好不要超过三年，获取全部数据，分年段获取，get_h_data
    (ok)N:R:实时行情：一次性获取当前所有股票行情数据 get_today_all
    (ok)1:历史分笔：当日之前的分笔数据，当天的用get_today_ticks获取，或当日18点之后，用本接口, get_tick_data
    (ok)N:R:实时分笔: 两三秒可调用一次，get_realtime_quotes(['code1','code2'])
    (ok)N:R:当日历史分笔: 交易进行中使用，get_today_ticks('601333') 列表吗？
    (ok)N:R:大盘指数行情列表: 大盘指数实时行情列表，get_index
    (ok)1:大单交易数据: 大单交易数据，来自新浪财经，默认400手，最好转换成金额（加转换功能）？
投资参考数据
    (ok)N:+R:分配预案: 季报，年报之前的送转，分红预案 profit_data
    (ok)N:+R 业绩预告：forecast_data(year,quarter)
    (ok)N:+R 限售股解禁: xsg_data(year,quarter) 
    (ok)N:+R 基金持股 fund_holding(year,quarter)
    (ok)1:新股数据 new_stocks()
    融资融券（沪市）
    融资融券（深市）
股票分类数据
    (ok)1:行业分类 get_industry_classified()
    (ok)1:概念分类 get_concept_classified()
    (ok)1:地域分类 get_area_classified()
    (ok)1:中小板分类: get_sme_classified()
    (ok)1:创业板分类 get_gem_classified()
    (ok)1:风险警示板分类 get_st_classified()
    (ok)1: 沪深300成份及权重 get_hs300s()
    (ok)1: 上证50成份股 get_sz50s()
    (ok)1: 中证500成份股 get_zz500s()
    终止上市股票列表
    暂停上市股票列表
基本面数据
    (ok?)1:股票列表: get_stock_basics()
    (ok)1:业绩报告（主表）: get_report_data(year,quarter)
    (ok)1:盈利能力: get_profit_data(year, quarter)
    (ok)1:营运能力: get_operation_data(year,quarter)
    (ok)1:成长能力: get_growth_data(year,quarter)
    (ok)1:偿债能力: get_debtpaying_data(year,quarter)
    (ok)1:现金流量: get_cashflow_data(year,quarter)
宏观经济数据
    (ok)1:存款利率: get_deposit_rate()
    (ok)1:贷款利率: get_loan_rate()
    (ok)1:存款准备金率: get_rrr()
    (ok)1:货币供应量: get_money_supply()
    (ok)1:货币供应量(年底余额): get_money_supply_bal()
    (ok)1:国内生产总值(年度): get_gdp_year()
    (ok)1:国内生产总值(季度): get_gdp_quarter()
    (ok)1:三大需求对GDP贡献: get_gdp_for()
    (ok)1:三大产业对GDP拉动: get_gdp_pull()
    (ok)1:三大产业贡献率: get_gdp_contrib()
    (ok)1:居民消费价格指数: get_cpi()
    (ok)1:工业品出厂价格指数: get_ppi()
新闻事件数据
    (ok)N+R:即时新闻: 获取即时财经新闻，类型包括国内财经、证券、外汇、期货、港股和美股等新闻信息。数据更新较快，使用过程中可用定时任务来获取。get_latest_news()
"""
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


#@sched.scheduled_job('cron',day_of_week='mon-fri',hour='16-17', minute='20-59',seconds='*/10')
@sched.scheduled_job('interval',seconds=10)
def timer_job():
    ts.get_latest_news()


#@sched.scheduled_job('cron',day_of_week='mon-sun',hour='20', minute='35-36',second='*/10')
def job_sunday(ts2):
    """
    定时间执行
    :return:
    """
    ts2.get_ppi()
    ts2.get_cpi()
    ts2.get_gdp_contrib()
    ts2.get_gdp_pull()
    ts2.get_gdp_for()
    ts2.get_gdp_quarter()
    ts2.get_gdp_year()
    ts2.get_money_supply_bal()
    ts2.get_money_supply()
    ts2.get_rrr()
    ts2.get_loan_rate()
    ts2.get_deposit_rate()

    ts2.get_zz500s()
    ts2.get_sz50s()
    ts2.get_hs300s()
    ts2.get_st_classified()
    ts2.get_gem_classified()
    ts2.get_sme_classified()
    ts2.get_area_classified()
    ts2.get_concept_classified()
    ts2.get_industry_classified()
    ts2.new_stocks()
    ts2.xsg_data()

    for year in range(2010, 2019):
        for quarter in range(1, 5):
            df = ts2.get_cashflow_data(year, quarter)

    for year in range(2010, 2019):
        for quarter in range(1, 5):
            df = ts2.get_debtpaying_data(year, quarter)

    for year in range(2010, 2019):
        for quarter in range(1, 5):
            df = ts2.get_growth_data(year, quarter)

    for year in range(2010, 2019):
        for quarter in range(1, 5):
            df = ts2.get_operation_data(year, quarter)

    for year in range(2010, 2019):
        for quarter in range(1, 5):
            df = ts2.get_profit_data(year, quarter)

    for year in range(2010,2019):
        for quarter in range(1,5):
            df = ts2.get_report_data(year,quarter)

    for year in range(2010, 2019):
        for quarter in range(1,5):
            df = ts2.fund_holdings(year, quarter)

    for year in range(2010, 2019):
        for quarter in range(1,5):
            df = ts2.forecast_data(year, quarter)

    for year in range(2010, 2019):
        df = ts2.profit_data(year, top=100)


@sched.scheduled_job('interval',seconds=3)
def job_once():
    ts.get_stock_basics()
    ts.get_hist_data('600848')
    ts.get_h_data('600848',autype='hfq',end='2018-06-28',start='2015-07-01')
    ts.get_sina_dd(['000063'], date='2018-06-27', vol=400)

@sched.scheduled_job('interval',seconds=3)
def job_realtime():
    ts.get_index()
    ts.get_today_ticks('601333')
    ts.get_realtime_quotes(['002049','002624'])
    ts.get_realtime_quotes(['sh', 'sz', 'hs300', 'sz50', 'zxb', 'cyb'])
    ts.get_tick_data('002049', DateUtil.getDatetimeYesterdayStr( DateUtil.getDatetimeToday()))
    ts.get_today_all()



def main():
    pass

is_closing = False

def signal_int_handler(signum, frame):
    global is_closing
    logging.info('exiting...')
    is_closing = True
    sched.shutdown(True)

#SIGKILL 不可被捕获
def signal_kill_handler():
    global is_closing
    logging.info('killed, exiting...')
    is_closing = True
    sched.shutdown(True)

def signal_term_handler(*args):
    global is_closing
    logging.info('killed, exiting...')
    is_closing = True
    sched.shutdown(True)

def try_exit():
    global is_closing
    if is_closing:
        # clean up here
        logging.info('exit success')

class Thread_job_sunday (threading.Thread):
    def __init__(self, threadname,ts):
        threading.Thread.__init__(self)
        self.threadname = threadname
        self.ts = ts

    def run(self):
        logging.info ("开始线程：" + self.threadname)
        job_sunday(self.ts)
        logging.info ("退出线程：" + self.threadname)


if __name__ == "__main__":
    # tfn_job_sunday = Thread_job_sunday('job_sunday', ts2)
    # tfn_job_sunday.start()
    # tfn_job_sunday.join()

    # signal.signal(signal.SIGINT, signal_int_handler)
    # #signal.signal(signal.SIGKILL, signal_term_handler)
    # signal.signal(signal.SIGTERM, signal_term_handler)
    # setup_logging()
    # main()
    # sched.start()

    globals.global_realtime()

