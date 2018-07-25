export AMPY_PORT=/dev/ttyUSB0

run:
	ampy run main.py

install: download
	ampy put main.py
	ampy put luke/main.py luke/main.py
	ampy put luke/defs.py luke/defs.py
	ampy put luke/servo.py luke/servo.py
	ampy put micropython-lib/umqtt.simple/umqtt 

download: micropython-lib

micropython-lib:
	git clone https://github.com/micropython/micropython-lib


