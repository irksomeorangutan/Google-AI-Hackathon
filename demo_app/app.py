from flask import Flask, request
from controllers import handle_ping

app = Flask(__name__)

@app.route("/ping")
def ping():
    target = request.args.get("target")
    return handle_ping(target)

if __name__ == "__main__":
    app.run(debug=True)
