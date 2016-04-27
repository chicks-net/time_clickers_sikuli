# start Time Clickers

from time import sleep

switchApp("TimeClickers")

for i in range(3):
    if not i % 50:
        Debug.user("i=%i" % (i))
    type("asdfg")
    sleep(0.4)