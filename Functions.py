# -*-coding:Utf-8 -*

import heatconf
from os.path import basename, splitext


def writefile(message):
    """
    @usage:
    writefile(fichier,message)
    """

    filename = heatconf.log
    logfile = file(filename, "a")
    logfile.write(time.strftime("\n%Y/%m/%d %H:%M:%S\t") + message)
    logfile.close()


def sendTextMail(texte):

    from_smtp = heatconf.from_smtp
    from_port = heatconf.from_port
    from_mail = heatconf.from_mail
    from_pwd = heatconf.from_pwd
    to_mail = heatconf.to_mail

    server = smtplib.SMTP(from_smtp, from_port)
    server.starttls()
    server.login(from_mail, from_pwd)

    msg = texte
    server.sendmail(from_mail, to_mail, msg)
    server.quit()

