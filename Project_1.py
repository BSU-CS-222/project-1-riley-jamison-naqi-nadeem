import json
import ssl
from urllib.request import urlopen

def get_recent_changes_url(article_name):
    base_url = f"https://en.wikipedia.org/w/api.php"
    query_params = (
        f"action=query&format=json&prop=revisions&titles={article_name}"
        f"&rvprop=timestamp|user&rvlimit=30&redirects"
    )
    full_url = f"{base_url}?{query_params}"
    return full_url

def get_recent_changes_data(changes_url):
    context = ssl._create_unverified_context()
    response = urlopen(changes_url, context=context)
    return json.loads(response.read())

def display_recent_changes(data, article_name):
    if "query" in data:
        pages = data["query"]["pages"]
        for _, page_info in pages.items():  #Over here page id is not a used variable, but for clean code practices unpacked using the "_" which is apparantly normal
            if 'redirects' in data['query']:
                print(f"Redirected to {page_info['title']}")
            
            if "revisions" in page_info:
                for rev in page_info["revisions"]:
                    print(f"{rev['timestamp']} {rev['user']}")
            else:
                print(f"No Wikipedia page found for {article_name}.")
                return 2
    else:
        print("Network error occurred.")
        return 3
    return 0

def main():
    article_name = input("Please enter the Wikipedia article name: ").strip()
    
    if not article_name:
        print("You must provide an article name.")
        exit(1)
    
    changes_url = get_recent_changes_url(article_name)
    data = get_recent_changes_data(changes_url)
    exit_code = display_recent_changes(data, article_name)
    exit(exit_code)

if __name__ == "__main__":
    main()
