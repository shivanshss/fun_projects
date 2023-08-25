from flask import Flask, render_template, request
import numpy as np
import plotly.express as px
import io
import base64

app = Flask(__name__)

def simulate_allele_frequency(mutation_rate, starting_frequency, population_size, generations, drift_variance):
    allele_frequencies = [starting_frequency]
    for _ in range(generations):
        if allele_frequencies[-1] == 0:
            allele_frequencies.append(0)
            break
        elif allele_frequencies[-1] == 1:
            allele_frequencies.append(1)
            break

        noise = np.random.normal(0, drift_variance)
        new_frequency = allele_frequencies[-1] * (1 - mutation_rate) + (1 - allele_frequencies[-1]) * mutation_rate + noise
        new_frequency = max(0, min(1, new_frequency))
        allele_frequencies.append(new_frequency)

    return allele_frequencies

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mutation_rate = max(0, min(0.00001, float(request.form['mutation_rate'])))
        starting_frequency = max(0, min(1, float(request.form['starting_frequency'])))
        population_size = int(request.form['population_size'])
        generations = max(0, min(10000, int(request.form['generations'])))
        drift_variance = max(0, float(request.form['drift_variance']))

        allele_frequencies = simulate_allele_frequency(mutation_rate, starting_frequency, population_size, generations, drift_variance)

        end_message = None
        if allele_frequencies[-1] == 0:
            end_message = "EXTINCT!"
        elif allele_frequencies[-1] == 1:
            end_message = "YOU WON THE GAME OF GENETICS!"

        fig = px.line(x=range(len(allele_frequencies)), y=allele_frequencies, labels={'x': 'Generation', 'y': 'Allele Frequency'})
        img_bytes = io.BytesIO()
        fig.write_image(img_bytes, format='png')
        img_data = base64.b64encode(img_bytes.getvalue()).decode('utf-8')

        return render_template('index.html', img_data=img_data, end_message=end_message)
    
    return render_template('index.html', img_data=None, end_message=None)

if __name__ == '__main__':
    app.run(debug=True)

