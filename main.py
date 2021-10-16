
import sys, os, json
import requests

user_agent_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



def get_url(tick: str):
    
    ticker = tick.upper()
    url = "https://query2.finance.yahoo.com"
    url = f"{url}/v8/finance/chart/{ticker}"

    r = requests.get(url, headers=user_agent_headers)
    response = r.json()

    print(json.dumps(response, indent=4))

    with open("tsla-stock.json", 'a') as f:
        json.dump(response, f)
    
    return 
    



def main():
    # tick = "TSLA"
    ticker = sys.argv[1]
    # print(f"\n\nALL ARGS:\n{tick[1]}\n\n")
    get_url(tick = ticker)


if __name__ == '__main__':
    main()