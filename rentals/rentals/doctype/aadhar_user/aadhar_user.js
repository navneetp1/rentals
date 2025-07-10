// Copyright (c) 2025, Navneet and contributors
// For license information, please see license.txt

frappe.ui.form.on("Aadhar User", {
	refresh(frm) {
    if (frm.doc.aadhar_number) {
            frm.trigger('show_masked');  // onload masking

      const cur_user = frappe.session.user

      if (cur_user === 'Administrator' || cur_user === frm.doc.owner){
              frm.add_custom_button("Toggle Aadhar", () => {
              if (frm.__aadhar_masked) {
                frm.trigger('show_unmasked'); 
              } else {
                frm.trigger('show_masked');
            }
      });
      }
      
    }
	},
    show_masked(frm){
        const masked = frm.doc.aadhar_number;
        frm.fields_dict.aadhar_number.$wrapper.html(`<div class="form-control">${masked}</div>`);
        frm.__aadhar_masked = true;
    },
    show_unmasked(frm){
        frappe.call({
          method: 'rentals.rentals.doctype.aadhar_user.aadhar_user.get_decrypted_aadhar',
          args: {
            docname: frm.doc.name
          },
          callback: function(r){
            if (r.message){
                  frm.fields_dict.aadhar_number.$wrapper.html(`<div class="form-control">${r.message}</div>`);
                  frm.__aadhar_masked = false;
            }
          }
        })
   
    },
    on_save(frm){
        frm.reload_doc()
    }

});


