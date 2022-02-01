const inputs = document.querySelectorAll("input");

let places;
let index;

function setPlaces() {
  places = [];

  inputs.forEach((input) => {
    if (input.checked) {
      places.push(...data[input.id]);
    }
  });

  for (let index = places.length - 1; index > 0; index--) {
    const randomIndex = Math.floor(Math.random() * (index + 1));
    [places[index], places[randomIndex]] = [places[randomIndex], places[index]];
  }

  index = 0;
}

inputs.forEach((input) => {
  input.addEventListener("change", () => {
    setPlaces();
  });
});

setPlaces();

function setResult() {
  const result = document.querySelector("#result");
  const place = places[index++ % places.length];

  result.style.backgroundColor = `hsl(${[0, 30, 90, 210, 270][place["category"]]}, 75%, 75%)`;

  result.innerHTML = `
    <div class="h-10">${place["name"]}</div>
    <div class="mt-10 h-10">${place["location"]}</div>
    <div class="h-10">${place["hours"]}</div>
  `;
}

document.querySelector("button").addEventListener("click", () => {
  setResult();
});
