document.getElementById('random_player_button').addEventListener('click', function() {
    fetch('/nba/random_player')
    .then(response => response.json())
    .then(data => {
        const playerName = data.name;  // Player's name from the API
            const playerId = data.id;  // Player's unique ID from the API

            // Construct the image URL dynamically
            const playerImageUrl = `https://cdn.nba.com/headshots/nba/latest/260x190/${playerId}.png`;

            // Update the text and image
            document.getElementById("player_name").textContent = playerName;
            const playerImg = document.getElementById("player_image");

            // Update the image source with the constructed URL
            playerImg.src = playerImageUrl;
            playerImg.style.display = "block";
    })
    .catch(error => console.error('Error:', error));
});