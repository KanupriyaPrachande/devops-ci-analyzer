def detect_failure(error_lines):
    joined = " ".join(error_lines).lower()

    if "modulenotfounderror" in joined:
        return "Missing Dependency"
    elif "pytest" in joined or "test failed" in joined:
        return "Test Failure"
    elif "permission denied" in joined:
        return "Permission Issue"
    elif "no such file or directory" in joined:
        return "File Path Error"
    elif "docker build failed" in joined:
        return "Docker Build Error"
    else:
        return "Unknown Error"
