from flask import Flask, url_for,request, jsonify,render_template
import joblib

app = Flask(__name__)

@app.route("/")
def index():
     return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def predict():
    # Check if request has a JSON content
    if request.json:
        # Get the JSON as dictionnary
        req = request.get_json()
        # Check mandatory key
        if "input" in req.keys():
            # Load model
            classifier = joblib.load("./models/model.joblib")
            # Predict
            prediction = classifier.predict(req["input"])
            # Return the result as JSON but first we need to transform the
            # result so as to be serializable by jsonify()
            prediction = str(prediction[0])
            return jsonify({"predict": prediction}), 200
    return jsonify({"msg": 
    'il faut envoyer une requete POST de type'
    """ input_simple = {'input': [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]} """
    })

 
if __name__ == "__main__":
    app.run(debug=True)

