#!/usr/bin/env python3
"""Quick script to get ClickUp user IDs for Jamie and Pepper"""
import os
from clickup_client import ClickUpClient

# Get Jamie's ID (principal)
principal_key = os.environ.get('CLICK_UP_API_KEY_PRINCIPAL')
if principal_key:
    client_principal = ClickUpClient(api_key=principal_key)
    user_principal = client_principal.get_current_user()
    print(f"Jamie (principal):")
    print(f"  User ID: {user_principal['id']}")
    print(f"  Username: {user_principal['username']}")
    print(f"  Email: {user_principal['email']}")
    print()

# Get Pepper's ID (assistant)
assistant_key = os.environ.get('CLICK_UP_API_KEY_ASSISTANT')
if assistant_key:
    client_assistant = ClickUpClient(api_key=assistant_key)
    user_assistant = client_assistant.get_current_user()
    print(f"Pepper (assistant):")
    print(f"  User ID: {user_assistant['id']}")
    print(f"  Username: {user_assistant['username']}")
    print(f"  Email: {user_assistant['email']}")
