import streamlit as st
import subprocess

def run_python_code(code):
    try:
        result = subprocess.run(['python', '-c', code], capture_output=True, text=True, timeout=5)
        return result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return None, "Error: Execution timed out."

def main():
    st.title("Johnny's Online Python Interpreter")

    code = st.text_area("Enter Python code here:", height=300)

    if st.button("Run Code"):
        st.text("Output:")
        output, error = run_python_code(code)

        if output:
            st.code(output, language="python")
        elif error:
            st.error(error)
        else:
            st.warning("No output.")

if __name__ == "__main__":
    main()
