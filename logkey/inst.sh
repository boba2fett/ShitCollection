#!/bin/bash
cp .service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable you_service_name.service
