# Conversational IVR Modernization Framework

## Overview

This project presents a modernized Interactive Voice Response (IVR) system by integrating conversational AI with a scalable backend. The system replaces traditional keypad-based navigation with intelligent voice interaction, enabling users to access railway services such as PNR status and train schedules efficiently.

---

## Objectives

* Enhance user experience through natural voice interaction
* Replace rigid IVR menus with dynamic conversational flow
* Integrate backend services for real-time data retrieval
* Deploy a scalable and accessible cloud-based solution

---

## Key Features

* Voice-based interaction using Twilio
* Intent detection for user queries
* PNR status retrieval
* Train schedule information
* Dynamic conversational flow handling
* Error handling for invalid inputs
* Optimized response time and performance

---

## System Architecture

* **Voice Interface:** Twilio
* **Backend:** FastAPI (Python)
* **Logic Layer:** Intent detection engine
* **Data Layer:** Backend service APIs
* **Deployment:** Render

---

## System Workflow

1. User initiates a call via Twilio
2. Twilio triggers the webhook endpoint
3. FastAPI processes the speech input
4. Intent detection module identifies user intent
5. Backend services fetch required information
6. Response is formatted and returned as TwiML
7. Twilio converts response to speech for the user

---

## Deployment

The application is deployed on a cloud platform for continuous availability.

Live Application URL:
https://conversational-ivr-modernization-nzvv.onrender.com

Webhook Endpoint:
https://conversational-ivr-modernization-nzvv.onrender.com/twilio-webhook

---

## Testing

* Unit Testing
* Integration Testing
* End-to-End Testing
* Performance Testing

---

## Performance

* Average response time: < 100 ms (core processing)
* Stable performance under multiple requests
* Accurate intent recognition and conversational flow

---

## Tech Stack

* Python
* FastAPI
* Twilio
* Render
* Pytest

---

## Setup and Execution

### Clone Repository

```bash
git clone https://github.com/maanyasri05/Conversational-IVR-Modernization-Framework.git
cd Conversational-IVR-Modernization-Framework
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn main:app --reload
```

### Configure Twilio

* Set webhook URL to deployed endpoint
* Use HTTP POST method

### Test Call

```bash
python make_call.py
```

---

## Key Achievements

* Implemented conversational IVR using voice interaction
* Integrated backend services for real-time responses
* Deployed application on cloud with public access
* Ensured system reliability through testing

---

## Future Enhancements

* Multi-language support
* Advanced NLP-based intent detection
* Integration with live railway data
* User authentication and personalization

---

## Author

V. Maanya Sri Sai
B.Tech Student

---

## Conclusion

This project demonstrates the transformation of traditional IVR systems into intelligent conversational platforms, delivering improved usability, scalability, and real-time responsiveness.

