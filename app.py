import argparse
import json

from runtime import simulate
from repair import repair
from intent import extract_intent
from design import generate_design
from schema import generate_schema
from validator import validate


def main():
    parser = argparse.ArgumentParser(description="AI App Compiler")
    parser.add_argument("-p", "--prompt", type=str, help="Natural language prompt")
    parser.add_argument("-o", "--output", type=str, default="output.json", help="Output JSON file")
    args = parser.parse_args()

    prompt = args.prompt
    if not prompt:
        prompt = input("Enter Prompt: ").strip()

    if not prompt:
        print("No prompt provided. Exiting.")
        return

    intent = extract_intent(prompt)
    print("Intent Generated")

    design = generate_design(intent)
    print("Design Generated")

    schema = generate_schema(design)
    print("Schema Generated")

    valid, missing = validate(schema)
    if not valid:
        print("Validation Failed")
        print("Missing:", missing)
        schema = repair(schema)
        print("Repair Applied")
    else:
        print("Validation Passed")

    print("\nFinal JSON Output:\n")
    print(json.dumps(schema, indent=4))

    with open(args.output, "w") as f:
        json.dump(schema, f, indent=4)

    print(f"Saved to {args.output}")
    simulate(schema)


if __name__ == "__main__":
    main()
