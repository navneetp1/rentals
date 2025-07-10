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

		get_vehicle = frappe.db.exists("Ride Booking", {
			"vehicle": self.vehicle,
			"docstatus": 1,
		})

		if get_vehicle:
			frappe.throw(f'{self.vehicle} is already booked. Try again later.')	


	# def before_save(self):
	# 	self.total_amount = self.rate * self.distance

	def on_submit(self):
		frappe.db.set_value('Vehicle', self.vehicle, 'status', 'Booked')
	
	def on_cancel(self):
		frappe.db.set_value('Vehicle', self.vehicle, 'status', 'Available')

	def before_save(self):
		if self.auto_assign == 1:
			available_driver = frappe.db.get_list("Driver", pluck="full_name", filters={
				'rating': (">", 0.6),
				'status': 'Available'
			})


			if not available_driver:
				frappe.throw('We couldn"t assign any good drivers to you as they all are booked for now. Please choose with caution')

			self.driver = available_driver[0]
			frappe.db.set_value("Driver", self.driver, 'status', 'Booked')
		else:
			frappe.throw("You need to choose a driver if haven't selected auto assign.")

	
