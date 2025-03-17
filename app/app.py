from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status='ok'), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

