from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    service_name = "web-app"
    status = "running"

    if request.method == "POST":
        service_name = request.form.get("service_name", "web-app").strip() or "web-app"
        status = request.form.get("status", "running")
        result = {
            "service_name": service_name,
            "status": status,
            "message": "Service is healthy." if status == "running" else "Check this service."
        }

    return render_template("index.html", result=result, service_name=service_name, status=status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
