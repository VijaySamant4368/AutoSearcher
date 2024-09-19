import time
import webbrowser
import random

import sys
n = len(sys.argv)

def main():
        # Help
    if '-h' in sys.argv or '--help' in sys.argv:
        print_help()
        sys.exit(0)
    
    try:
        browser_arg_index = sys.argv.index('-b') + 1    #browser
        browser_path = sys.argv[browser_arg_index]
    except ValueError:      #If there is no -b
        browser_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" #Your own browser path

    try:
        file_arg_index = sys.argv.index('-f') + 1       #File with queries separated with newline
        file_path = sys.argv[file_arg_index]
        with open(file_path, 'r') as file:
            queries = file.readlines()
    except ValueError:      #If there is no -f
        try:
            query_arg_index = sys.argv.index('-q') + 1       #FTotal number of queries to search. Ignored if file location is given
            total_queries = int(sys.argv[query_arg_index])
        except ValueError:  #-q not given, or no character/str given as -q arg
            total_queries = 10
        queries = [generate_random_word(3) for _ in range(total_queries)]

    try:
        engine_arg_index = sys.argv.index('-e') + 1     #Search engine to use
        engine = sys.argv[engine_arg_index]
    except ValueError:      #If there is no -e
        engine  = "https://www.bing.com"

    try:
        wait_arg_index = sys.argv.index('-w') + 1     #Wait time between subsequent searches in sec
        wait = int(sys.argv[wait_arg_index])
    except ValueError:      #If there is no -w, or a str/char passed as -w argument
        wait = 3
        
    for search_query in queries: 

        url = f"{engine}/search?q={search_query}"
        webbrowser.register('browser', None, webbrowser.BackgroundBrowser(browser_path))

        # Open Microsoft Edge and search
        webbrowser.get('browser').open_new_tab(url)
        time.sleep(wait)


def generate_random_syllable():
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    return random.choice(consonants) + random.choice(vowels) + random.choice(consonants)

def generate_random_word(length):
    return ''.join(generate_random_syllable() for _ in range(length))

def print_help():
    help_message = """
Usage: python main.py [options]

Options:
  -b <path>     Path to the browser executable. Default is "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe".
  -f <file>     Path to a file containing queries (one per line). If not provided, use -q to specify a number of queries.
  -q <number>   Total number of random queries to generate if -f is not given. Default is 10.
  -e <engine>   Search engine URL to use for searches. Default is "https://www.bing.com".
  -w <seconds>  Wait time (in seconds) between subsequent searches. Default is 3.

Example:
  python main.py -b "C:\\Path\\To\\Browser.exe" -f queries.txt -e "https://www.google.com" -w 5
"""
    print(help_message)


if __name__ == "__main__":
    main()