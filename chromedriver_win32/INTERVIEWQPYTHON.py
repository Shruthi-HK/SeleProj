#Write a program to find the length of the string without using inbuilt function (len)

def _len(iterable):
    _count = 0
    for item in iterable:
        _count += 1
    return _count
# a= "hello"
a= [1,2,3,4]
print(_len(a))# a =len({1,2,3})
