const sliderWrappers = document.querySelectorAll(".input-slider__input");

sliderWrappers.forEach((wrapper) => {
    const numberInput = wrapper.querySelector('input[type="number"]');
    const slider = wrapper.querySelector('input[type="range"]');

    slider.value = numberInput.value;

    numberInput.addEventListener("change", (e) => {
        const validValue = validateNumberValue(
            numberInput.min*1,
            numberInput.max*1,
            e.target.value
        );
        numberInput.value = validValue;
        slider.value = validValue;
    });

    slider.addEventListener("input", (e) => {
        numberInput.value = e.target.value;
        numberInput.dispatchEvent(new Event('change'));
    });
});

function validateNumberValue(min, max, value){
    if (!Number(value)) return min;
    if (value*1 < min) return min;
    if (value*1 > max) return max;

    return value*1;
}