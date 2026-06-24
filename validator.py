def validate(schema):
    missing = []

    if not isinstance(schema, dict):
        return False, ["schema"]

    if "ui" not in schema or not isinstance(schema["ui"], dict) or not schema["ui"].get("pages"):
        missing.append("ui.pages")

    if "api" not in schema or not isinstance(schema["api"], dict) or not schema["api"].get("endpoints"):
        missing.append("api.endpoints")

    if "database" not in schema or not isinstance(schema["database"], dict) or not schema["database"].get("tables"):
        missing.append("database.tables")

    if "auth" not in schema or not isinstance(schema["auth"], dict) or not schema["auth"].get("roles"):
        missing.append("auth.roles")

    if missing:
        return False, missing

    return True, []
