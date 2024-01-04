#!/usr/bin/python3
'''This file uses functions created in the Spod_box toolbox package'''
# import dependencies
from C:\Users\rober\OneDrive\Documents\GitHub\SpodBoxLibrary import spod_box as sb
# import datetime, time
# import gspread
# from google.auth.transport.requests import AuthorizedSession
# from google.oauth2 import service_account
# from time import sleep
# import math
import urllib.request

#Task 1 - get data (need requests module and URL)
esp32_url="http://144.167.214.188"
#data=sb.readESP32_BME688
sb.readESP32_BME688(esp32_url)
#print(data) 

#Task 2