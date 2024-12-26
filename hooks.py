app_name = "education_union"
app_title = "Education Union"
app_publisher = "Your Name"
app_description = "Educational Unions Management System"
app_icon = "octicon octicon-organization"
app_color = "blue"
app_email = "your@email.com"
app_license = "MIT"

# Include RTL CSS
app_include_css = [
    "/assets/education_union/css/education_union_rtl.css"
]

# Fixtures for Role and Custom Field
fixtures = [
    {
        "doctype": "Role",
        "filters": [
            ["name", "in", [
                "Union Executive",
                "Regional Office Admin",
                "Provincial Office Admin",
                "Local Office Admin"
            ]]
        ]
    }
]

# Document translations
translation_modules = ["education_union"] 