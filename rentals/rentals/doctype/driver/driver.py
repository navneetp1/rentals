# Copyright (c) 2025, Navneet and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Driver(WebsiteGenerator):
	def before_save(self):
		if self.last_name == "":
			self.full_name = f"{self.first_name}"
		else:
			self.full_name = f"{self.first_name} {self.last_name}"
	
	# def send_alert(self):
	# 	print("sending message")

	def on_trash(self):
		available_driver = frappe.db.exists("Ride Booking", {
			"driver": self.full_name,
			"docstatus": ("<", 2)
		})

		if available_driver:
			frappe.throw("Can't delete a driver with an active booking.")
