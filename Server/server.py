from flask import request,Flask , jsonify,render_template
app = Flask(__name__)
import util
util.load_saved_artifacts()

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/api/get_location_names',methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

@app.route('/api/predict_home_price',methods = ['POST'])
def predict_home_price():
    try:
        total_sqrft = float(request.form["total_sqft"])
        location = request.form["location"]
        bhk = int(request.form["bhk"])
        bath = int(request.form["bath"])

        estimated_price = util.get_prediction(location, total_sqrft, bhk, bath)

        response = jsonify({"estimated_price": estimated_price})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    except Exception as e:
        print("🔥 Error in prediction:", e)
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    print("running flask server")
    app.run()