from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    
    full_name = "Santhosh D V"  
    username = os.getenv("USER") or os.getenv("USERNAME")
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')

   
    try:
        top_output = subprocess.check_output("top -b -n 1 | head -15", shell=True, text=True)
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

   
    return f"""
    <html>
    <head><title>/htop Endpoint</title></head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time:</strong> {server_time}</p>
        <h2>Top Output</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
