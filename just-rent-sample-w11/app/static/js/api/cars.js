document.addEventListener('DOMContentLoaded', function () {
    fetchData()
})

function fetchData() {
    fetch("http://127.0.0.1:5000/api/cars/22")
        .then(function (response) {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(function (data) {
            update(data)
        })
        .catch(function (error) {
            console.error('There was a problem with the fetch operation:', error);

        })
}
function update(data) {
    document.querySelector('.d-value[data-spec="body"]').textContent = data.body;
    document.querySelector('.d-value[data-spec="seats"]').textContent = data.seats;
    document.querySelector('.d-value[data-spec="door"]').textContent = data.door

}