
import sys, os, json
import requests



def write_data(json_data):
    """ Function will write json to filename. """


def get_url(tick: str):
    """ Takes a stock tick and makes request aganist finance API """
    user_agent_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    base_url = "https://query2.finance.yahoo.com"
    url = f"{base_url}/v8/finance/chart/{tick.upper()}"

    r = requests.get(url, headers=user_agent_headers)
    response = r.json()
    return response    


def main():
    ticker = sys.argv[1]
    get_url(tick = ticker)


if __name__ == '__main__':
    main()