const text = "tes";
const url = "https://model-ml-7vvpza7dfa-et.a.run.app"; // Ganti URL dengan URL API ML Model yang sesuai

fetch(url, {
    method: "POST",
    headers: {
        "Content-Type": "application/x-www-form-urlencoded"
    },
    body: `sentence=${encodeURIComponent(text)}`
})
    .then(response => response.json())
    .then(jsonResponse => {
        const prediction = jsonResponse.prediction;
        console.log(jsonResponse);
    })
    .catch(error => {
        console.error("Error dalam mengirimkan permintaan ke model machine learning:", error);
    });