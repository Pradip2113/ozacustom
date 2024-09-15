# Copyright (c) 2024, sanpra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BatchOrder(Document):
	@frappe.whitelist()
	def filchild(self,sale_order_name):
		item_list=[]
		child_list= frappe.get_all("Sales Order Item", filters={"parent":sale_order_name}, fields=["item_code","parent"])
		for i in child_list:
			item_list.append(i.item_code)
		return item_list
     
