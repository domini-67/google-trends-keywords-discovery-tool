thonimport requests

def parse_trends(keyword):
    url = f"https://trends.google.com/trends/api/explore?q={keyword}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve trends for {keyword}")
    
    trends_data = response.json()
    return trends_data['default']['trendingSearches']