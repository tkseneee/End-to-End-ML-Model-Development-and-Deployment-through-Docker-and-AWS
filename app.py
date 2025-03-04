import flask
import pickle
import numpy as np
import os
import sklearn

# Load the saved pipeline dictionary
with open('full_pipeline', 'rb') as f:
    pipeline = pickle.load(f)

# Extract the pipelines and the model from the dictionary
numeric_pipeline = pipeline['numeric_pipeline']
categorical_pipeline = pipeline['categorical_pipeline']
model = pipeline['model']

# Initialize the Flask app
app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Render the form with default values
        return flask.render_template('main.html', original_input={}, result=None)
    
    if flask.request.method == 'POST':
        # Safely extract form data using .get()
        Married = flask.request.form.get('Married')
        Education = flask.request.form.get('Education')
        ApplicantIncome_val = flask.request.form.get('ApplicantIncome')
        LoanAmount_val = flask.request.form.get('LoanAmount')
        Credit_History_val = flask.request.form.get('Credit_History')
        
        # Check for missing inputs
        if None in [Married, Education, ApplicantIncome_val, LoanAmount_val, Credit_History_val]:
            return flask.render_template('main.html', original_input={}, result="Missing input data. Please fill in all fields.")
        
        # Convert numeric fields to float
        try:
            ApplicantIncome = float(ApplicantIncome_val)
            LoanAmount = float(LoanAmount_val)
            Credit_History = float(Credit_History_val)
        except ValueError:
            return flask.render_template('main.html', original_input={}, result="Invalid numeric input. Please enter valid numbers.")
        
        # Create numpy arrays for the categorical and numeric inputs
        # First two columns are categorical and next three are numeric.
        categorical_input = np.array([[Married, Education]], dtype=object)
        numeric_input = np.array([[ApplicantIncome, LoanAmount, Credit_History]])
        
        try:
            # Transform the inputs using the saved pipelines
            categorical_transformed = categorical_pipeline.transform(categorical_input).toarray()
            numeric_transformed = numeric_pipeline.transform(numeric_input)
            
            # Concatenate the transformed features.
            # This order should match the one used during training: categorical features first, then numeric.
            test_input = np.concatenate([categorical_transformed, numeric_transformed], axis=1)
            
            # Get the prediction from the model
            prediction = model.predict(test_input)[0]
            prediction_percentage = f"{prediction * 100:.2f}%"
        except Exception as e:
            return flask.render_template('main.html', original_input={}, result="Error during processing: " + str(e))
        
        # Prepare a dictionary of the original inputs to display
        original_input = {
            'Married': Married,
            'Education': Education,
            'ApplicantIncome': ApplicantIncome,
            'LoanAmount': LoanAmount,
            'Credit_History': Credit_History
        }
        
        return flask.render_template('main.html', original_input=original_input, result=prediction_percentage)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
