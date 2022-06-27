''' # Require install
pip3 install flask
pip3 install pywhatkit  '''

import pywhatkit
from datetime import datetime
import time

seconds = time.time() + 60

date = datetime.fromtimestamp(seconds)
pywhatkit.sendwhatmsg('+34633328749', 'Esto es una prueba', date.hour, date.minute)
time.sleep(5)
pywhatkit.sendwhats_image("+910123356789", "Images/Hello.png")

