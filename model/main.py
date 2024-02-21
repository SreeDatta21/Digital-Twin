from flask import Flask, request, render_template, jsonify
import subprocess
import pandas as pd
import time

app = Flask(__name__)
data = pd.read_excel(r'C:\Users\hp\OneDrive\Documents\Book1.xlsx')
current_row = 0

# Serve static CSS files
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/datta', methods=['POST'])
def datta():
    try:
        # Use subprocess to execute the Python script
        # print("here")
        result = subprocess.check_output(['python', 'gain.py'], universal_newlines=True, stderr=subprocess.STDOUT)
       # print("here1")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return result
@app.route('/work', methods=['POST'])
def work():
    try:
        # Use subprocess to execute the Python script
       # print("here")
        result = subprocess.check_output(['python', 'gain.py'], universal_newlines=True, stderr=subprocess.STDOUT)
        # print("here1")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return result

if __name__ == "__main__":
    app.run(debug=True)