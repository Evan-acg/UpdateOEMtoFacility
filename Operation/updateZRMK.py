# -*- coding: utf-8 -*-
# filename: updateZRMK.py


from Public.dboperation import DBOperation


class UpdateZRMK:
	def __init__(self):
		self.dbo = DBOperation()


	def run(self):
		self.dbo.updateOEMToFacility()



if __name__ == '__main__':
	upRmk = UpdateZRMK()
	upRmk.run()