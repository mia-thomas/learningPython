''' A program that prompts for a list of repositories

Add each item to an array

Loop through the array and using the GitHub API, check if those repositories already exist and print to the user if the repo exists or not

Bonus ( not sure if it can be done with API but probably can ), when checking if repo exists, if it doesn’t then ask the user if they want it to be created, if they do then create the repo '''

print("Hello User!\nCan you please provide a list of Repositories you would like me to check?\nI can check a maximum of 5 times!\nIf you have entered as many as you please and do not want to continue, please type \'DONE\' when prompted for a Repo")

userRepos = []
maxLength = 5
while len(userRepos) < maxLength:
    repos = input("Please type the Repo you would like us to create/check?").lower()
    userRepos.append(repos)
    if repos == "done":
        break
    print("You have entered " + repos + " as a Repo to create/check.")
    print(userRepos)
 
print("Thank you! I will now check these!")