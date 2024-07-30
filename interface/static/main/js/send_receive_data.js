const socket = new WebSocket('ws://127.0.0.1:8001/ws/pension/');

socket.onmessage = (e) => {
    data = JSON.parse(e.data);
    document.querySelector(".result-income-value").innerText = data.pension;
}

socket.onclose = (e) => {
    alert("Something went wrong. Please try again later.")
}

const numberInputs = document.querySelectorAll(".number-input--controls input");
const checkedRadioInputs = document.querySelectorAll('input[type="radio"]');
const allInputs = [...numberInputs, ...checkedRadioInputs];

allInputs.forEach(input => {
    input.addEventListener("change", async () => {
        const data = getInputsData();
        socket.send(JSON.stringify(data));
    });
});

function getInputsData(){
    const inputs = [
        ...document.querySelectorAll(".number-input--controls input"),
        ...document.querySelectorAll('input[type="radio"]:checked')
    ]
    let data = {};

    inputs.forEach(input => {
        data[input.name] = input.value;
    });

    return data;
}