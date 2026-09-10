from flask import Flask, request, jsonify

app = Flask(__name__)
fake_crm_database = {}

@app.route("/api/customers", methods=["POST"])
def receive_customer():
    data = request.get_json()
    fake_crm_database[data["crm_id"]] = data
    print(f"[CRM] Received/updated customer: {data['full_name']}")
    return jsonify({"status": "success", "crm_id": data["crm_id"]}), 200

@app.route("/api/customers", methods=["GET"])
def list_customers():
    return jsonify(list(fake_crm_database.values()))

if __name__ == "__main__":
    app.run(port=5000, debug=True)