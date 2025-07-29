import json
import os
import anime_functions 


with open('anime_data.json', 'r') as file:
    data = json.load(file)

#options are mac or linux. this is used later to determine how to open the link to the episode. xdg-open or open.
system="mac"

# class entry:
#     def __init__(self, name: str , link: str, updated, base_url_index: int, episode_count: int):
#         self.name = name
#         self.link = link
#         self.updated = updated
#         self.base_url_index = base_url_index    
#         self.episode_count = episode_count

#     def add(self):
#         data.update({
#             name: {
#                 "type": type,
#                 "link": link,
#                 "udpated": updated,
#                 "base_url_index": base_url_index,
#                 "episode_count": episode_count
#             }
#         })
    
    # def delete(self):
    #     delete stuff 

def update_ep_count(episode_count: str, link: str):

    ep_count_int = int(episode_count)
    ep_count_int += 1
    episode_count = str(ep_count_int)
    return episode_count

def generate_new_link(base_index: int, link: str, episode_count: str):
    updated_link_ending = base_url_index + int(episode_count) - 1 #minus 1 because the ep count indexes from 0 and the base index indexes from 1 ie the base url index is the index for episode 1
    new_link = link + str(updated_link_ending)    
    return new_link

print('''please make your selection
    - list 
    - add
    - <anime name>''')
selection = input()

if selection == "help":
    print('''
        options ared:
        - list
        - add anime
        - <name>
        - remove 
        ''')

if selection == 'surprise me':
    print("you betcha!")
    anime_functions.count_down(3)

    #call random anime function
    selection = anime_functions.random_anime(json_data=data)
    
if selection == 'list':
    print("We can watch:")
    for entry in data:
        print("- ", entry)

elif selection == "add":
   anime_functions.add(data=data)

elif selection == "delete":
    anime_functions.delete(data=data)
    
elif data[selection]:

    #set values
    name = selection
    link = data[selection]["link"]
    updated = data[selection]["updated"]
    base_url_index = data[selection]["base_url_index"]
    episode_count = data[selection]["episode_count"]

    #generate new link with udated ep number
    updated_episode_count = update_ep_count(episode_count=episode_count, link=link)
    
    #update episode count in dict
    data[selection]["episode_count"] = updated_episode_count # here we have to use the full data[][] value because that is the dict object whereas episode_count is just a thing equal to it's value not the original storage location itself.
    updated_link = generate_new_link(base_index=base_url_index, link=link, episode_count=updated_episode_count)

    #ask for user confirmation
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

#write any changes made back to the json file
with open('anime_data.json', 'w') as file:
    json.dump(data, file, indent=4)
