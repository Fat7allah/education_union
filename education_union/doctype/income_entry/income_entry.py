from frappe.model.document import Document
import frappe

class IncomeEntry(Document):
    def validate(self):
        if not self.entry_date:
            self.entry_date = frappe.utils.nowdate() 