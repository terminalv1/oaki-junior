
from flask import Flask, send_file, render_template_string, request, redirect, url_for, session
import os
import glob
import json

app = Flask(__name__)
app.secret_key = 'your_super_secret_key'
META_FILE = '/home/pi/timelapse/metadata.json'

def load_metadata():
    if os.path.exists(META_FILE):
        with open(META_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_metadata(data):
    with open(META_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/', methods=['GET', 'POST'])
def index():
    metadata = load_metadata()
    if request.method == 'POST':
        filename = request.form['filename']
        tag = request.form.get('tag', '').strip()
        note = request.form.get('note', '').strip()
        if filename not in metadata:
            metadata[filename] = {}
        metadata[filename]['tag'] = tag
        metadata[filename]['note'] = note
        save_metadata(metadata)
        return redirect(url_for('index'))

    query = request.args.get('q', '').lower()
    filter_type = request.args.get('type', 'all')
    filter_date = request.args.get('date', '')

    all_files = sorted(glob.glob('/home/pi/timelapse/*.jpg'))
    snapshots = [f for f in all_files if 'motion' not in f]
    motions = [f for f in all_files if 'motion' in f]

    if query:
        snapshots = [f for f in snapshots if query in os.path.basename(f).lower()]
        motions = [f for f in motions if query in os.path.basename(f).lower()]

    if filter_type == 'snapshots':
        motions = []
    elif filter_type == 'motions':
        snapshots = []

    if filter_date:
        snapshots = [f for f in snapshots if filter_date in os.path.basename(f)]
        motions = [f for f in motions if filter_date in os.path.basename(f)]

    snapshots = [os.path.basename(f) for f in snapshots]
    motions = [os.path.basename(f) for f in motions]

    return render_template_string("""
    <style>
      body { font-family: sans-serif; padding: 1em; }
      img { max-width: 100%; height: auto; }
      input[type=text], input[type=password], select { width: 100%; padding: 8px; margin: 5px 0; }
      button { padding: 10px; margin-top: 5px; width: 100%; }
      form { margin-bottom: 1em; }
      @media (min-width: 768px) {
        button { width: auto; }
        input[type=text], input[type=password], select { width: auto; }
      }
    </style>
    <h1>Timelapse & Motion Viewer with Tags</h1>
    {% if session.get("admin") %}
      <p><b>Logged in as admin</b> | <a href="/logout">Logout</a></p>
    {% else %}
      <p><a href="/login">Admin Login</a></p>
    {% endif %}

    <h2>Latest Image</h2>
    <img src="/latest.jpg" width="600"><br><br>

    <h2>🔋 PiJuice Power Status</h2>
    <div id="powerData">Loading...</div>
    <script>
    fetch('/power')
      .then(res => res.json())
      .then(data => {
        if (data.error) {
          document.getElementById("powerData").innerText = "Error: " + data.error;
        } else {
          document.getElementById("powerData").innerText = 
            "Battery: " + data.BatteryLevel + 
            "\nVoltage: " + (data.Voltage || "N/A") +
            "\nStatus: " + JSON.stringify(data.Status, null, 2);
        }
      })
      .catch(err => {
        document.getElementById("powerData").innerText = "Error fetching power status.";
      });
    </script>
    """, snapshots=snapshots, motions=motions, metadata=metadata)

@app.route('/power')
def power_status():
    try:
        from pijuice import PiJuice
        pj = PiJuice(1, 0)
        status = pj.status.GetStatus()['data']
        charge = pj.status.GetChargeLevel()['data']
        voltages = pj.status.GetBatteryVoltage()['data']
        return {
            "BatteryLevel": f"{charge}%",
            "Status": status,
            "Voltage": voltages
        }
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/latest.jpg')
def latest_image():
    return send_file('/home/pi/timelapse/latest.jpg', mimetype='image/jpeg')

@app.route('/timelapse/<filename>')
def serve_snapshot(filename):
    path = os.path.join('/home/pi/timelapse', filename)
    return send_file(path, mimetype='image/jpeg')

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        password = request.form.get('password', '')
        if password == 'admin123':
            session['admin'] = True
            return redirect(url_for('index'))
        else:
            msg = 'Incorrect password'
    return '''
    <h2>Admin Login</h2>
    <form method="post">
        <input type="password" name="password" placeholder="Password">
        <button type="submit">Login</button>
        <p style="color:red;">{}</p>
    </form>
    '''.format(msg)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

app.run(host='0.0.0.0', port=8000)
