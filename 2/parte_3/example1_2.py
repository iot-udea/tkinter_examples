import threading

num_threads = 0


def heron(a):

    global num_threads
    num_threads += 1

    ### Calculates the square root of a
    eps = 0.0000001
    old = 1
    new = 1
    while True:
        old,new = new, (new + a/new) / 2.0
        print (old, new)
        if abs(new - old) < eps:
            break
    # code has been left out, see above
    num_threads -= 1
    return new

h1 = threading.Thread(target=heron, args=(99,))
h2 = threading.Thread(target=heron, args=(999,))
h3 = threading.Thread(target=heron, args=(1733,))
h4 = threading.Thread(target=heron, args=(17334,))

h1.start()
h2.start()
h3.start()
h4.start()

while num_threads > 0:
    pass
