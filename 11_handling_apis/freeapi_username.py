import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')
def fetch_random_user_freeapi():
    url = 'https://api.freeapi.app/api/v1/public/randomusers'
    
    querystring = {"page": "1", "limit": "10"}
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()  # important

    data = response.json()
    print(data)
    if data.get('success') and 'data' in data:
        users = data['data']          # this is a LIST
        user_data = users[0]          # pick first user

        username = user_data['login']['username']
        country = user_data['location']['country']

        return username, country
    else:
        raise Exception('Failed to fetch data')
    

def main():
    try:
        username, country = fetch_random_user_freeapi()
        print("\nUsername:", username)
        print("Country:", country)
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()