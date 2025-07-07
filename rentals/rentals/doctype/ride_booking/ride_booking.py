# Copyright (c) 2025, Navneet and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):

	def validate(self):

		if not self.rate:
			self.rate = frappe.db.get_single_value("Rentals Settings", "standard_rate") 
			# frappe.db.get_singles_dict("Rentals Settings") - returns as a dict ; unparsed output
			# frappe.get_single("Rentals Settings").standard_rate - parsed output

		total_distance = 0
		for item in self.items:
			total_distance += item.distance
		
		self.total_amount = self.rate * total_distance


	# def before_save(self):
	# 	self.total_amount = self.rate * self.distance
