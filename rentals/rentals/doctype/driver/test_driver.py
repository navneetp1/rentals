 # Copyright (c) 2025, Navneet and Contributors
# See license.txt

import frappe

from frappe.tests import IntegrationTestCase
from frappe.tests.utils import FrappeTestCase

# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



class IntegrationTestDriver(IntegrationTestCase):
	"""
	Integration tests for Driver.
	Use this class for testing interactions between multiple components.
	"""

	pass

class TestDriver(FrappeTestCase):
	def test_full_name_correctly(self):
		test_driver = frappe.new_doc('Driver')
		test_driver.first_name = "Harry"
		test_driver.last_name = "Brook"
		test_driver.license_number = "ABCDE12345"
		test_driver.save()
	
		self.assertEqual(test_driver.full_name, "Harry Brook")
	
	def test_full_name_correctly_when_no_lastname_provided(self):
		test_driver = frappe.new_doc('Driver')
		test_driver.first_name = "John"
		test_driver.last_name = ""
		test_driver.license_number = "ABCDE12345"
		test_driver.save()
	
		self.assertEqual(test_driver.full_name, "John")
	