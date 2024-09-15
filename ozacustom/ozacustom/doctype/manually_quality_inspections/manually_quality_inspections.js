// Copyright (c) 2024, sanpra and contributors
// For license information, please see license.txt

frappe.ui.form.on("Manually Quality Inspections", {
	quality_inspection_template: function (frm) {
		frm.clear_table("quality_inspection_item")
		frm.refresh_field('quality_inspection_item')		
		frm.call({
			method:'gettemp',
			doc: frm.doc
		});
	}
});

frappe.ui.form.on("Manually Quality Inspections", {
	longitudinal_reversion: function (frm) {
		frm.clear_table("longitudinal_reversion_test")
		frm.refresh_field('longitudinal_reversion_test')		
		frm.call({
			method:'gett',
			doc: frm.doc
		});
	}
});

frappe.ui.form.on("Manually Quality Inspections", {
	internal_pressure_template: function (frm) {
		frm.clear_table("internal_pressure_test")
		frm.refresh_field('internal_pressure_test')		
		frm.call({
			method:'mdn',
			doc: frm.doc
		});
	}
});

frappe.ui.form.on("Manually Quality Inspections", {
	quality_other_test_template: function (frm) {
		frm.clear_table("quality_other_test")
		frm.refresh_field('quality_other_test')		
		frm.call({
			method:'mocks',
			doc: frm.doc
		});
	}
});
