def generate_schema(design):
    entities = design["entities"]

    return {
        "metadata": {
            "app_type": design.get("app_type", "Unknown"),
            "description": design.get("description", "")
        },
        "ui": {
            "pages": design["flows"]
        },
        "api": {
            "endpoints": [
                {
                    "path": f"/{entity.lower()}",
                    "methods": ["GET", "POST", "PUT", "DELETE"]
                }
                for entity in entities
            ]
        },
        "database": {
            "tables": [entity.lower() for entity in entities]
        },
        "auth": {
            "roles": design["roles"]
        }
    }
