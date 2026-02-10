#!/usr/bin/env python
import os
import sys
import django
import requests
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "loan_system_project.settings")
django.setup()

# Test the registration endpoint
test_data = {
    "full_name": "John Manager",
    "email": "john@example.com",
    "phone": "+254712345678",
    "role": "MANAGER",
    "password": "SecurePass123",
}

print("Testing Registration Endpoint...")
print(f"URL: http://127.0.0.1:8000/api/auth/register/")
print(f"Data: {json.dumps(test_data, indent=2)}")
print("\n" + "=" * 50 + "\n")

try:
    response = requests.post(
        "http://127.0.0.1:8000/api/auth/register/",
        json=test_data,
        headers={"Content-Type": "application/json"},
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

    if response.status_code == 201:
        print("\n✓ Registration successful!")
    else:
        print(f"\n✗ Registration failed!")

except Exception as e:
    print(f"Error: {str(e)}")
