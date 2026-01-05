def suggest_fix_gpt(failure_type, error_lines):
    context = " ".join(error_lines)

    if failure_type == "Missing Dependency":
        return f"""
The CI pipeline failed due to a missing Python dependency.

🔍 Error Context:
{context}

✅ Suggested Fix:
- Add the missing module to requirements.txt
- Run `pip install -r requirements.txt`
- Commit and re-run the pipeline
"""

    elif failure_type == "Test Failure":
        return f"""
The pipeline failed because test cases did not pass.

🔍 Error Context:
{context}

✅ Suggested Fix:
- Identify failing test cases
- Fix logic or update expected outputs
- Re-run CI
"""

    elif failure_type == "Permission Issue":
        return """
The pipeline failed due to insufficient file permissions.

✅ Suggested Fix:
- Add `chmod +x <script_name>` in your GitHub Actions workflow
"""

    else:
        return """
Unable to confidently classify this error.

✅ Suggested Fix:
- Review logs manually
- Add new failure patterns to the analyzer
"""
