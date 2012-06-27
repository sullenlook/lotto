#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: SullenLook <sullenlook@sullenlook.eu>
# lotto plugin

from plugin import *
from BeautifulSoup import BeautifulSoup
import feedparser
import random
import re
import urllib2, urllib, uuid
import json
from xml.dom import minidom

class lotto(Plugin):   
        
        @register("de-DE", ".*Gewinnzahlen |.*Euromillionen.*")
        def euromillionen_get(self, speech, language):
                if language == "de-DE":
                        rss_url = "http://www.lottoy.net/de/euromillionen/rss-feed/aktuelle-lottozahlen-gewinnzahlen-euromillionen.xml"
                        feed = feedparser.parse( rss_url )
                        answer = self.ask("alle Gewinnzahlen?")
                        self.say("Die Aktuellen Euromillionen Gewinnzahlen:")
                        feedcontent = ""
                        for entry in feed["items"]:
                                #self.say(entry["title"])
                                if format(answer) == "Ja":
                                        #self.say(summary)
                                        feedcontent = feedcontent + "\"" + entry["title"] + "\": " + entry["summary"] + "\n\n"
                                else:
                                        feedcontent = feedcontent + "\"" + entry["title"] + "\",\n"
                        self.say(feedcontent, ' ')
                self.complete_request()

        @register("de-DE", ".*Lottozahlen |.*Lotto.*")
        def fflh_updates(self, speech, language):
                if language == "de-DE":
                        rss_url = "http://rss.auto-scripting.com/rss_lotto_6aus49.php?count=1"
                        feed = feedparser.parse( rss_url )
                        answer = self.ask("6 aus 49?")
                        self.say("Die Aktuellen Lottozahlen 6 aus 49:")
                        feedcontent = ""
                        for entry in feed["items"]:
                                #self.say(entry["title"])
                                if format(answer) == "Ja":
                                        #self.say(summary)
                                        feedcontent = feedcontent + "\"" + entry["title"] + "\": " + entry["summary"] + "\n\n"
                                else:
                                        feedcontent = feedcontent + "\"" + entry["title"] + "\",\n"
                        self.say(feedcontent, ' ')
                self.complete_request()