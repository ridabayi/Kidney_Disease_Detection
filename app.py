import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from CnnClassifier.utils.common import decodeImage
from CnnClassifier.pipeline.prediction import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    # os.system("dvc repro")
    return "Training done successfully!"


@app.route("/heatmap", methods=['POST'])
@cross_origin()
def heatmapRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    
    # Generate heatmap logic here
    heatmap_data = clApp.classifier.generate_heatmap()  # Placeholder for heatmap generation logic
    return jsonify({"heatmap": heatmap_data})



if __name__ == "__main__":
    clApp = ClientApp()

    app.run(host='0.0.0.0', port=8080) #for AWS
