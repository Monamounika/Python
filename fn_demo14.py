def first():
    print("this is outer fn")
    def second():
        print("this is inner fn")
    second()
first()