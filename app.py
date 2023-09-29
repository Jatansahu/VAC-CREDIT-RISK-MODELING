from flask import Flask, render_template
from waitress import serve

app= Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')


# # @app.route('/style.css')
# # def index():
# #     return ('style.html')


# if __name__ == '__main__':
#     # from waitress import serve
#     # serve(app, host="0.0.0.0", port=8080)r
#     app.run(debug=True)


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the form data
    age = int(request.form['age'])
    duration = int(request.form['duration'])
    installment_rate = int(request.form['installment_rate'])
    residence_since = int(request.form['residence_since'])
    existing_credits = int(request.form['existing_credits'])
    credit_amount = int(request.form['credit_amount'])
    existing_checkout = request.form['existing_checkout']
    credit_history = request.form['credit_history']
    purpose = request.form['purpose']
    savings_acc = request.form['savings_acc']
    emp_duration = request.form['emp_duration']
    sex_status = request.form['sex_status']
    property_ = request.form['property']
    installment_plan = request.form['installment_plan']
    housing = request.form['housing']
    foreign_worker = request.form['foreign_worker']

    # Perform credit risk modeling calculations
    # Customize this part to implement your specific credit risk modeling algorithm

    # Example logic: If age > 18 and credit_amount < 5000, consider it a good account
    is_good_account = age > 18 and credit_amount < 5000

    # Render the result template with the loan approval result
    return render_template('result.html', is_good_account=is_good_account)

if __name__ == '__main__':
    app.run()
