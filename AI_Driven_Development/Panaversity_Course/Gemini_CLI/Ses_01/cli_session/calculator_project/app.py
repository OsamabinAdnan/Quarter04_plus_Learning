from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    try:
        # Basic and unsafe evaluation for demonstration.
        # In a real application, use a safer math expression parser.
        result = str(eval(expression))
    except Exception as e:
        result = 'Error'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
