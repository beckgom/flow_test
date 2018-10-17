def hello_world(name=None):
    if name != None:
        print("hello world!, {}".format(name))
    else:
        print("hello world!")

if __name__ == "__main__":
    hello_world()
