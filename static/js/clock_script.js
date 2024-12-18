function updateClock() {
    const now = new Date();
    const date = now.toLocaleDateString('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
    });
    const time = now.toLocaleTimeString();

    const clock = document.getElementById('clock');
    clock.innerHTML = `${date} | ${time}`;
}

// Update the clock every second
setInterval(updateClock, 1000);

// Initial call to display the time immediately
updateClock();