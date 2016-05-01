# 1. start Time Clickers (windowed 1024x768)
# 2. start time warp
# 3. pick artifacts, click done
# 4. run this script
# 5. profit

from time import sleep

switchApp("TimeClickers")

# upgrade gun
click("gun01.png") # 01
gun = getLastMatch()
click(gun) # 02
click(gun) # 03
click(gun) # 04
click(gun) # 05
click(gun) # 06
click(gun) # 07
click(gun) # 08
click(gun) # 09
click(gun) # 10
click(gun) # 11
click(gun) # 12
click(gun) # 13


# buy abilities
click("ability01.png") # 01
ability = getLastMatch()
click(ability) # 02
click(ability) # 03
click(ability) # 04
click(ability) # 05
click(ability) # 06
click(ability) # 07
click("dimension_shift.png") # dimension shift
click(ability) # 08
click(ability) # 09
click(ability) # 10

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
