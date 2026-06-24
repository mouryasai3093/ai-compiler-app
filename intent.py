def extract_intent(prompt):
    prompt = prompt.lower()

    app_type = "Unknown"
    app_map = {
        ("hospital", "health"): "Hospital",
        ("crm", "customer relationship management"): "CRM",
        ("student", "portal"): "Student",
        ("inventory", "stock"): "Inventory",
        ("ecommerce", "e-commerce", "online store"): "Ecommerce",
        ("library", "book"): "Library",
        ("hotel", "booking"): "Hotel",
        ("hr", "human resources"): "HR",
        ("payroll", "salary", "payslip"): "Payroll",
        ("task", "project management", "todo"): "Task"
    }

    for keywords, value in app_map.items():
        if any(keyword in prompt for keyword in keywords):
            app_type = value
            break

    feature_map = {
        "login": "login",
        "dashboard": "dashboard",
        "payment": "payment",
        "payments": "payment",
        "report": "report",
        "reports": "report",
        "notification": "notification",
        "notifications": "notification",
        "search": "search",
        "booking": "booking",
        "approve": "approval",
        "approvals": "approval",
        "analytics": "analytics",
        "register": "register",
        "signup": "register",
        "profile": "profile"
    }

    features = [feature for keyword, feature in feature_map.items() if keyword in prompt]
    features = sorted(set(features))

    return {
        "app_type": app_type,
        "features": features
    }

    