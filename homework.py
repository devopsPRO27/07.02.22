import json
import requests
from User import *

#lst=[{'name':'hodi'}}]

def getUser():
    response=requests.get('http://jsonplaceholder.typicode.com/users') # list of string ['{}''{}'{}'{}{}]
    if response.status_code//100 ==2:
        return  json.loads(response.content) # list of users  => list of dic

def findUser(nameToCheck,userList):
    for user in userList:
        temp=User(user)
        if temp.name ==nameToCheck:
            return temp
    return 'this name was not found '


def main():
    userJson=getUser()
    rightuser=findUser('Ervin Howell', userJson)

    print(rightuser)
    print(rightuser.address)


if __name__ == '__main__':
    main()