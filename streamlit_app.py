import streamlit as st

from components.state_manager import init_state


st.set_page_config(
    page_title="Python Programmer Explainer",
    page_icon=":material/code:",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_state()

pages = {
    "Python Foundations": [
        st.Page("pages/01_introduction.py", title="Introduction", icon=":material/waving_hand:"),
        st.Page("pages/02_operators.py", title="Operators", icon=":material/calculate:"),
        st.Page("pages/03_control_structures.py", title="Control Structures", icon=":material/account_tree:"),
        st.Page("pages/04_data_structures.py", title="Data Structures", icon=":material/data_object:"),
    ],
    "Program Design": [
        st.Page("pages/05_functions.py", title="Functions", icon=":material/function:"),
        st.Page("pages/06_modules_and_libraries.py", title="Modules and Libraries", icon=":material/extension:"),
        st.Page("pages/07_objects.py", title="Objects and Classes", icon=":material/category:"),
        st.Page("pages/08_try_except.py", title="Try / Except", icon=":material/report:"),
    ],
    "Modern Python": [
        st.Page("pages/09_pythonic_code.py", title="Pythonic Code", icon=":material/auto_fix_high:"),
        st.Page("pages/10_json_apis_and_environments.py", title="JSON, APIs, and Environments", icon=":material/api:"),
    ],
}

page = st.navigation(pages)
page.run()
