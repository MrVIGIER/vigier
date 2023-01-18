import requests
# Function to get current time of selected timezone
def get_time(timezone):
    url = "https://timeapi.io/api/Time/current/zone?timeZone="+timezone
    response = requests.request('GET', url, headers={}, data={})
    return response.json()
print(get_time('Europe/Paris'))
