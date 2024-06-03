from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# Suppose we have this token for simplification
ACCESS_TOKEN = "your-secure-token"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        if token != ACCESS_TOKEN:
            return jsonify({'message': 'Invalid token!'}), 403
        return f(*args, **kwargs)
    return decorated

@app.route('/generate_fusion_text', methods=['POST'])
@token_required
def generate_fusion_text():
    data = request.get_json()
    # Your logic for generating fusion text goes here
    return jsonify({'message': 'Fusion text generated successfully!', 'data': data})

@app.route('/embedding', methods=['POST'])
@token_required
def embedding():
    data = request.get_json()
    # Your logic for embedding goes here
    return jsonify({'message': 'Embedding successful!', 'data': data})

@app.route('/generate_image', methods=['POST'])
@token_required
def generate_image():
    data = request.get_json()
    # Your logic for generating image goes here
    return jsonify({'message': 'Image generated successfully!', 'data': data})

if __name__ == '__main__':
    app.run(debug=True)