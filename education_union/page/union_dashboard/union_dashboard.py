import frappe

@frappe.whitelist()
def get_dashboard_data():
    data = {
        'total_members': frappe.db.count('Member'),
        'active_cards': frappe.db.count('Membership Card', {'status': 'مدفوع'}),
        'pending_cards': frappe.db.count('Membership Card', {'status': 'قيد الانتظار'})
    }
    return data 