# Copyright (c) 2024, sanpra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class QualityAssurancePlanFitting(Document):
	@frappe.whitelist()
	def getitems(self):
		sales_order_doc = frappe.get_doc("Sales Order", self.sales_order_no)	
		self.sales_order_date = sales_order_doc.transaction_date	
		for mg in sales_order_doc.get("items"):
			self.append("items", {
				"item_code": mg.item_code,
				"item_name": mg.item_name,
				"qty": mg.qty,
			})

	@frappe.whitelist()
	def gettemp(self):
		lst_temp = frappe.get_doc("Quality Assurance Plan Fitting Template", self.quality_assurance_plan_fitting_template)		
		for mc in lst_temp.get("items"):
			self.append("quality_assurance_plan_fitting_item", {
				"description": mc.description,
				"type_of_check": mc.type_of_check,
				"quantum_of_check": mc.quantum_of_check,
				"ref_doc": mc.ref_doc,
				"acceptance_norms": mc.acceptance_norms,
				"documentation": mc.documentation,
				"inspection_manual": mc.inspection_manual,
				"inspection_customer": mc.inspection_customer,
				"remark": mc.remark,
			})
