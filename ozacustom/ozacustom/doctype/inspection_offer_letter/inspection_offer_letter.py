# Copyright (c) 2024, sanpra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class InspectionOfferLetter(Document):
	@frappe.whitelist()
	def getitems(self):
		sales_order_doc = frappe.get_doc("Sales Order", self.sales_order_no)	
		self.sales_order_date = sales_order_doc.transaction_date	
		for mg in sales_order_doc.get("items"):
			self.append("fitting_item", {
				"item_code": mg.item_code,
				"item_name": mg.item_name,
				"qty": mg.qty,
			})
