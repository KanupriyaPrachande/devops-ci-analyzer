import streamlit as st
from log_parser import parse_logs
from pattern_detector import detect_failure
from fix_suggester import suggest_fix_gpt

st.title("🚀 Intelligent CI/CD Failure Analyzer")

st.write("Paste your GitHub Actions failure logs below:")

log_text = st.text_area("CI/CD Logs", height=300)

if st.button("Analyze Failure"):
    if log_text.strip() == "":
        st.warning("Please paste logs first.")
    else:
        error_lines = parse_logs(log_text)
        failure_type = detect_failure(error_lines)
        fix = suggest_fix_gpt(failure_type, error_lines)

        st.subheader("🔍 Detected Failure Type")
        st.success(failure_type)

        st.subheader("🤖 AI Suggested Fix")
        st.info(fix)

        st.subheader("📄 Error Lines Found")
        for line in error_lines:
            st.code(line)
