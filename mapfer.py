import requests
import base64
import json
import argparse


def get_bearer_token(conkey, consec):
    TWITTER_URL = 'https://api.twitter.com/oauth2/token'

    cred = conkey + ':' + consec

    headers = {
        'authorization': b'Basic ' + base64.b64encode(cred.encode('ascii')),
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    data = {
        'grant_type': 'client_credentials'
    }

    res = requests.post(TWITTER_URL, headers=headers, data=data)
    res = res.json()

    return res['access_token']


def main(args):
    with open(args.file, 'r') as token_file:
        tokens = json.load(token_file)
        bearer = get_bearer_token(tokens['conkey'], tokens['consec'])


if __name__ == '__main__':
    desc = 'Mining and visualising user location data from Twitter.'
    hlp = 'the path to JSON file containing the consumer tokens'

    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('file', metavar='path', help=hlp)
    main(parser.parse_args())
