# start Time Clickers

from time import sleep

switchApp("TimeClickers")

# upgrade team stepwise, so each is one step above the one below it
type("aa"); sleep(0.1);
type("aass"); sleep(0.1);
type("aassdd"); sleep(0.1);
type("aassddff"); sleep(0.1);
type("aassddffgg"); sleep(0.1);

for i in range(20):
    if not i % 10:
        Debug.user("i=%i" % (i))
    type("asdfg")
    sleep(0.2)