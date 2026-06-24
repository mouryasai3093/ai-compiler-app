def generate_design(intent):
    app_type = intent["app_type"]
    features = intent["features"]

    flows = []

    if "login" in features:
        flows.append("Login")

    if "register" in features:
        flows.append("Register")

    if "dashboard" in features:
        flows.append("Dashboard")

    if "report" in features:
        flows.append("Reports")

    if "notification" in features:
        flows.append("Notifications")

    if "search" in features:
        flows.append("Search")

    if "booking" in features:
        flows.append("Booking")

    if "approval" in features:
        flows.append("Approvals")

    if "analytics" in features:
        flows.append("Analytics")

    if app_type == "Hospital":
        flows = list(dict.fromkeys(flows + ["Book Appointment", "Patient Records"]))
        return {
            "app_type": app_type,
            "description": "Hospital management system with appointments, doctors, and patients.",
            "entities": ["Doctor", "Patient", "Appointment", "Prescription"],
            "roles": ["Admin", "Doctor", "Patient", "Nurse"],
            "flows": flows
        }

    elif app_type == "CRM":
        if not flows:
            flows.append("Login")
        flows = list(dict.fromkeys(flows + ["Contact Management", "Sales Pipeline"]))
        return {
            "app_type": app_type,
            "description": "Customer relationship management with contact tracking and sales workflows.",
            "entities": ["User", "Contact", "Lead", "Opportunity"],
            "roles": ["Admin", "Sales", "Customer"],
            "flows": flows
        }

    elif app_type == "Student":
        if "Login" not in flows:
            flows.append("Login")
        flows = list(dict.fromkeys(flows + ["View Courses", "Grades"]))
        return {
            "app_type": app_type,
            "description": "Student portal for course access, grades, and learning resources.",
            "entities": ["Student", "Course", "Faculty", "Enrollment"],
            "roles": ["Admin", "Student", "Faculty"],
            "flows": flows
        }

    elif app_type == "Inventory":
        if "Login" not in flows:
            flows.append("Login")
        flows = list(dict.fromkeys(flows + ["Manage Inventory", "Stock Alerts"]))
        return {
            "app_type": app_type,
            "description": "Inventory management for products, suppliers, and stock control.",
            "entities": ["Product", "Supplier", "Stock", "Warehouse"],
            "roles": ["Admin", "Manager", "Warehouse Staff"],
            "flows": flows
        }

    elif app_type == "Ecommerce":
        if "Login" not in flows:
            flows.append("Login")
        flows = list(dict.fromkeys(flows + ["Browse Products", "Checkout", "Order History"]))
        return {
            "app_type": app_type,
            "description": "Ecommerce platform with product browsing, checkout, and customer orders.",
            "entities": ["Product", "Order", "Customer", "Cart"],
            "roles": ["Admin", "Customer"],
            "flows": flows
        }

    elif app_type == "Library":
        if "Login" not in flows:
            flows.append("Login")
        flows = list(dict.fromkeys(flows + ["Issue Book", "Search Catalog"]))
        return {
            "app_type": app_type,
            "description": "Library system for book issue, member management, and catalog search.",
            "entities": ["Book", "Member", "Issue", "Catalog"],
            "roles": ["Admin", "Librarian", "Member"],
            "flows": flows
        }

    elif app_type == "Hotel":
        if "Login" not in flows:
            flows.append("Login")
        flows = list(dict.fromkeys(flows + ["Search Rooms", "Reservation"]))
        return {
            "app_type": app_type,
            "description": "Hotel booking system with room search, reservations, and guest management.",
            "entities": ["Hotel", "Room", "Reservation", "Guest"],
            "roles": ["Admin", "Receptionist", "Guest"],
            "flows": flows
        }

    elif app_type == "HR":
        if "Login" not in flows:
            flows.append("Login")
        flows = list(dict.fromkeys(flows + ["Employee Directory", "Leave Management"]))
        return {
            "app_type": app_type,
            "description": "HR management system for employee records, leave, and approvals.",
            "entities": ["Employee", "Department", "Leave", "Payroll"],
            "roles": ["Admin", "HR", "Employee"],
            "flows": flows
        }

    elif app_type == "Payroll":
        if "Login" not in flows:
            flows.append("Login")
        flows = list(dict.fromkeys(flows + ["Payroll Processing", "Payslips"]))
        return {
            "app_type": app_type,
            "description": "Payroll system for salary processing, payslips, and employee compensation.",
            "entities": ["Employee", "Salary", "Payslip", "Tax"],
            "roles": ["Admin", "Finance", "Employee"],
            "flows": flows
        }

    elif app_type == "Task":
        if "Login" not in flows:
            flows.append("Login")
        flows = list(dict.fromkeys(flows + ["Task Board", "Project Overview"]))
        return {
            "app_type": app_type,
            "description": "Task management system with projects, tasks, and collaboration.",
            "entities": ["Task", "Project", "User", "Comment"],
            "roles": ["Admin", "User", "Manager"],
            "flows": flows
        }

    if not flows:
        flows.append("Login")

    return {
        "app_type": app_type,
        "description": "General application generated from natural language requirements.",
        "entities": ["User"],
        "roles": ["User"],
        "flows": flows
    }
