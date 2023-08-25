function runSimulation() {
    const mutationRate = parseFloat(document.getElementById('mutation-rate').value);
    const startingFrequency = parseFloat(document.getElementById('starting-frequency').value);
    const populationSize = parseInt(document.getElementById('population-size').value);

    fetch('/simulate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `mutation_rate=${mutationRate}&starting_frequency=${startingFrequency}&population_size=${populationSize}`,
    })
    .then(response => response.json())
    .then(graphData => {
        const graphDiv = document.getElementById('graph');
        Plotly.newPlot(graphDiv, JSON.parse(graphData), {});
    });
}

