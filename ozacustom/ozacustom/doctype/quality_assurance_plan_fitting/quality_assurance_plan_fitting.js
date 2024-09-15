// Copyright (c) 2024, sanpra and contributors
// For license information, please see license.txt

frappe.ui.form.on("Quality Assurance Plan Fitting", {
	sales_order_no: function (frm) {
		frm.clear_table("items")
		frm.refresh_field('items')		
		frm.call({
			method:'getitems',
			doc: frm.doc
		});
	}
});

frappe.ui.form.on("Quality Assurance Plan Fitting", {
	quality_assurance_plan_fitting_template: function (frm) {
		frm.clear_table("quality_assurance_plan_fitting_item")
		frm.refresh_field('quality_assurance_plan_fitting_item')		
		frm.call({
			method:'gettemp',
			doc: frm.doc
		});
	}
});
