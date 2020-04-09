#!/bin/bash
cp k.py /usr/bin/
cp rebrot.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable rebrot.service
