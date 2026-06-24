import streamlit as st
from intent import extract_intent
from design import generate_design
from schema import generate_schema
from validator import validate
from repair import repair
import json

st.set_page_config(page_title="AI App Compiler", layout="wide")
st.title("🚀 AI App Compiler")
st.markdown("Convert natural language prompts into application blueprints")

prompt = st.text_area("Enter your app prompt:", height=100, placeholder="e.g., Build Hospital Management System with login dashboard reports notification search")

if st.button("Generate Blueprint", type="primary"):
    if not prompt.strip():
        st.error("Please enter a prompt")
    else:
        with st.spinner("Generating blueprint..."):
            try:
                intent = extract_intent(prompt)
                st.info(f"✓ Intent Detected: {intent['app_type']} App")
                
                design = generate_design(intent)
                st.info(f"✓ Design Generated: {len(design['flows'])} flows detected")
                
                schema = generate_schema(design)
                st.info(f"✓ Schema Generated")
                
                valid, missing = validate(schema)
                if not valid:
                    st.warning(f"⚠ Validation Issues: {missing}")
                    schema = repair(schema)
                    st.info("✓ Auto-repair applied")
                else:
                    st.success("✓ Validation Passed")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("📋 Generated Blueprint")
                    st.json(schema)
                
                with col2:
                    st.subheader("🎯 Application Overview")
                    st.write("**Pages:**")
                    for page in schema["ui"]["pages"]:
                        st.write(f"  • {page}")
                    
                    st.write("**Entities:**")
                    for table in schema["database"]["tables"]:
                        st.write(f"  • {table}")
                    
                    st.write("**API Endpoints:**")
                    for api in schema["api"]["endpoints"]:
                        st.write(f"  • {api['path']} ({', '.join(api['methods'])})")
                    
                    st.write("**Roles:**")
                    for role in schema["auth"]["roles"]:
                        st.write(f"  • {role}")
                
                st.success("✅ Blueprint Generated Successfully!")
                
                json_str = json.dumps(schema, indent=2)
                st.download_button(
                    label="Download Blueprint (JSON)",
                    data=json_str,
                    file_name="blueprint.json",
                    mime="application/json"
                )
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.error("Please check your prompt and try again")