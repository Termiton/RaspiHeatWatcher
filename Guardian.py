import os
import time
import re
import smtplib
import heatconf
from os.path import basename, splitext
from Functions import sendTextMail

while True:

    # max_temperature
    max_temperature = heatconf.max_temp

    # Heat mesure command open
    cmd_temperature = os.popen("/opt/vc/bin/vcgencmd measure_temp")

    # Heat mesure command read
    get_temperature = cmd_temperature.read() #"temp=37.5'C"

    # Heat mesure command close
    cmd_temperature.close()

    # Get temperature float
    match = re.search(r"^temp=([0-9.]{2,4})'C$", get_temperature)
    float_temperature = float(match.group(1))





    # Mail Alert if temperature > 45'C
    if float_temperature >=  max_temperature:
        texte = "La temperature a depasse les %s'C." % max_temperature
        sendTextMail(texte)
    i = 1
    time.sleep(60)


