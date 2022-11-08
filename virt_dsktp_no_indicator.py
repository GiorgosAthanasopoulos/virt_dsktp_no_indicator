import pystray
from PIL import Image
import pyvda
import threading
import time

max_virt_dsktps = 10
images_directory = './images/'

icon = pystray.Icon('virt dsktp no indicator',icon=Image.open(images_directory + '1.png'),menu=pystray.Menu(pystray.MenuItem('Exit',lambda icon:icon.stop())))

def bgThread():
    global icon

    while True:
        current_desktop = pyvda.VirtualDesktop.current().number

        if str(current_desktop) not in icon.icon.filename and current_desktop <= max_virt_dsktps:
            icon.icon = Image.open(images_directory + str(current_desktop) + '.png')

        time.sleep(.2)

threading.Thread(target=bgThread).start()
icon.run()
