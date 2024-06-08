from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('model')

# Dictionary to map prediction results to descriptive statements
prediction_statements = {
    0: "Great !👍 You are currently <div='fr'> not showing signs of sleep disorder🌜.</div>",
    1: "Ohh ho !🙄You are showing signs of <div='fr'> SLEEP APNEA🐺. </div>",
    2: "Ohh ho !😕 You are showing signs of <div='fr'> INSOMNIA🦉. </div>"
}

# Dictionary to map prediction results to advice points
advice_points = {
    0: [
        "Keep a consistent ⏰ bedtime 🛌",
        "Make your bedroom quiet 🌜 and dark 🌃",
        "Avoid caffeine and heavy🚫☕ meals before bed.",
        "Walk or exercise daily 🚶‍♂️ 🏋️ ",
        "Drink plenty of water🫗 throughout the day, but limit intake before bed"
    ],
    1: [
        "Maintain a consistent sleep routine ⏰ 🛌",
        "Avoid alcohol and smoking🚫🍺🚭",
        "Stay hydrated🫗, but avoid large amounts of water before bedtime.",
        "stablish a wind-down routine⏰, such as reading a book or taking a warm bath🚿",
        "Practice good sleep hygiene🛏️"
    ],
    2: [
        "Try herbal teas🍵🥬 like chamomile or valerian root before bed.",
        "Create a comfortable sleep environment🌃 🛏️",
        "Establish a relaxing bedtime routine (e.g., taking a warm bath🚿 or reading📖).",
        "Avoid screens (phones, tablets, computers)📵 an hour before bedtime.",
        "Drink water regularly during the day to stay hydrated🫗"
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # Get the input data as JSON
        input_data = [data.get('feature1'), data.get('feature2'), data.get('feature3'), data.get('feature4'), data.get('feature5'), data.get('feature6'), data.get('feature7'), data.get('feature8'), data.get('feature9'), data.get('feature10'), data.get('feature11'), data.get('feature12')]  # Adjust based on your model's input
        prediction = model.predict([input_data])[0]
        if prediction in prediction_statements:
            prediction_statement = prediction_statements[prediction]
            advice = advice_points[prediction]
            return jsonify({'prediction': prediction_statement, 'advice': advice})
        else:
            return jsonify({'error': 'Unable to determine sleep disorder.'})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
