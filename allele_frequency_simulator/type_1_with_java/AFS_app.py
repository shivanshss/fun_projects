from flask import Flask, render_template, request, jsonify
import numpy as np
import plotly.express as px

app = Flask(__name__)

def simulate_allele_frequency(mutation_rate, starting_frequency, population_size, generations):
    allele_frequencies = [starting_frequency]
    for _ in range(generations):
        new_frequency = allele_frequencies[-1] * (1 - mutation_rate) + (1 - allele_frequencies[-1]) * mutation_rate
        allele_frequencies.append(new_frequency)
    return allele_frequencies

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def run_simulation():
    mutation_rate = float(request.form['mutation_rate'])
    starting_frequency = float(request.form['starting_frequency'])
    population_size = int(request.form['population_size'])
    generations = 100  # You can adjust the number of generations

    allele_frequencies = simulate_allele_frequency(mutation_rate, starting_frequency, population_size, generations)

    fig = px.line(x=range(generations + 1), y=allele_frequencies, labels={'x': 'Generation', 'y': 'Allele Frequency'})
    graph_json = fig.to_json()

    return jsonify(graph_json)

if __name__ == '__main__':
    app.run(debug=True)

