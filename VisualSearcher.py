import webbrowser
import os
import pyautogui
import time

def main():
    queries = [generate_random_word(3) for _ in range(10)]

    # Define the search query
    search_query = "Lorem Ipsum"
    # Format the search query for a URL
    url = f"https://www.bing.com/search?q={search_query}"


    # Register Edge as a browser
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

    # Open Microsoft Edge and search
    webbrowser.get('edge').open_new_tab(url)

    # new_search_query = "Ipsum Lorem"

    for new_search_query in queries:
        time.sleep(10)

        # Click and a new search query and press Enter
        pyautogui.click(x=500, y=150)  # Adjust the coordinates based on your screen resolution
        # pyautogui.typewrite("Hello")
        # time.sleep(1)

        pyautogui.keyDown('ctrl')  # hold down the shift key
        pyautogui.keyDown('shift')  # hold down the shift key
        pyautogui.press('home')     # press the left arrow key
        pyautogui.keyUp('shift')    # release the shift key
        pyautogui.keyUp('ctrl')    # release the shift key

        pyautogui.typewrite(new_search_query)
        pyautogui.press('enter')


import random

def generate_random_syllable():
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    return random.choice(consonants) + random.choice(vowels) + random.choice(consonants)

def generate_random_word(length):
    return ''.join(generate_random_syllable() for _ in range(length))

if __name__ == "__main__":
    main()
