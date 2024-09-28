
#!/usr/bin/python3
import sys
import requests

#Reteriveing data from todo list to check 
#the progress of the empolyee  in the todo list

#Sending a request to the specified url 
if __name__ == "___main___":

    url  = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url, "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId":sys.argv[1]}).json()

#Gathering data
    compeleted = [todo.get("title")for todo in todos:if todo.get("compeleted")is True]
    print("Employee{} is done with tasks({}/{})".format(user.get("name"), len(compeleted), len(todos)))
    [print("\todo{}".format(compelete))for compelete in compeleted]
