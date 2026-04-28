from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "password"),
        database=os.getenv("DB_NAME", "autodeploydb")
    )

@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "message": "AutoDeploy Hub is Live!"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
