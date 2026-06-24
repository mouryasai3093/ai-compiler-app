def repair(schema):
    if not isinstance(schema, dict):
        schema = {}

    if "ui" not in schema or not isinstance(schema["ui"], dict):
        schema["ui"] = {"pages": ["Login"]}
    elif not schema["ui"].get("pages"):
        schema["ui"]["pages"] = ["Login"]

    if "api" not in schema or not isinstance(schema["api"], dict):
        schema["api"] = {"endpoints": [{"path": "/user", "methods": ["GET", "POST"]}]}
    elif not schema["api"].get("endpoints"):
        schema["api"]["endpoints"] = [{"path": "/user", "methods": ["GET", "POST"]}]

    if "database" not in schema or not isinstance(schema["database"], dict):
        schema["database"] = {"tables": ["user"]}
    elif not schema["database"].get("tables"):
        schema["database"]["tables"] = ["user"]

    if "auth" not in schema or not isinstance(schema["auth"], dict):
        schema["auth"] = {"roles": ["User"]}
    elif not schema["auth"].get("roles"):
        schema["auth"]["roles"] = ["User"]

    return schema
