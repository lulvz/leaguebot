from lobby import *
from clicks import *
from audiohandler import *

# champ imports import only the ones being used
from yuumi import *

# changeable variables
champ = "yuumi" # available champs: yuumi
spells = ["heal", "barrier"]
champ_file = "./IMAGES/yuumi.png"

# in case something goes wrong
pyautogui.FAILSAFE = True

# if the lobby handler errors gotta do it manually
try:
    # lobby handler created
    lh = LobbyHandler("./IMAGES/accept.png", "./IMAGES/wait_file.png", champ_file, "./IMAGES/lock_file.png")
    # lobby accept fas
    lh.accept()
    # champ select
    lh.select_champ()
except Exception as e:
    print(e)

# From here on its up to the bot file
print("Initializing " + champ + "bot")
ymi = YuumiBot(spells)

for key in ymi.command_list:
    print(key + " - " + str(ymi.command_list[key]))

ymi.play()
