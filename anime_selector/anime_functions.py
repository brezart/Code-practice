import os 
import subprocess
import numpy as np
import time 
import random

def gather_data():

    #gather anime data from user
    print("enter name:")
    name = input()
    
    print("enter type:")
    type = input()

    print("enter link:")
    link = str(input())

    command = ['date']
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    updated = result.stdout

    #setup link and get base_url_index from full link
    link, base_url_index = link.split("=")
    link = link + "="

    print("enter episide count:")
    ep_count= input()
    return (name,type,link,updated,base_url_index,ep_count)

def add(data) -> None:

    #assign variables 
    name,type,link,updated,base_url_index,ep_count = gather_data()

    #use it to create entry
    data.update({
        name: {
            "type": type,
            "link": link,
            "updated": updated,
            "base_url_index": base_url_index,
            "episode_count": ep_count
        }
    })

def delete(data):

    #prompt the user to select anime to delete
    print("select anime to delete")

    name = input()
    if data[name]:

        #prompt the user to confirm deletion  
        print(f"Are you sure you want to delete {name}? Y/n")

        #delete selection
        user_choice = input()
        if user_choice == 'Y' or "y":
            del data[name]
            print(f"Successfully deleted {name}")

        elif user_choice== 'N' or 'n':
            print(f"Okay, we won't delete {name}")

    return data

#this function is currently not being used
def count_down(n: int):
    array = np.arange(1,n+1,1)
    backwards_array = array[::-1]
    for i in backwards_array:
        print(i)
        time.sleep(1)
 
def random_anime(json_data) -> str:
    anime_data = json_data
    choice = random.choice(list(anime_data.keys()))
    print(f'"{str(choice)}"')
    
    return choice

def update_ep_count(episode_count: str, link: str):
    ep_count_int = int(episode_count)
    ep_count_int += 1
    episode_count = str(ep_count_int)
    return episode_count   