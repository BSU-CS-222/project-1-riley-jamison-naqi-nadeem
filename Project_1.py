import json
import ssl
from urllib.request import urlopen

def get_wikipedia_url(article_name):
    formatted_name = article_name.replace(' ', '%20')
    return f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles={formatted_name}&rvprop=timestamp|user&rvlimit=30&redirects"

def fetch_wikipedia_data(url):
    context = ssl._create_unverified_context()
    response = urlopen(url, context=context)
    return json.loads(response.read())

def display_recent_changes(article_name, data):
    if "query" in data:
        pages = data["query"]["pages"]
        for _, page_info in pages.items():
            if 'redirects' in data['query']:
                print(f"Redirected to {page_info['title']}")
            
            if "revisions" in page_info:
                for rev in page_info["revisions"]:
                    print(f"{rev['timestamp']} {rev['user']}")
                return 0
        print(f"No Wikipedia page found for {article_name}.")
        return 2
    else:
        print("Network error occurred.")
        return 3

def main():
    article_name = input("Please enter the Wikipedia article name: ").strip()
    
    if not article_name:
        print("You must provide an article name.")
        exit(1)
    
    
    url = get_wikipedia_url(article_name)
    data = fetch_wikipedia_data(url)
    exit_code = display_recent_changes(article_name, data)
    exit(exit_code)

if __name__ == "__main__":
    main()
