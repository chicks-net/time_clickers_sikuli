# 1. start Time Clickers (windowed 1024x768)
# 2. start time warp
# 3. pick artifacts, click done
# 4. run this script
# 5. profit

from time import sleep

switchApp("TimeClickers")

# upgrade gun
click("gun01.png") # 01
click("gun02.png") # 02
click("gun03.png") # 03
click("gun04.png") # 04
click("gun05.png") # 05
click("gun06.png") # 06
click("gun07.png") # 07
click("gun08.png") # 08
click("gun09.png") # 09
click("gun10.png") # 10
click("gun11.png") # 11
click("gun12.png") # 12
click("gun13.png") # 13


# buy abilities
click("ability01.png") # 01
click("ability02.png") # 02
click("ability03.png") # 03
click("ability04.png") # 04
click("ability05.png") # 05
click("ability06.png") # 06
click("ability07.png") # 07
click("dimension_shift.png") # dimension shift
click("ability08.png") # 08
click("ability09.png") # 09
click("ability10.png") # 10

# upgrade team stepwise, so each is one step above the one below it
type("aa"); sleep(0.1);
type("aass"); sleep(0.1);
type("aassdd"); sleep(0.1);
type("aassddff"); sleep(0.1);
type("aassddffgg"); sleep(0.1);

# start weapons in Idle Mode
click("weapon_left.png") # left
click("weapon_center.png") # center
click("weapon_right.png") # right

# upgrade a bunch
for i in range(90):
    if not i % 10:
        Debug.user("i=%i" % (i))
    type("asdfg")
    sleep(0.1)

# upgrade slower
Debug.user("slower")
for i in range(20):
    type("asdfg")
    sleep(0.5)
