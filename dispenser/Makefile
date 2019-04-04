
PORT=/dev/ttyUSB0
export AMPY_PORT=$(PORT)


SRCS=main.py servo.py config.py config_local.py 
UPTARGETS=$(patsubst %.py, .%.amput, $(SRCS)) \
			../micropython-lib/logging/.logging.amput

.%.amput: %.py
	ampy put $<
	touch $@

install: $(UPTARGETS)

minicom:
	make install
	minicom -D $(PORT)

debug:
	echo SRCS=$(SRCS)
	echo MILSRCS=$(MILSRCS)
	echo UPTARGETS=$(UPTARGETS)


