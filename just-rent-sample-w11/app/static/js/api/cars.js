document.addEventListener('DOMContentLoaded', function () {
    let carId = document.querySelector('#carId').value
    fetchData(carId)
})

function fetchData(carId) {
    fetch("http://127.0.0.1:5000/api/cars/" + carId)
        .then(function (response) {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(function (car) {
            update(car)
        })
        .catch(function (error) {
            console.error('There was a problem with the fetch operation:', error);

        })
}
function update(car) {
    document.querySelector('.d-value[data-spec="body"]').textContent = car.body;
    document.querySelector('.d-value[data-spec="seats"]').textContent = car.seats;
    document.querySelector('.d-value[data-spec="door"]').textContent = car.door

}