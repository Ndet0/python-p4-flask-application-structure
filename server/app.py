#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Home page route"""
    return 'Welcome to my page!'

@app.route('/<username>')
def user_profile(username):
    """Dynamic user profile route"""
    return f'Profile for {username}'
