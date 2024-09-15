import frappe
from frappe.model.document import Document

@frappe.whitelist()
def role():
    wo = frappe.get_all("Work Order",fields=["name","production_item","sales_order","custom_batch_no"])
    for i in wo:
        user_roles = frappe.get_all("Set Batch Table", filters={"item_code":i.production_item,"sales_order":i.sales_order},fields=["item_code","batch_no","sales_order"])
        for m in user_roles:
            frappe.db.set_value("Work Order", str(i.name), "custom_batch_no",m.batch_no)
            
            
# @frappe.whitelist()
# def filchild():
    
    # sorder = frappe.get_all("Sales Order",fields=["name"])
    # for m in sorder:
    #     user_roles = frappe.get_all("Set Batch Table", filters={"sales_order":m.name},fields=["sales_order"])
    #     for s in user_roles:
    #         frappe.msgprint(str(s.sales_order))
        # oktest = frappe.get_all("Sales Order Item", filters={"parent":m.name}, fields=["item_code","parent"])
        # for z in oktest:
        #     frappe.msgprint(str(z.item_code))
        # return [item.get("item_code") for item in oktest]
    # for j in oktest:
    #     frappe.msgprint(str(j.item_code))
    #     # pass