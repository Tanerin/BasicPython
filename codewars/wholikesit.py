def likes (names):
    if len(names) == 0:
        return "no one likes this"
    if len(names)==1:
        return names[0]+" likes this"
    if len(names)==2:
        return names[0]+" and "+names[1]+" likes this"
    if len(names)==3:
        return names[0]+", "+names[1]+" and "+names[2]+" likes this"
    if len(names)>3:
        return names [0]+", "+names[1]+ " and "+str(len(names)-2)+" others like this"


def run():
    names=["Peter", "Jacob", "Mark", "Max", "Ulises"]
    result =likes(names)
    print(result)


if __name__ == "__main__":
    run()