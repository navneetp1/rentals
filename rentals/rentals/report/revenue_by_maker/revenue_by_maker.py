# Copyright (c) 2025, Navneet and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	# data = get_data()
	data = frappe.get_all("Ride Booking", fields=["SUM(total_amount) as total_revenue" , "vehicle.maker"], filters={"docstatus": ("<", 2), "total_amount": (">",0)}, group_by="maker")

	return columns, data


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Maker"),
			"fieldname": "maker",
			"fieldtype": "Data",
		},
		{
			"label": _("total Revenue"),
			"fieldname": "total_revenue",
			"fieldtype": "Currency",
			"options": "INR" 
		},
	]


def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	# return frappe.db.sql("""
	# 	SELECT
	# 		v.maker AS maker,
	# 		SUM(rb.total_amount) AS total_revenue
	# 	FROM `tabRide Booking` rb
	# 	JOIN `tabVehicle` v ON rb.vehicle = v.name
	# 	WHERE rb.docstatus < 2 AND rb.total_amount > 0
	# 	GROUP BY v.maker
	# """, as_dict=True)
	pass 
