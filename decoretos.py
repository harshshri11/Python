def greet(mfx):
    def func(*args, **kwargs):
        print("hlo i am decoretor")
        mfx(*args, **kwargs)
        print("_!_!_!_")
    return func

@greet
def fuck1():
    print("good morning harsh")

@greet
def fuck2():
     print("good morning sir")

fuck1()
fuck2()