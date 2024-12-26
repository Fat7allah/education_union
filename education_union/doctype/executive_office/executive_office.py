from frappe.model.document import Document

class ExecutiveOffice(Document):
    def validate(self):
        # Ensure head_of_office is a member of the office
        if self.head_of_office:
            is_member = False
            for member in self.members:
                if member.member == self.head_of_office:
                    is_member = True
                    break
            if not is_member:
                self.append("members", {
                    "member": self.head_of_office,
                    "position": "رئيس المكتب"
                }) 