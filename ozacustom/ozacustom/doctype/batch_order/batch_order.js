// Copyright (c) 2024, sanpra and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Batch Order", {
// 	refresh(frm) {

// 	},
// });

// frappe.ui.form.on('Set Batch Table', {
//     sales_order: function (frm, cdt, cdn) {
//         var child_doc = locals[cdt][cdn]
//         frappe.call({
//             method: "filchild",
//             args: {
//                 sale_order_name: child_doc.sales_order
//             },
//             doc:frm.doc,
//             callback: function(response) {
//                 var myVariable = []
//                 myVariable=response.message;
//                 frm.set_query("item_code",function(frm, cdt, cdn) {
//                     var child=locals[cdt][cdn]
//                     return {
//                         filters: [
//                             ["Item","name","in", response.message]
//                         ]
//                     };
//                 });
//             }
//         });
//     }
// });


frappe.ui.form.on('Set Batch Table', {
    sales_order: function(frm, cdt, cdn) {
        var child_doc = locals[cdt][cdn];
        frappe.call({
            method: "filchild",
            args: {
                sale_order_name: child_doc.sales_order
            },
            doc:frm.doc,
            callback: function(response) {
                var myVariable = response.message;
                frm.fields_dict['set_batch_table'].grid.get_field('item_code').get_query = function(doc, cdt, cdn) {
                    return {
                        filters: [
                            ["Item", "name", "in", myVariable]
                        ]
                    };
                };
            }
        });
    }
});
