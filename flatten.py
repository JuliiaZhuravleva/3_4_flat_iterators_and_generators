def flatten(mylist):
    if not mylist:
        return mylist
    if isinstance(mylist[0], list):
        return flatten(mylist[0]) + flatten(mylist[1:])
    return mylist[:1] + flatten(mylist[1:])