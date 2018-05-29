# -*- coding: utf-8 -*-
# filename: dboperation.py



from dbconnection import DBConnection
from getdate import GetDate

class DBOperation(object):
	def __init__(self):
		self.dbc = DBConnection()
		self.getDate = GetDate()

	def updateOEMToFacility(self):
		SQL = """
				UPDATE T3 SET T3.ZRMK_0 = T1.ZRMK_0
				FROM SORDERQ T1
					LEFT JOIN PORDERQ T2 ON T1.SOHNUM_0 = T2.SOHNUM_0 AND T1.SOPLIN_0 = T2.SOPLIN_0
					LEFT JOIN SORDERQ T3 ON T2.POHNUM_0 = T3.POHNUM_0 AND T2.POPLIN_0 = T3.POPLIN_0
				WHERE T1.ZRMK_0 <> N'' 
					AND T1.SALFCY_0 = N'0101'
					AND T3.ZRMK_0 = N''
			"""
		self.dbc.execute(SQL)


if __name__ == '__main__':
	dbo = DBOperation()
	print dbo.getTodaySaleOrderDetails('0201')