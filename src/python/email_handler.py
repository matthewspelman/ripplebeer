from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for development

RESEND_API_KEY = "re_aW3zNY8B_LUwkyzqLFBwQ3sr3TVsJfpnT"
RESEND_API_URL = "https://api.resend.com/emails"

@app.route('/subscribe', methods=['POST', 'OPTIONS'])
def subscribe():
    if request.method == 'OPTIONS':
        return '', 200
        
    try:
        data = request.json
        print("Received data:", data)  # Debug log
        email = data.get('email')
        
        if not email:
            return jsonify({'error': 'Email is required'}), 400

        # Send email using Resend API directly
        headers = {
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json"
        }
        
        email_data = {
            "from": "Ripple Beer Co. <ripplebeerco@gmail.com>",
            "to": ["ripplebeerco@gmail.com"],
            "subject": "New Subscriber - Ripple Beer Co.",
            "html": f"""
                <h2>New Subscriber</h2>
                <p>Email: {email}</p>
                <p>Signed up from the Ripple Beer Co. website</p>
            """
        }

        response = requests.post(RESEND_API_URL, headers=headers, json=email_data)
        print("Resend API response:", response.status_code, response.text)  # Debug log

        if response.status_code == 200:
            return jsonify({'message': 'Successfully subscribed!'}), 200
        else:
            return jsonify({'error': 'Failed to send email'}), 500

    except Exception as e:
        print("Error:", str(e))  # Debug log
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True) 