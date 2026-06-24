def simulate(schema):
    print("\n=== Runtime Simulation ===")

    print("Pages:")
    for page in schema["ui"]["pages"]:
        print("-", page)

    print("\nAPIs:")
    for api in schema["api"]["endpoints"]:
        print(f"- {api['path']} ({', '.join(api['methods'])})")

    print("\nDatabase Tables:")
    for table in schema["database"]["tables"]:
        print("-", table)

    print("\nApplication Ready!")