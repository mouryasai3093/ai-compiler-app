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

st.markdown(
    """
    <style>
    .hero-box {
        background: linear-gradient(135deg, #7c83fd 0%, #cb74ff 100%);
        padding: 24px;
        border-radius: 18px;
        color: white;
        box-shadow: 0 30px 80px rgba(124, 131, 253, 0.18);
        margin-bottom: 24px;
    }
    .hero-box h1 {
        margin: 0;
        font-size: 2.5rem;
    }
    .hero-box p {
        margin: 8px 0 0;
        font-size: 1.05rem;
        opacity: 0.92;
    }
    </style>
    <div class='hero-box'>
        <h1>AI App Compiler</h1>
        <p>Generate app blueprints from natural language prompts with UI, API, database, and auth definitions.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

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

                app_metrics, result_panel = st.columns([1, 2])
                with app_metrics:
                    st.metric("Pages", len(schema["ui"]["pages"]))
                    st.metric("Entities", len(schema["database"]["tables"]))
                    st.metric("API Endpoints", len(schema["api"]["endpoints"]))
                    st.metric("Roles", len(schema["auth"]["roles"]))

                with result_panel:
                    st.subheader("📋 Generated Blueprint")
                    st.json(schema)

                with st.expander("View summary details"):
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