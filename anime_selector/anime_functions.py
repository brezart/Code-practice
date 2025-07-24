import os 
import subprocess

def gather_data():

    #gather anime data from user
    print("enter name:")
    name = input()
    
    print("enter type:")
    type = input()

    print("enter link:")
    link = input()

    command = ['date']
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    updated = result.stdout

    print("enter base_url_index")
    base_url_index = int(input())

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
            "udpated": updated,
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