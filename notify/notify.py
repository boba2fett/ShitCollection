#!/usr/bin/env python3
import sys, os
from gi.repository import Notify
# sudo apt-get install python-gobject
Notify.init("App Name")
Notify.Notification.new("yeet").show()
