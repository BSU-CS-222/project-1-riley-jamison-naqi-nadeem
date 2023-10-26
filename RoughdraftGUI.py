import tkinter as tk
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
                string = ""  # empty string
                for rev in page_info["revisions"]:
                    timestamp = rev["timestamp"]
                    user = rev["user"]
                    string = string + timestamp + "   " + user + "\n"
                return string
        return f"No Wikipedia page found for {article_name}.\n"
    else:
        return "Network error occurred."
    
def display_recent_changesGUI(article_name, data, text_result, text_result2, text_result3, text_result4):
    if "query" in data:
        pages = data["query"]["pages"]
        for _, page_info in pages.items():
            if 'redirects' in data['query']:
                redirect_message = f"Redirected to {page_info['title']}"
                text_result2["text"] = redirect_message 
                return

            if "revisions" in page_info:
                stringInfo = ""  # empty string
                for rev in page_info["revisions"]:
                    timestamp = rev["timestamp"]
                    user = rev["user"]
                    stringInfo = stringInfo + timestamp + "   " + user + "\n"
                text_result["text"] = stringInfo #text_result holds the user and time edits
                return

        text_result3["text"] = f"No Wikipedia page found for {article_name}."
    else:
        text_result4["text"] = "Network error occurred."
    
def main():
    article_name = input("Please enter the Wikipedia article name: \n").strip()
    
    if not article_name:
        print("You must provide an article name.\n")
        return
    
    url = get_wikipedia_url(article_name)
    data = fetch_wikipedia_data(url)
    result = display_recent_changes(article_name, data)
    
    if result == "No Wikipedia page found for article_name.\n":
        print(result)
    elif result == "Network error occurred.":
        print(result)
    else:
        print(result)

def mainGUI():
    article_name = entry1.get().strip()
    
    if not article_name:
        no_entry = "You must provide an article name."
        text_result3["text"] = no_entry
        return
        
    url = get_wikipedia_url(article_name)
    data = fetch_wikipedia_data(url)
    result = display_recent_changesGUI(article_name, data, text_result, text_result2, text_result3, text_result4)

    if result == "No Wikipedia page found for article_name.\n":
        text_result4["text"] = result
    elif result == "Network error occurred.":
        text_result5["text"] = result

def TKGUI():
    window = tk.Tk()
    window.title("Find Wikipedia Edits")
    window.geometry("600x600")
    lbl1 = tk.Label(window, text="Enter a Wikipedia Page")
    global entry1, text_result, text_result2, text_result3, text_result4, text_result5
    entry1 = tk.Entry(window)
    text_result = tk.Label(window)
    text_result2 = tk.Label(window)
    text_result3 = tk.Label(window)
    text_result4 = tk.Label(window)
    text_result5 = tk.Label(window)
    btnSearch = tk.Button(window, text="Search Edits", command=mainGUI)

    lbl1.grid(column=0, row=0)
    entry1.grid(column=1, row=0)
    btnSearch.grid(column=0, row=2)
    text_result.grid(column=2, row=2)
    window.mainloop()

while True:
    print("Choose an option:")
    print("1) Search Through Command Line")
    print("2) Search Through GUI")
    print("3) Quit")

    option = input()

    if option == "1": 
        main()  

    elif option == "2":
        TKGUI()

    elif option == "3":
        print("Goodbye")
        break
