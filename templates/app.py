from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form inputs
        holiday = int(request.form['holiday'])
        temp = float(request.form['temp'])
        rain = float(request.form['rain'])
        snow = float(request.form['snow'])
        weather = int(request.form['weather'])
        year = int(request.form['year'])
        month = int(request.form['month'])
        day = int(request.form['day'])
        hours = int(request.form['hours'])
        minutes = int(request.form['minutes'])
        seconds = int(request.form['seconds'])

        # Dummy estimation logic instead of model prediction:
        estimated_traffic = (
            (temp * 10) +
            (rain * 100) +
            (snow * 150) +
            (weather * 5) +
            ((24 - hours) * 20) + 
            (minutes + seconds) / 10 +
            holiday * 30 +
            month * 5 +
            day * 2
        )
        return redirect(url_for('result', prediction=round(estimated_traffic, 2)))

    except Exception as e:
        return f"Error: {e}"

@app.route('/result')
def result():
    prediction = request.args.get('prediction', None)
    if prediction is None:
        return redirect(url_for('home'))
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
