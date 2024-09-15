// Copyright (c) 2024, sanpra and contributors
// For license information, please see license.txt

frappe.ui.form.on("Inspection Offer Letter", {
	sales_order_no: function (frm) {
		frm.clear_table("fitting_item")
		frm.refresh_field('fitting_item')		
		frm.call({
			method:'getitems',
			doc: frm.doc
		});
	}
});
