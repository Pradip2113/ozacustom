# Copyright (c) 2024, sanpra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class QualityAssurancePlanPipe(Document):
	@frappe.whitelist()
	def getitems(self):
		sales_order_doc = frappe.get_doc("Sales Order", self.sales_order)	
		self.po_date = sales_order_doc.transaction_date	
		for mg in sales_order_doc.get("items"):
			self.append("pipe_set_sales_order_item", {
				# "item_code": mg.discricption,
				"discricption": mg.item_name,
				"qty": mg.qty,
			})

	@frappe.whitelist()
	def gettemp(self):
		rw_temp = frappe.get_doc("Pipe Raw Material Template", self.pipe_raw_material_template)	
		for j in rw_temp.get("items"):
			self.append("material_item", {
				"clause_no": j.clause_no,
				"test_name": j.test_name,
				"samples": j.samples,
				"test_method": j.test_method,
				"specification": j.specification,
				"documentation": j.documentation,
				"inspection_by_m": j.inspection_by_m,
				"inspection_by_tpi": j.inspection_by_tpi,
				"inspection_by_b": j.inspection_by_b,
				"remark": j.remark,
			})

	@frappe.whitelist()
	def getset(self):
		set_temp = frappe.get_doc("EF TPI PIPE Template", self.ef_tpi_pipe_template)	
		for i in set_temp.get("items"):
			self.append("tpi_pipe_item", {
				"clause_no": i.clause_no,
				"test_name": i.test_name,
				"samples": i.samples,
				"test_method": i.test_method,
				"specification": i.specification,
				"documentation": i.documentation,
				"inspection_by_m": i.inspection_by_m,
				"inspection_by_tpi": i.inspection_by_tpi,
				"inspection_by_b": i.inspection_by_b,
				"remark": i.remark,
			})

	@frappe.whitelist()
	def getsetfinish(self):
		set_temp = frappe.get_doc("Pipe Finish Material Template", self.pipe_finish_material_template)	
		for i in set_temp.get("items"):
			self.append("ef_tpi_pipe_item", {
				"clause_no": i.clause_no,
				"test_name": i.test_name,
				"samples": i.samples,
				"test_method": i.test_method,
				"specification": i.specification,
				"documentation": i.documentation,
				"inspection_by_m": i.inspection_by_m,
				"inspection_by_tpi": i.inspection_by_tpi,
				"inspection_by_b": i.inspection_by_b,
				"remark": i.remark,
			})
