from frappe.model.document import Document
import frappe

class Member(Document):
    def autoname(self):
        # Generate unique membership number
        self.name = f"MEM-{frappe.utils.now_datetime().strftime('%Y')}-{frappe.utils.random_string(6)}"
    
    def validate(self):
        if not self.membership_number:
            self.membership_number = self.name 