import streamlit as st
from tools import outline, characters, timeline

def main():
    # Page configuration
    st.set_page_config(
        page_title="Book Writer Toolkit",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # App header
    st.title("Book Writer Toolkit")

    # Sidebar menu
    st.sidebar.header("Tools")
    tool = st.sidebar.selectbox(
        "Choose a tool",
        [
            "Outline Generator",
            "Character Database",
            "Plot Timeline",
        ],
    )

    # Route to the selected tool
    if tool == "Outline Generator":
        outline.show()
    elif tool == "Character Database":
        characters.show()
    elif tool == "Plot Timeline":
        timeline.show()
    else:
        st.error("Unknown tool selected.")

if __name__ == "__main__":
    main()
