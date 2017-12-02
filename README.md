### Airsensor
#### Compile
sudo apt-get install libusb-dev
sudo vi /etc/udev/rules.d/99-usb.rules
SUBSYSTEM=="usb", ATTR{idVendor}=="03eb", ATTR{idProduct}=="2013", MODE="0666"

15 22 * * 1-5 /usr/local/bin/node /home/pi/Dev/portfolio/index.js


#Build
docker build --rm -t tomtom101/airsensor .

# Run
docker rm air && docker run --name air -it tomtom101/airsensor python3 -c 'print("Hello World")'
docker rm air && docker run --name air -it tomtom101/airsensor tail -f /var/log/cron.log
