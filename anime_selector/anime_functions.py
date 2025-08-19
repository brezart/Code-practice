import os 
import subprocess
import numpy as np
import time 
import random

#gather data from user
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

#Performs a countdown from n to 0
def count_down(n: int):
    array = np.arange(1,n+1,1)
    backwards_array = array[::-1]
    for i in backwards_array:
        print(i)
        time.sleep(1)

#Chooses a random anime 
def random_anime(json_data) -> str:
    anime_data = json_data
    choice = random.choice(list(anime_data.keys()))
    print(f'"{str(choice)}"')
    
    return choice

#Updates anime_dict with new data
def add(data) -> None:

    #assign variables 
    name,type,link,updated,base_url_index,ep_count = gather_data()

    #use it to create dict entry
    data.update({
        name: {
            "type": type,
            "link": link,
            "updated": updated,
            "base_url_index": base_url_index,
            "episode_count": ep_count
        }
    })


#Deletes anime_dict entry
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

#Updates episode count variable and returns it as output
def update_ep_count(episode_count: str, link: str) -> str:
    ep_count_int = int(episode_count)
    ep_count_int += 1
    episode_count = str(ep_count_int)
    return episode_count   

#Constructs new link for next episode from base url index and episode count
def generate_new_link(base_url_index: int, link: str, episode_count: str) -> str:
    updated_link_ending = base_url_index + int(episode_count) - 1 #minus 1 because the ep count indexes from 0 and the base index indexes from 1 ie the base url index is the index for episode 1
    new_link = link + str(updated_link_ending)    
    return new_link

#Asks user to confirm selection and then opens in browser
def get_confirmation_and_open_link(selection, system: str, updated_link: str) -> None:
    print("found your selection", selection)
    print("do you want to watch it? Y/n")
    decision = input()

    if decision == "y" or decision == "Y":

        #get link and open it
        if system == "mac":
            os.system(f'open "{updated_link}"')
        elif system == "linux":
            os.system(f'xdg-open "{updated_link}"')
        print("enjoy the show :)")

    else:

        print("okay we won't watch that one")


#store options for cli tool
options = ["list", "add", "help", "delete", "surprise me"]

#get user selection
def accept_selection() -> None:
    for option in options:
        print("-" + option)
    selection = input()
    return selection

def help() -> None:
    for option in options:
        print("-" + option)