def friend(x):
    friends=[]
    for index in range(len(x)):
        name=x[index]
        if len(name) == 4:
            friends.append(name)
    return friends

if __name__=="__main__":
    names=["Ulises","Samuel","Daniela","Ryan","Mark"]
    friends=friend(names)
    print(friends)