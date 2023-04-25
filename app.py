from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/predict_rejection', methods=['POST'])
def predict():
    # Get the request data
    data = request.form
    Amount = float(data['Amount'])
    B2B = int(data['B2B'])
    Category = int(data['Category'])
    Fulfilment = int(data['Fulfilment'])
    Size = int(data['Size'])
    region = int(data['region'])

    # Create a test array with the input features
    test_array = ([[Amount, B2B, Category, Fulfilment, Size, region]])

    # Predict the rejection using the `predicted_rejection` function
    def predicted_rejection(test_array):
        rejection = rf_model.predict(test_array)
        rejection = np.around(rejection, 2)
        return rejection

    rejection = predicted_rejection(test_array)

    # Return the result as a JSON object
    if rejection == [1]:
        result = {'result': 'Product was rejected by customer due to high pricing'}
    elif rejection == [0]:
        result = {'result': 'Product was rejected by customer due to negative reviews'}
    else:
        result = {'result': 'Unable to predict rejection'}

    return jsonify(result)

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
