import argparse
import json
import requests

def reset_conversation():
    url_reset = "http://localhost:8080/reset"
    response = requests.request("POST", url_reset, headers=headers, data = payload)
    print(response)

def send_message(user_message):
    url = "http://localhost:8080/interact"
    response = requests.request("POST", url, headers=headers, data = user_message)
    response_json = json.loads(response.text.encode('utf8'))
    print(response_json['text'])
    return response_json['text']



if __name__ == '__main__':
    # Construct the argument parser
    ap = argparse.ArgumentParser()

    # Add the arguments to the parser
    ap.add_argument("-m", "--message", required=True,
       help="message to be sent to the bot")
    args = vars(ap.parse_args())
    payload = args['message']

    headers = {
      'Content-Type': 'application/json'
    }

    ### Reset conversation
    reset_conversation()

    ### Send Message
    send_message(payload)
