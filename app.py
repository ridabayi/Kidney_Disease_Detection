import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from CnnClassifier.pipeline.prediction import PredictionPipeline

# Initialize Flask App
app = Flask(__name__)
CORS(app)

# Set a max upload size (16MB)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Initialize your Prediction Pipeline
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

# Initialize once
clApp = ClientApp()

# Home Route
@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

# Train Route (optional)
@app.route("/train", methods=["GET", "POST"])
def trainRoute():
    os.system("python main.py")
    return "Training Done Successfully!"

# Predict Route
@app.route("/predict", methods=["POST"])
def predictRoute():
    try:
        # Check if file part is in the request
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        
        file = request.files['file']

        # Save the uploaded file
        file.save(clApp.filename)

        # Predict using your pipeline
        result = clApp.classifier.predict()

        # Send prediction back
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
