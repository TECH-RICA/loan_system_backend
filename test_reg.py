#!/usr/bin/env python3
import requests
import json

data = {
    "full_name": "Test User",
    "email": "testuser@example.com",
    "phone": "+254712345678",
    "role": "MANAGER",
    "password": "TestPass123",
}

print("Testing registration...")
print(f"Data: {json.dumps(data, indent=2)}")
print("\n" + "=" * 50 + "\n")

try:
    response = requests.post(
        "http://127.0.0.1:8000/api/auth/register/", json=data, timeout=30
    )

    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")

except Exception as e:
    print(f"Error: {str(e)}")
