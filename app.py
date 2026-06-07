import joblib
import pandas as pd
from flask import Flask, render_template, request, jsonify
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

# LOAD DATASET (PICKLE)
df = pd.read_pickle("adult_dataset.pkl")

# LOAD MODEL & ENCODERS
model = joblib.load("salary_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")
target_encoder = joblib.load("target_encoder.pkl")

# PLACEHOLDER INPUT
PLACEHOLDER_INPUT = {
    "age": 25,
    "workclass": "Private",
    "fnlwgt": 226802,
    "education": "11th",
    "educational-num": 7,
    "marital-status": "Never-married",
    "occupation": "Machine-op-inspct",
    "relationship": "Own-child",
    "race": "Black",
    "gender": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States"
}

# ROUTE: MAIN PAGE
@app.route("/")
def index():
    return render_template(
        "index.html",
        encoders={k: list(v.classes_) for k, v in label_encoders.items()},
        placeholder=PLACEHOLDER_INPUT
    )

# ROUTE: PREDICT
@app.route("/predict")
def predict():

    input_data = {}

    for col in PLACEHOLDER_INPUT:
        val = request.args.get(col, PLACEHOLDER_INPUT[col])

        if col in label_encoders:
            input_data[col] = val
        else:
            input_data[col] = float(val)

    input_df = pd.DataFrame([input_data])

    for col in label_encoders:
        input_df[col] = label_encoders[col].transform(input_df[col])

    pred = model.predict(input_df)[0]
    salary = target_encoder.inverse_transform([pred])[0]

    # Simple summary table (placeholder-style)
    table = [{
        "Field": "Predicted Income",
        "Value": salary
    }]

    return jsonify({
        "table": table,
        "prediction": salary
    })

@app.route("/service-status", methods=["GET"])
def status():
    return jsonify({
        "status": "ok",
        "service": "Employee Salary Prediction Service API"
    })

if __name__ == "__main__":
    app.run()
