from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_file', methods=['POST'])
def create_file():
    if request.method == 'POST':
        data = request.json  # Get JSON data from the request
        name = data.get('name', 'default_name')  # Extract 'name' from JSON data, or use a default name if not provided

        # Write JSON data to a text file
        with open(f"{name}.txt", "w") as f:
            f.write(json.dumps(data, indent=4))  # Convert JSON data to a string and write to file

        # Return a response to acknowledge the successful request
        return jsonify(data), 200

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5001,
        debug=True
    )