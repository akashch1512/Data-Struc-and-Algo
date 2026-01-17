import requests
import json

url = "http://1.208.108.242:63650/api/generate/"

payload = {
    "model": "llama3:8b-instruct-q4_K_M",
    "prompt": "What is FastAPI?"
}

# Basic authentication credentials
auth = ("user", "1")  # Using OPEN_BUTTON_TOKEN as password

try:
    with requests.post(url, json=payload, auth=auth, stream=True, timeout=300) as r:
        r.raise_for_status()
        final = ""

        for line in r.iter_lines(decode_unicode=True):
            if not line:
                continue
            data = json.loads(line)
            if "response" in data:
                final += data["response"]
            if data.get("done"):
                break

    print(final)

except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
    print(f"Response content: {r.text}")  # Print the response content for debugging
except Exception as e:
    print(f"An error occurred: {e}")