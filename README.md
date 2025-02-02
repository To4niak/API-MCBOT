# API-MCBOT

This is an API for MCBOT that allows remote request control for launching Minecraft bot attacks.

## Features
- Start bot-based attacks on Minecraft servers remotely.
- Secure API with an API key.
- Logging of all attack requests.
- Supports multiple attack methods.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/api-mcbot.git
   cd api-mcbot
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the API server:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

## API Usage

### Endpoint: Start Attack
**URL:** `/start-attack`  
**Method:** `POST`  
**Content-Type:** `application/json`

#### Request Body:
```json
{
  "ip_port": "36.90.48.40:25577",
  "protocol": 47,
  "method": "join",
  "seconds": 60,
  "target_cps": 1000,
  "api_key": "your_secret_api_key"
}
```

#### Response Example:
```json
{
  "status": "Attack started",
  "details": {
    "ip_port": "36.90.48.40:25577",
    "protocol": 47,
    "method": "join",
    "seconds": 60,
    "target_cps": 1000,
    "api_key": "your_secret_api_key"
  }
}
```

## Security
- The API requires a valid API key to prevent unauthorized usage.
- Make sure to keep your API key private.

## Logs
All attack requests are logged in `attack.log` for monitoring.

## Disclaimer
This tool is intended for **educational purposes only** or for **testing your own server**. Misuse of this API for unauthorized attacks is strictly prohibited.

## License
MIT License

