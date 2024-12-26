from frappe.model.document import Document

class MembershipCard(Document):
    def validate(self):
        if not self.issue_date:
            self.issue_date = frappe.utils.nowdate()
        
        if not self.expiry_date:
            # Set expiry date to one year from issue date
            self.expiry_date = frappe.utils.add_years(self.issue_date, 1) 