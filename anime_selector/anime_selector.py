import json
import os
import anime_functions 


with open('anime_data.json', 'r') as file:
    data = json.load(file)

#options are mac or linux. this is used later to determine how to open the link to the episode. xdg-open or open.
system="linux"

selection = anime_functions.accept_selection()

match selection: 
    case "help":
        anime_functions.help()
        
    case "surprise me":
        print("you betcha!")
        anime_functions.count_down(3)

        #call random anime function
        selection = anime_functions.random_anime(json_data=data)
        anime_functions.get_confirmation_and_open_link(selection=selection, system=system, updated_link=updated_link)        

    case "list":
        print("We can watch:")
        for entry in data:
            print("- ", entry)    

    case "add":
        anime_functions.add(data=data)   

    case "delete":
        anime_functions.delete(data=data)        

    case _:
        if data[selection]:

            #set values
            name = selection
            link = data[selection]["link"]
            updated = data[selection]["updated"]
            base_url_index = data[selection]["base_url_index"]
            episode_count = data[selection]["episode_count"]

            #generate new link with udated ep number
            updated_episode_count = anime_functions.update_ep_count(episode_count=episode_count, link=link)
            
            #update episode count in dict
            data[selection]["episode_count"] = updated_episode_count # here we have to use the full data[][] value because that is the dict object whereas episode_count is just a thing equal to it's value not the original storage location itself.

            #Updated link to point to new episode
            updated_link = anime_functions.generate_new_link(base_url_index=base_url_index, link=link, episode_count=updated_episode_count)

            #ask for user confirmation
            anime_functions.get_confirmation_and_open_link(selection=selection, system=system, updated_link=updated_link)        

# if selection == "help":    
#     anime_functions.help()
#     exit

# elif selection == 'surprise me':
#     print("you betcha!")
#     anime_functions.count_down(3)

#     #call random anime function
#     selection = anime_functions.random_anime(json_data=data)
    
# elif selection == 'list':
#     print("We can watch:")
#     for entry in data:
#         print("- ", entry)

# elif selection == "add":
#    anime_functions.add(data=data)

# elif selection == "delete":
#     anime_functions.delete(data=data)
    
# if data[selection]:

#     #set values
#     name = selection
#     link = data[selection]["link"]
#     updated = data[selection]["updated"]
#     base_url_index = data[selection]["base_url_index"]
#     episode_count = data[selection]["episode_count"]

#     #generate new link with udated ep number
#     updated_episode_count = anime_functions.update_ep_count(episode_count=episode_count, link=link)
    
#     #update episode count in dict
#     data[selection]["episode_count"] = updated_episode_count # here we have to use the full data[][] value because that is the dict object whereas episode_count is just a thing equal to it's value not the original storage location itself.

#     #Updated link to point to new episode
#     updated_link = anime_functions.generate_new_link(base_url_index=base_url_index, link=link, episode_count=updated_episode_count)

#     #ask for user confirmation
#     anime_functions.get_confirmation_and_open_link(selection=selection, system=system, updated_link=updated_link)

#write any changes made back to the json file
with open('anime_data.json', 'w') as file:
    json.dump(data, file, indent=4)
