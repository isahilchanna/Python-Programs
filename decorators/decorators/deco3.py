def calling():
    print("hello from the outter")
    def returning():
        print("Hello from the inner")
    return returning

new = calling()

new()
