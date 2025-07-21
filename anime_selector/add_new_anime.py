import os 
import subprocess

def main(data) -> None:
    #gather input from user
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

    #use it to create entr
    data.update({
        name: {
            "type": type,
            "link": link,
            "udpated": updated,
            "base_url_index": base_url_index,
            "episode_count": ep_count
        }
    })