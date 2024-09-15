// Copyright (c) 2024, sanpra and contributors
// For license information, please see license.txt

frappe.ui.form.on("EF TPI FITTING", {
	sales_order_no: function (frm) {
		frm.clear_table("fitting_item")
		frm.refresh_field('fitting_item')		
		frm.call({
			method:'getitems',
			doc: frm.doc
		});
	}
});

frappe.ui.form.on("EF TPI FITTING", {
	ef_tpi_fitting_template: function (frm) {
		frm.clear_table("ef_tpi_fitting_item")
		frm.refresh_field('ef_tpi_fitting_item')		
		frm.call({
			method:'gettemp',
			doc: frm.doc
		});
	}
});
