# encoding: UTF-8

from hsstock.vnpy.trader.app.riskManager.rmEngine import RmEngine
from hsstock.vnpy.trader.app.riskManager.uiRmWidget import RmEngineManager

appName = 'RiskManager'
appDisplayName = u'风险管理'
appEngine = RmEngine
appWidget = RmEngineManager
appIco = 'rm.ico'