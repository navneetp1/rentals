# Copyright (c) 2025, Navneet and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from cryptography.fernet import Fernet


class AadharUser(Document):

	def validate(self):
		if not self.aadhar_number:
			frappe.throw("Aadhar Number can't be empty")
		if len(self.aadhar_number) != 12:
			frappe.throw(f"Aadhar Number should be 12 characters long, Current length: {len(self.aadhar_number)}")
		if self.aadhar_number[0] in ['1', '2']:
			frappe.throw(f'Aadhar shouldn"t begin with 1 or 2')

		# encryption
		self.aadhar_encryption()
		self.aadhar_number = f'XXXX-XXXX-{self.aadhar_number[8:]}'

	def get_fernet(self):
		key = frappe.conf.encryption_key
		return Fernet(key)

	def aadhar_encryption(self):
		fernet = self.get_fernet()
		self.aadhar_encrypted = fernet.encrypt(self.aadhar_number.encode())
	
	def aadhar_decryption(self, value):
		fernet = self.get_fernet()
		return fernet.decrypt(value).decode()
	

@frappe.whitelist()
def get_decrypted_aadhar(docname):
	doc = frappe.get_doc("Aadhar User", docname)
	return doc.aadhar_decryption(doc.aadhar_encrypted)


	


	# 	key = get_encryption_key()
    # 	fernet = Fernet(key)
	# 	self.aadhar_number = encrypt_aadhar(self.aadhar_number)
			
	
	# def get_encryption_key(self):
	# 	key = frappe.conf.encryption_key
	# 	if not key:
	# 		frappe.throw('No encryption key provided in json')
	# 	return key
	
	# def encrypt_aadhar(self, value):
	# 	key = get_encryption_key()	
	# 	fernet = Fernet(key)
	# 	return fernet.encrypt(value.encode())

	
	# def decrypt_aadhar(self, enc_value):
	# 	key = get_encryption_key()
	# 	fernet = Fernet(key)
	# 	return fernet.decrypt(env_value).decode()
		


# steps
# key = frappe.conf.encryption_key

# <cryptography.fernet.Fernet at 0x79b33c215930>
# fernet = Fernet(key)

# value = 'abc123'
# enc = fernet.encrpyt(value.encode())

# # decryption
# dec = fernet.decrypt(enc).decode()





