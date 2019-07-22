def some_function():
    L = []
    for x in range(10):
        L.append(x)

    import ipdb;ipdb.set_trace()

    return L


some_function()