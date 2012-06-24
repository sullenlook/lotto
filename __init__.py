#!/usr/bin/python
# -*- coding: utf-8 -*-
# Résultat du dernier tirage du Lotto (belge, avec 2 t) et de l'Euromillions.
# Utilise l'API de l'application iPhone de la loterie nationale belge.
# Par Cédric Boverie (cedbv)

import re
import xml.etree.ElementTree as ET
import urllib2, urllib
import locale 
import time
import random

from plugin import *

class lotto(Plugin):   
        
    @register("de-DE", u".*(loto|lotto|eurolotto).*")
    def lotto(self, speech, language, regex):
                
        typetirage = regex.group(regex.lastindex).strip().lower()
        print typetirage
        if typetirage == "loto" or typetirage == "lotto":
            typetirage = "lotto"
            if self.assistant.timeZoneId != "Europe/Berlin":
                self.say(u"Bitte beachten Sie, sind nur die Ergebnisse der belgischen Lotto verfuegbar.")
        else:
            typetirage = "euromillions"
        
        ns = "{http://www."+typetirage+".be/soap2/}"
        date_tirage = None
        result = ""
        result_say = ""
        try:
            response = urllib2.urlopen("http://www.lotto.de/soap2/{0}.asmx/LatestDraw?User=appsolution&Password=appsolutionwebservice".format(typetirage), timeout=5).read()
            xml = ET.fromstring(response)

            locale.setlocale(locale.LC_ALL, '')
            t = time.strptime(xml.find(ns+"DrawDate").text, "%Y-%m-%dT%H:%M:%S")
            date_tirage = time.strftime(u"%A, %d/%m/%Y", t)

            for c in xml.find(ns+"Results"):
                result += c.text + " "
                result_say += c.text + ", "
        except:
            pass
        
        if result != "":
            self.say(u"Tirage {0} du {1} : ".format(typetirage,date_tirage))
            self.say(result,result_say)
        else:
            self.say(u"Leider keine Ergebnisse.")

        self.complete_request()     