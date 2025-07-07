import frappe

# http://van.life:8000/api/v2/method/rentals.api.get_message - The actual get API
# never use allow_guest again, use the headers Authorization for REST APIs
@frappe.whitelist(allow_guest=True)
def get_message():
    return "This is a Message from Custom API"

def throw_emoji(doc, event):
    frappe.throw('😭')


@frappe.whitelist()
def get_vehicle_list():
    data = frappe.db.get_list("Driver")
    return data

@frappe.whitelist()
def get_vehicle_names(doc, event):
    data = frappe.db.get_list("Driver", pluck="full_name")
    frappe.throw(data)

def send_reminder():
    pass

@frappe.whitelist()
def get_license_numbers():
    data = frappe.db.get_list("Driver", fields=["full_name", "license_number"])
    return data

@frappe.whitelist()
def get_phone_numbers():
    data = frappe.db.get_list("Driver", fields=["full_name", "phone_number"], order_by="full_name desc")
    return data

@frappe.whitelist()
def count_total_drivers():
    data = frappe.db.count("Driver")
    return data