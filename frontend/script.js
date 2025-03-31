document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("prediction-form");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();
        
        const data = {
            container_memory_working_set_bytes: parseFloat(document.getElementById("memory_working_set").value),
            container_memory_usage_bytes: parseFloat(document.getElementById("memory_usage").value),
            container_file_descriptors: parseFloat(document.getElementById("file_descriptors").value),
            container_network_receive_bytes_rate: parseFloat(document.getElementById("network_receive_rate").value),
            total_header_bytes: parseFloat(document.getElementById("total_header").value)
        };

        try {
            const response = await fetch("http://127.0.0.1:5500/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            const result = await response.json();
            resultDiv.textContent = `Prediction: Pod Failure - ${result.prediction[0][0]}, Network Issue - ${result.prediction[0][1]}`;
            resultDiv.style.color = "green";
        } catch (error) {
            resultDiv.textContent = "Error: Could not fetch prediction";
            resultDiv.style.color = "red";
            console.error("Error:", error);
        }
    });
});
