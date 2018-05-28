
OTACLIDIR=../../micropython-OTA/otacli
PORT=/dev/ttyUSB0
export AMPY_PORT=$(PORT)

install: otacli.py
	make -C .. download
	make -C smallinstall
	ampy put ../micropython-lib/umqtt.simple/umqtt
	ampy put ../micropython-lib/utarfile/utarfile.py
	ampy put ../micropython-lib/os.path/os/path.py ospath.py
	ampy put otacli.py

smallinstall:
	ampy put main.py
	ampy put servo.py
	ampy put config.py
	ampy put config_local.py

otacli.py:
	cp $(OTACLIDIR)/otacli.py ./
