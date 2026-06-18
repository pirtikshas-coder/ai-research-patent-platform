function searchAI() {

    let query = document.getElementById("query").value;

    fetch("/search", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            query: query
        })
    })

    .then(response => response.json())

    .then(data => {

        document.getElementById("resultBox").innerHTML = `

        <h2>${query}</h2>

        <p>${data.result}</p>

        <hr>

        <h3>Related Papers</h3>

        <ul>
            <li>AI Applications in Healthcare</li>
            <li>Future of Artificial Intelligence</li>
            <li>Machine Learning Trends</li>
        </ul>

        <h3>Patent Opportunities</h3>

        <ul>
            <li>Smart Diagnostic Systems</li>
            <li>AI-powered Education Platforms</li>
            <li>Predictive Analytics Engines</li>
        </ul>

        `;
    })

    .catch(error => {
        console.log(error);
    });
}


// Research Analytics Chart

const chartCanvas = document.getElementById("researchChart");

if (chartCanvas) {

    new Chart(chartCanvas, {

        type: "line",

        data: {

            labels: [
                "2021",
                "2022",
                "2023",
                "2024",
                "2025"
            ],

            datasets: [

                {
                    label: "Research Growth",

                    data: [
                        100,
                        250,
                        450,
                        700,
                        1000
                    ],

                    borderWidth: 3,

                    tension: 0.4
                }

            ]
        },

        options: {

            responsive: true,

            plugins: {

                legend: {
                    labels: {
                        color: "white"
                    }
                }

            },

            scales: {

                x: {
                    ticks: {
                        color: "white"
                    }
                },

                y: {
                    ticks: {
                        color: "white"
                    }
                }

            }
        }
    });

}
function downloadReport(){

let content =
document.getElementById("resultBox").innerText;

let blob =
new Blob([content],
{type:"text/plain"});

let a =
document.createElement("a");

a.href =
URL.createObjectURL(blob);

a.download =
"Research_Report.txt";

a.click();

}