// Copyright (c) 2024, sanpra and contributors
// For license information, please see license.txt

frappe.ui.form.on("Quality Assurance Plan Pipe", {
	sales_order: function (frm) {
		frm.clear_table("pipe_set_sales_order_item")
		frm.refresh_field('pipe_set_sales_order_item')		
		frm.call({
			method:'getitems',
			doc: frm.doc
		});
	}
});

frappe.ui.form.on("Quality Assurance Plan Pipe", {
	pipe_raw_material_template: function (frm) {
		frm.clear_table("material_item")
		frm.refresh_field('material_item')		
		frm.call({
			method:'gettemp',
			doc: frm.doc
		});
	}
});

frappe.ui.form.on("Quality Assurance Plan Pipe", {
	ef_tpi_pipe_template: function (frm) {
		frm.clear_table("tpi_pipe_item")
		frm.refresh_field('tpi_pipe_item')		
		frm.call({
			method:'getset',
			doc: frm.doc
		});
	}
});

frappe.ui.form.on("Quality Assurance Plan Pipe", {
	pipe_finish_material_template: function (frm) {
		frm.clear_table("ef_tpi_pipe_item")
		frm.refresh_field('ef_tpi_pipe_item')		
		frm.call({
			method:'getsetfinish',
			doc: frm.doc
		});
	}
});