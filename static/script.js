async function loadChart(containerId, jsonPath) {
    try {
        const response = await fetch(jsonPath);
        if (!response.ok) throw new Error("Chart not found");

        const fig = await response.json();
        Plotly.newPlot(containerId, fig.data, fig.layout, { responsive: true });

    } catch (err) {
        console.error(err);
        document.getElementById(containerId).innerHTML =
            "<p style='color:red;text-align:center;'>Chart failed to load</p>";
    }
}

// Load charts (static JSON)
loadChart("chart1", "/static/charts/income_distribution.json");
loadChart("chart2", "/static/charts/age_vs_income.json");
loadChart("chart3", "/static/charts/education_vs_income.json");

// Prediction
function runPrediction() {

    const params = new URLSearchParams();

    document.querySelectorAll(".controls input, .controls select")
        .forEach(el => {
            params.append(el.id, el.value);
        });

    fetch(`/predict?${params.toString()}`)
        .then(res => res.json())
        .then(data => renderTable(data.table))
        .catch(err => {
            console.error(err);
            alert("Prediction failed");
        });
}

function renderTable(rows) {
    let html = `
    <table class="data-table">
        <tr>
            <th>Field</th>
            <th>Value</th>
        </tr>`;

    rows.forEach(r => {
        html += `
        <tr>
            <td>${r.Field}</td>
            <td class="${r.Value.includes('>') ? 'bad' : 'good'}">${r.Value}</td>
        </tr>`;
    });

    html += "</table>";
    document.getElementById("table").innerHTML = html;
}