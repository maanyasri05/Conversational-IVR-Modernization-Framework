from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_welcome():
    response = client.post("/twilio-webhook", data={})
    assert response.status_code == 200
    assert "<Say>" in response.text
    assert "<Gather" in response.text


def test_pnr_intent():
    response = client.post(
        "/twilio-webhook",
        data={"SpeechResult": "check pnr", "CallSid": "CA123"}
    )
    assert response.status_code == 200
    assert "<Gather" in response.text


def test_train_intent():
    response = client.post(
        "/twilio-webhook",
        data={"SpeechResult": "train schedule", "CallSid": "CA123"}
    )
    assert response.status_code == 200
    assert "<Gather" in response.text


def test_book_ticket():
    response = client.post(
        "/twilio-webhook",
        data={"SpeechResult": "book ticket", "CallSid": "CA123"}
    )
    assert "booking" in response.text.lower()


def test_cancel_ticket():
    response = client.post(
        "/twilio-webhook",
        data={"SpeechResult": "cancel ticket", "CallSid": "CA123"}
    )
    assert "cancel" in response.text.lower()


def test_invalid_input():
    response = client.post(
        "/twilio-webhook",
        data={"SpeechResult": "random words", "CallSid": "CA123"}
    )
    assert "Sorry" in response.text


def test_full_pnr_flow():
    response = client.post(
        "/twilio-webhook",
        data={"SpeechResult": "check pnr", "CallSid": "CA123"}
    )
    assert "<Gather" in response.text

    response = client.post(
        "/process-pnr",
        data={"SpeechResult": "1234567890", "CallSid": "CA123"}
    )
    assert "<Say>" in response.text


def test_full_train_flow():
    response = client.post(
        "/twilio-webhook",
        data={"SpeechResult": "train schedule", "CallSid": "CA123"}
    )
    assert "<Gather" in response.text

    response = client.post(
        "/process-train",
        data={"SpeechResult": "12345", "CallSid": "CA123"}
    )
    assert "<Say>" in response.text


def test_end_call():
    response = client.post(
        "/twilio-webhook",
        data={"SpeechResult": "end call", "CallSid": "CA123"}
    )
    assert "Goodbye" in response.text


def test_full_ivr_flow():
    response = client.post(
        "/twilio-webhook",
        data={}, 
    )
    assert "<Say>" in response.text

    response = client.post(
        "/twilio-webhook",
        data={"SpeechResult": "check pnr", "CallSid": "CA123"}
    )
    assert "<Gather" in response.text

    response = client.post(
        "/process-pnr",
        data={"SpeechResult": "1234567890", "CallSid": "CA123"}
    )
    assert "<Say>" in response.text

    response = client.post(
        "/twilio-webhook",
        data={"SpeechResult": "end call", "CallSid": "CA123"}
    )
    assert "Goodbye" in response.text