import random
import string
from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'radadadadaadadadaddad'


if __name__ == '__main__':
    app.run(debug=True)

shortened_urls = {}
