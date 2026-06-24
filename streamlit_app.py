import streamlit as st
from intent import extract_intent
from design import generate_design
from schema import generate_schema
from validator import validate
from repair import repair
import json

st.set_page_config(page_title="AI App Compiler", layout="wide")

if "prompt" not in st.session_state:
    st.session_state.prompt = ""

sample_prompts = [
    "Build Hospital Management System with login dashboard reports notification search",
    "Create an Ecommerce application with login checkout payment and search",
    "Develop a Student Portal with login dashboard courses and notifications"
]

with st.sidebar:
    st.title("AI App Compiler")
    st.write("Generate app blueprints from natural language requirements.")
    st.write("### Example prompts")
    for sample in sample_prompts:
        if st.button(sample, key=sample):
            st.session_state.prompt = sample
    st.markdown("---")
    st.write("### How to use")
    st.write("1. Enter a prompt describing the app you want.")
    st.write("2. Click Generate Blueprint.")
    st.write("3. Download the generated JSON blueprint.")

st.title("🚀 AI App Compiler")
st.markdown("Convert natural language prompts into application blueprints for UI, API, database, and auth.")

prompt = st.text_area(
    "Enter your app prompt:",
    value=st.session_state.prompt,
    height=140,
    placeholder="e.g., Build Hospital Management System with login dashboard reports notification search"
)

generate = st.button("Generate Blueprint", type="primary")

if generate:
    if not prompt.strip():
        st.error("Please enter a prompt before generating a blueprint.")
    else:
        st.session_state.prompt = prompt
        with st.spinner("Generating blueprint..."):
            try:
                intent = extract_intent(prompt)
                design = generate_design(intent)
                schema = generate_schema(design)

                valid, missing = validate(schema)
                if not valid:
                    schema = repair(schema)
                    validation_message = f"⚠ Validation issues found and repaired: {missing}"
                    st.warning(validation_message)
                else:
                    st.success("✓ Validation passed")

                st.success("✅ Blueprint Generated Successfully!")

                col1, col2 = st.columns([2, 1])
                with col1:
                    st.subheader("📋 Generated Blueprint")
                    st.json(schema)
                with col2:
                    st.subheader("🎯 Application Overview")
                    st.markdown(f"**Detected app type:** {intent['app_type']}")
                    st.markdown("**Pages**")
                    for page in schema["ui"]["pages"]:
                        st.write(f"- {page}")
                    st.markdown("**Entities**")
                    for table in schema["database"]["tables"]:
                        st.write(f"- {table}")
                    st.markdown("**API Endpoints**")
                    for api in schema["api"]["endpoints"]:
                        st.write(f"- `{api['path']}`: {', '.join(api['methods'])}")
                    st.markdown("**Roles**")
                    for role in schema["auth"]["roles"]:
                        st.write(f"- {role}")

                json_str = json.dumps(schema, indent=2)
                st.download_button(
                    label="Download Blueprint (JSON)",
                    data=json_str,
                    file_name="blueprint.json",
                    mime="application/json"
                )

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.error("Please check your prompt and try again.")