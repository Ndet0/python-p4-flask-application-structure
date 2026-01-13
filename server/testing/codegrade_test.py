#!/usr/bin/env python3

import pytest
from flask import Flask
from server.app import app

class TestFlaskApp:
    """Test suite for Flask application routes and structure"""
    
    def test_app_instance_creation(self):
        """Test that Flask app instance is created correctly"""
        assert app is not None
        assert isinstance(app, Flask)
    
    def test_index_route(self):
        """Test that index route returns correct content"""
        client = app.test_client()
        response = client.get('/')
        assert response.status_code == 200
        assert b'Welcome to my page!' in response.data
    
    def test_dynamic_username_route(self):
        """Test that dynamic username route works correctly"""
        client = app.test_client()
        response = client.get('/NASA')
        assert response.status_code == 200
        assert b'Profile for NASA' in response.data
    
    def test_dynamic_username_route_with_different_user(self):
        """Test dynamic route with different username"""
        client = app.test_client()
        response = client.get('/TestUser')
        assert response.status_code == 200
        assert b'Profile for TestUser' in response.data

