#!/usr/bin/env python

import argparse
from tv_stuff import TV
from conf import *

def remote():
    """the remote for PC-Remote"""
    parser = argparse.ArgumentParser(description='Control your TV using PC-Remote')

    parser.add_argument('BUTTON_NAME', type=str, help='Name of the button to press')
    
    args = parser.parse_args()
    
    try:
        BUTTON_NAME = args.BUTTON_NAME.lower()
        # ---------- MOVEMENT ---------- #
        if BUTTON_NAME == "ok":
            clicks = int(input(f"How many times would you like to press {BUTTON_NAME}?: "))
            for _ in range(clicks):
                TV.remote(key="OK")
            print("Pressed 'OK'")
            
        elif BUTTON_NAME == "left":
            clicks = int(input(f"How many times would you like to press {BUTTON_NAME}?: "))
            for _ in range(clicks):
                TV.remote("LEFT")
            print(f"Moved LEFT {clicks} times.")

        elif BUTTON_NAME == "right":
            clicks = int(input(f"How many times would you like to press {BUTTON_NAME}?: "))
            for _ in range(clicks):
                TV.remote("RIGHT")
            print(f"Moved RIGHT {clicks} times.")

        elif BUTTON_NAME == "up":
            clicks = int(input(f"How many times would you like to press {BUTTON_NAME}?: "))
            for _ in range(clicks):
                TV.remote("UP")
            print(f"Moved UP {clicks} times.")

        elif BUTTON_NAME == "down":
            clicks = int(input(f"How many times would you like to press {BUTTON_NAME}?: "))
            for _ in range(clicks):
                TV.remote("DOWN")
            print(f"Moved DOWN {clicks} times.")

        elif BUTTON_NAME == "pause":
            TV.remote(key="PAUSE")
            print(f"Pressed PAUSE.")

        elif BUTTON_NAME == "back":
            clicks = int(input(f"How many times would you like to press {BUTTON_NAME}?: "))
            for _ in range(clicks):
                TV.remote(key="BACK")
            print(f"Pressed BACK {clicks} times.")

        # ------------ TV ---------- #
        elif BUTTON_NAME == "home":
            TV.remote(key="HOME")
            print("Pressed 'HOME'")
        elif BUTTON_NAME == "close":
            TV.remote("EXIT")
            print("Successfully Exited")
        elif BUTTON_NAME == "on":
            TV.remote(key="POW_ON")
            print(f"Powered on {DEVICE_NAME}")
        elif BUTTON_NAME == "off":
            TV.remote(key="POW_OFF")
            print(f"Powered off {DEVICE_NAME}")

        # ------------ VOLUME ---------- #
        elif BUTTON_NAME == "CC":
            TV.remote(key="CC_TOGGLE")
            print("Toggled CC")
        elif BUTTON_NAME == "vol_up":
            amount = int(input("How much would you like to turn the TV up?: "))
            for _ in range(amount):
                TV.remote(key="VOL_UP")
            print("Turned volume up")
        elif BUTTON_NAME == "vol_down":
            amount = int(input("How much would you like to turn the TV down?: "))
            for _ in range(amount):
                TV.remote(key="VOL_DOWN")
            print("Turned volume down")
        elif BUTTON_NAME == "mute":
            TV.remote(key="MUTE_TOGGLE")
            print(f"Toggled mute on {DEVICE_NAME}")
        
        # ------------ APPS ---------- #
        elif BUTTON_NAME == "launch" or BUTTON_NAME == "open":
            app_name = input("What app would you like to open?: ")
            TV.launch_app(app_name=f"{app_name}")
            print(f"Launched {app_name}")
        elif BUTTON_NAME == "apps":
            print(TV.get_apps_list())

        else:
            print(f"Unknown button: {BUTTON_NAME}")
    except KeyboardInterrupt:
        print("\nExiting PC-Remote")
        exit(1)

if __name__ == "__main__":
    remote()
