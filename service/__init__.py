"""Flask service used for the CI/CD final project."""
import os

from flask import Flask, jsonify

app = Flask(__name__)

# The lab grader expects this marker in the application container logs.
print("SERVICERUNNING on port 8000", flush=True)


@app.route("/")
def index():
    """Return service metadata."""
    return jsonify(
        status="SERVICERUNNING",
        message="CI/CD final project service is running",
        port=int(os.environ.get("PORT", "8000")),
    )


@app.route("/health")
def health():
    """Simple readiness endpoint."""
    return jsonify(status="OK"), 200
