// Simple polling to update chat messages every 2 seconds
setInterval(async () => {
    const response = await fetch('/get_objects');
    const data = await response.json();
    const chatDiv = document.getElementById('chat');
    chatDiv.innerHTML = ''; // clear previous messages

    for (const [obj, count] of Object.entries(data)) {
        const p = document.createElement('p');
        p.textContent = `Detected ${obj}: ${count}`;
        chatDiv.appendChild(p);
    }
}, 2000);
