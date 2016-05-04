import os
import time
import re
import smtplib
from os.path import basename, splitext
from Functions import sendTextMail
from Functions import writefile


while True:

    # Heat mesure command open
    cmd_temperature = os.popen("/opt/vc/bin/vcgencmd measure_temp")

    # Heat mesure command read
    get_temperature = cmd_temperature.read() #"temp=37.5'C"

    # Heat mesure command close
    cmd_temperature.close()

    # Get temperature float
    match = re.search(r"^temp=([0-9.]{2,4})'C$", get_temperature)
    float_temperature = float(match.group(1))

    # Mail temperature
    writefile(str(float_temperature))
    sendTextMail(get_temperature)
    
    # Wait
    time.sleep(3600)


