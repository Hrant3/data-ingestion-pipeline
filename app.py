# app.py
import os
import psycopg2
from psycopg2.extras import execute_values
from flask import Flask, request, jsonify
import datetime
import logging

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL')
print("Connecting to:", DATABASE_URL)

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

logging.basicConfig(level=logging.INFO)

def validate_data(data):
    required_fields = ['timestamp', 'user_id', 'session_id', 'metric_type', 'metric_value']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    try:
        datetime.datetime.fromisoformat(data['timestamp'])
    except ValueError:
        return False, "Invalid timestamp format"
    return True, ""

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    valid_data = []
    for d in data:
        is_valid, error_msg = validate_data(d)
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        valid_data.append(
            (
                datetime.datetime.fromisoformat(d['timestamp']),
                d['user_id'],
                d['session_id'],
                d['metric_type'],
                d['metric_value'],
                d.get('device_id'),
                d.get('app_version'),
                d.get('location'),
                d.get('sentiment_score')
            )
        )

    insert_query = """
        INSERT INTO metrics (timestamp, user_id, session_id, metric_type, metric_value, device_id, app_version, location, sentiment_score)
        VALUES %s
    """
    try:
        execute_values(cur, insert_query, valid_data)
        conn.commit()
    except Exception as e:
        conn.rollback()
        app.logger.error(f"Database error: {e}")
        return jsonify({"error": "Database error"}), 500

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
