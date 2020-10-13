
import baostock as BS
import pandas as PD
import time as TIME

START_DATE = '2017-06-01'
END_DATE   = TIME.strftime('%Y-%m-%d')

MIN_LEVEL  = "date,time,code,open,high,low,close,volume,amount,adjustflag"
DAY_LEVEL  = "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST"
WEEK_LEVEL = "date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg"

CODE_OK = '0'

# date : 交易所行情日期，格式 YYYY-MM-DD
# time : 交易所行情时间，格式 YYYYMMDDHHMMSSsss
#

def login():
	lg = BS.login()

	# show login info
	print('login respond error_code : ' + lg.error_code)
	print('login respond error_msg  : ' + lg.error_msg)

	pass


def logout():
	BS.logout()
	pass


def get_stock_data(id, level, start_date, end_date):
	''' 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。'''
	rs = BS.query_history_k_data_plus(
		id,
		level,
		start_date = START_DATE,
		end_date   = END_DATE,
		frequency  = "d",
		adjustflag = "3")

	data_list = []

	while (rs.error_code == '0') & rs.next():
		# 获取一条记录，将记录合并在一起
		data_list.append(rs.get_row_data())
	result = PD.DataFrame(data_list, columns=rs.fields)

	#### 结果集输出到csv文件 ####   
	#result.to_csv("D:\\history_A_stock_k_data.csv", index=False)
	print(result)
	return result


def get_stock_basic(_code):
	'''
	code: 证券代码
	code_name: 证券名称
	ipoDate: 上市日期
	outDate: 退市日期
	type: 证券类型（1，股票；2，指数；3，其他）
	status: 上市状态（1，上市；0，退市）
	'''
	rs = BS.query_stock_basic(code=_code)
	data_list = []
	while (rs.error_code == '0') & rs.next():
		data_list.append(rs.get_row_data())
	result = PD.DataFrame(data_list, columns=rs.fields)
	print(result)
	return result


def get_all_stocks(start_date):
	rs = BS.query_all_stock(day=start_date)

	data_list = []

	while (rs.error_code == '0') & rs.next():
		data_list.append(rs.get_row_data())

	result = PD.DataFrame(data_list, columns=rs.fields)

	print(result)
	return result


# 行业分类
def get_stock_industry():
	rs = BS.query_stock_industry()
	industry_list = []
	while (rs.error_code == '0') & rs.next():
		industry_list.append(rs.get_row_data())
	result = PD.DataFrame(industry_list, columns=rs.fields)

	print(result)
	return result

# 沪深300
def get_hs300_stocks():
	rs = BS.query_hs300_stocks()

	hs300_stocks = []
	while (rs.error_code == '0') & rs.next():
		hs300_stocks.append(rs.get_row_data())
	result = PD.DataFrame(hs300_stocks, columns=rs.fields)
	print(result)
	return result


# 上证50
def get_sz50_stocks():
	rs = BS.query_sz50_stocks()

	sz50_stocks = []
	while (rs.error_code == '0') & rs.next():
		sz50_stocks.append(rs.get_row_data())
	result = PD.DataFrame(sz50_stocks, columns=rs.fields)
	print(result)
	return result


# 中证500
def get_zz500_stocks():
	rs = BS.query_zz500_stocks()

	zz500_stocks = []
	while (rs.error_code == '0') & rs.next():
		zz500_stocks.append(rs.get_row_data())
	result = PD.DataFrame(zz500_stocks, columns=rs.fields)
	print(result)
	return result

#######Test

login()

#get_stock_data('sh.600000', DAY_LEVEL, START_DATE, END_DATE)
#get_all_stocks(START_DATE)
#get_hs300_stocks()
#get_sz50_stocks()
#get_stock_industry()
#d = get_zz500_stocks()
#print(d.shape)
get_stock_basic('sh.600000')

logout()
