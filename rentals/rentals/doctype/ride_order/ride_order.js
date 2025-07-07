// Copyright (c) 2025, Navneet and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
	refresh(frm) {
        if (frm.doc.status === "New"){
            frm.add_custom_button('Accept', () => {
                frm.set_value("status", "Accepted")
                frm.save()
            }, "Actions")

            frm.add_custom_button('Reject', () => {
                frm.set_value("status", "Rejected")
                frm.save()
            }, "Actions")
        }
        
	},
    status: function(frm){
        console.log("status changed")
    } // just for status field
});
