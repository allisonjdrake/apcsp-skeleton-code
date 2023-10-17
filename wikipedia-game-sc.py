from queue import Queue
import wikipediaapi
import time

user_agent = "Allison'sWikipediaGame/1.0 (dr1453al0618@pusd.us)"

wiki_wiki = wikipediaapi.Wikipedia(user_agent, "en")
    #en = english, can change language to whatever (i.e. es or kor)

# HELPER FUNCTION: fetch_links(page) passes in a wikipedia page and returns a list of all the pages linked from that page
def fetch_links(page):
    links_list = []
    #puts all links connected and puts it into a variable
    links = page.links
    for title in sorted(links.keys()):
        links_list.append(title)
        #only add the title for the link, we don't care about the URL of each actual link
        
    return links_list

#IN CLASS: Finish the definition of the wikipedia_game_solver using a Breadth-First-Search Traversal
def wikipedia_game_solver(start_page, target_page):
    print('Working on it...')
    start_time = time.time()
  
    visited = []
    queue = Queue()
    path = []

    visited.append(start_page.title)
    
    while not queue.empty():
        
    #queue.get() gets the first thing in the queue
    #queue.put() puts something at the end of the queue


    end_time = time.time()
    print("This algorithm took", end_time-start_time, "seconds to run!")
  
    return path

# Example usage:
start_page = wiki_wiki.page('Nina Tandon')
target_page = wiki_wiki.page('Italian language')
path = wikipedia_game_solver(start_page, target_page)
print("Shortest path:", path)

