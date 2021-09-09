print("Hello! Here are the URLs you requested!")

file = open('url.txt', 'r')
fileContent = file.readlines()
import requests
for url in fileContent:
    print("https://" + url.strip())
    response = requests.get("https://" + url.strip())
    statusCode = response.status_code
    print("The Status code for " + url + "is " + str(statusCode))
    if statusCode == 200:
        print("The url for" + url + "is Healthy!")
    else:
        print("The url for" + url + "is Unhealthy!")
