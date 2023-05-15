from flask import Flask, render_template, request

app = Flask(__name__)

# load the model
import pickle

file = open("xgb_model.pkl", 'rb')
model = pickle.load(file)
file.close()


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route("/predict", methods=["GET"])
def predict():
    gender = int(request.args.get('gender'))
    age = int(request.args.get('age'))
    license = int(request.args.get('license'))
    region = int(request.args.get('region'))
    insured = int(request.args.get('insured'))
    Vehicle_age = int(request.args.get('Vehicle_age'))
    damage = int(request.args.get('damage'))
    Anuual_premium = float(request.args.get('Anuual_premium'))
    channel = int(request.args.get('channel'))
    vintage = int(request.args.get('vintage'))


    predictions = model.predict([[gender, age, license, region, insured, Vehicle_age, damage, Anuual_premium, channel, vintage]])
    result = f"Customer May {'' if predictions[0] == 1 else 'NOT'} Purchase The Insurance"
    return render_template("index.html",  prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)