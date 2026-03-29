import requests
import time

URL = "http://127.0.0.1:8000/twilio-webhook"


def test_latency():
    print("\n--- Latency Test ---")

    start = time.perf_counter()

    response = requests.post(
        URL,
        data={"SpeechResult": "check pnr", "CallSid": "CA123"}
    )

    end = time.perf_counter()

    print("Status Code:", response.status_code)
    print("Response Time:", (end - start) * 1000, "ms")


def test_load():
    print("\n--- Load Test ---")

    start = time.perf_counter()

    for i in range(10):
        response = requests.post(
            URL,
            data={"SpeechResult": "check pnr", "CallSid": f"CA{i}"}
        )
        print(f"Request {i+1}: {response.status_code}")

    end = time.perf_counter()

    print("Total Time:", end - start, "seconds")


if __name__ == "__main__":
    test_latency()
    test_load()