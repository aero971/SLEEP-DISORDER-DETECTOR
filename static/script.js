
    document.getElementById('predictionForm').addEventListener('submit', async function(e) {
        e.preventDefault();
        const feature1 = document.querySelector('input[name="feature1"]:checked').value;
        const feature2 = document.getElementById('age').value;
        const feature3 = document.getElementById('occupation').value;
        const feature4 = document.getElementById('sleepDuration').value;
        const feature5 = document.getElementById('qualityOfSleep').value;
        const feature6 = document.getElementById('physicalActivity').value;
        const feature7 = document.getElementById('stressLevel').value;
        const feature8 = document.querySelector('input[name="feature8"]:checked').value;
        const feature9 = document.getElementById('bloodPressureHigher').value;
        const feature10 = document.getElementById('bloodPressureLower').value;
        const feature11 = document.getElementById('heartRate').value;
        const feature12 = document.getElementById('dailySteps').value;

        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10, feature11, feature12 })
        });

        const data = await response.json();
        const resultDiv = document.getElementById('result');
        if (data.prediction) {
            let advicePoints;
            switch(data.prediction) {
                case "No sleep disorder":
                    advicePoints = [
                        "Maintain a regular sleep schedule",
                        "Create a restful environment",
                        "Limit caffeine and alcohol intake",
                        "Stay physically active",
                        "Practice relaxation techniques"
                    ];
                    break;
                case "Sleep disorder: Sleep Apnea":
                    advicePoints = [
                        "Maintain a healthy weight",
                        "Avoid alcohol and smoking",
                        "Use a continuous positive airway pressure (CPAP) machine",
                        "Sleep on your side",
                        "Practice good sleep hygiene"
                    ];
                    break;
                case "Sleep disorder: Insomnia":
                    advicePoints = [
                        "Maintain a regular sleep schedule",
                        "Create a comfortable sleep environment",
                        "Avoid stimulants before bedtime",
                        "Use relaxation techniques",
                        "Seek cognitive behavioral therapy for insomnia (CBT-I)"
                    ];
                    break;
                default:
                    advicePoints = [];
            }
            resultDiv.innerHTML = `<div class="alert alert-info">
                <h4>Prediction: ${data.prediction}</h4>
                <ul>
                    ${advicePoints.map(point => `<li>${point}</li>`).join('')}
                </ul>
            </div>`;
        } else {
            resultDiv.innerHTML = `<div class="alert alert-danger">Error: ${data.error}</div>`;
        }
    });

