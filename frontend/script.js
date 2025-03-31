document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("prediction-form");
    const resultDiv = document.getElementById("result");
    const loadingDiv = document.getElementById("loading");
    const predictBtn = document.getElementById("predict-btn");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();
        
        // Show loading state
        loadingDiv.style.display = 'flex';
        resultDiv.style.display = 'none';
        predictBtn.disabled = true;
        
        const data = {
            container_memory_working_set_bytes: parseFloat(document.getElementById("memory_working_set").value),
            container_memory_usage_bytes: parseFloat(document.getElementById("memory_usage").value),
            container_file_descriptors: parseFloat(document.getElementById("file_descriptors").value),
            container_network_receive_bytes_rate: parseFloat(document.getElementById("network_receive_rate").value),
            total_header_bytes: parseFloat(document.getElementById("total_header").value)
        };

        try {
            const response = await fetch("http://127.0.0.1:8000/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                body: JSON.stringify(data)
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
            
            // Format the results exactly as in your original script
            const podFailureProb = result.prediction[0][0];
            const networkIssueProb = result.prediction[0][1];
            
            resultDiv.textContent = `Prediction: Pod Failure - ${podFailureProb}, Network Issue - ${networkIssueProb}`;
            resultDiv.className = "result-container result-success";
            
        } catch (error) {
            console.error("Error:", error);
            resultDiv.textContent = "Error: Could not fetch prediction";
            resultDiv.className = "result-container result-error";
        } finally {
            loadingDiv.style.display = 'none';
            resultDiv.style.display = 'block';
            predictBtn.disabled = false;
        }
    });
});
