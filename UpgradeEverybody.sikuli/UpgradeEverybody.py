# start Time Clickers

from time import sleep

switchApp("TimeClickers")

for i in range(20):
    if not i % 10:
        Debug.user("i=%i" % (i))
    type("asdfg")
    sleep(0.2)