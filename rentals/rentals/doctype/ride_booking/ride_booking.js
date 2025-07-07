// Copyright (c) 2025, Navneet and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {
        
	},
    // dynamically calculate price on changing the rate
    rate(frm){
        frm.trigger("update_total_amount") // calling the method using trigger
    },

    update_total_amount(frm){
        let total_distance = 0
        for(let item of frm.doc.items){
            total_distance += item.distance
        }
        const amount = total_distance * frm.doc.rate
        frm.set_value("total_amount", amount)
    }
});

frappe.ui.form.on("Ride Booking Item", {
    refresh(frm){
        // dynamically changing the price upon changing distance

    },
    distance(frm, cdt, cdn){
        // console.log(cdt, cdn); // child table doctype, child table name
        // console.log("Child table distance modified");
        // console.log(frappe.get_doc(cdt, cdn));
        // frappe.model.set_value(cdt, cdn, "source", "updt_source")
        frm.trigger("update_total_amount")
        
    },
    // https://docs.frappe.io/framework/user/en/api/form (Child Table Events)
    items_remove(frm){
        frm.trigger("update_total_amount")
    }   
})