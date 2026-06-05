# AI Weather Agent 🌦️

## Overview

AI Weather Agent is a Generative AI-powered weather assistant that provides real-time weather information and intelligent responses to user queries. Users can enter a city name and ask weather-related questions in natural language, and the AI agent retrieves live weather data and generates meaningful answers.

## Features

* Real-time weather data using OpenWeather API
* AI-powered question answering using Groq LLM
* FastAPI backend
* Streamlit frontend
* Natural language weather queries
* Cloud deployment support with Render and Streamlit Cloud

## Tech Stack

### Backend

* Python
* FastAPI
* LangChain
* Groq API
* OpenWeather API

### Frontend

* Streamlit

### Deployment

* Render
* Streamlit Cloud

## Project Structure

```text
AI_Weather_Agent/
│
├── Backend/
│   ├── main.py
│   ├── requirements.txt
│
├── Frontend/
│   └── app.py
|   |__ requirements.txt
│
└── README.md
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd AI_Weather_Agent
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file inside the Backend folder:

```env
weather_api_key=YOUR_OPENWEATHER_API_KEY
api_key=YOUR_GROQ_API_KEY
```

## Running Backend

```bash
uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

## Running Frontend

```bash
streamlit run app.py
```

Frontend runs at:

```text
[https://aiweatheragent.streamlit.app/](https://aiweatheragent.streamlit.app/)
```

## API Endpoint

### Get Weather

```http
POST /get_weather
```

Parameters:

| Parameter | Type   | Description           |
| --------- | ------ | --------------------- |
| city      | string | City Name             |
| question  | string | User Weather Question |

Example:

```text
City: Hyderabad
Question: Should I carry an umbrella today?
```

## Example Queries

* What is the temperature in Hyderabad?
* Is it raining in Delhi?
* Should I carry an umbrella in Mumbai today?
* Is the weather suitable for outdoor activities in Chennai?

## Deployment

### Backend Deployment

Deploy the FastAPI backend on Render.

Start Command:

```bash
uvicorn Backend.main:app --host 0.0.0.0 --port $PORT
```

### Frontend Deployment

Deploy Streamlit frontend on Streamlit Cloud.

Add secret:

```toml
backend_url="[https://your-render-backend-url.onrender.com](https://ai-weather-agent-75lb.onrender.com)"
```

## Future Enhancements

* Multi-day weather forecast
* Weather alerts and notifications
* Voice-based weather assistant
* Location auto-detection
* Weather analytics dashboard

## Author

**Jeegari Thirumal**

