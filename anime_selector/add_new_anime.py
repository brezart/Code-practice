import os 

def main(data) -> None:
    #gather input from user
    print("enter name:")
    name = input()
    
    print("enter type:")
    type = input()

    print("enter link:")
    link = input()

    updated = os.system('date')

    print("enter episide count:")
    ep_count= input()

    #use it to create entr
    data.update({
        name: {
            "type": type,
            "link": link,
            "udpated": updated,
            "episode_count": ep_count
        }
    })