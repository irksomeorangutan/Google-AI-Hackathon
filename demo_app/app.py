from flask import Flask, request
from controllers import handle_ping
import os

app = Flask(__name__)

@app.route("/ping")
def ping():
    target = request.args.get("target")
    return handle_ping(target)

if __name__ == "__main__":
    # Debug mode is enabled only if the DEBUG environment variable is set to "true"
    app.run(debug=(os.environ.get("DEBUG") == "true"))