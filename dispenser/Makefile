
PORT=/dev/ttyUSB0
export AMPY_PORT=$(PORT)


SRCS=main.py servo.py config.py config_local.py conn.py
UPTARGETS=$(patsubst %.py, .%.amput, $(SRCS))

TPLS=templates/index.tpl
TPLTARGETS=$(patsubst templates/%.tpl, templates/.%.tpl, $(TPLS))

.%.amput: %.py
	ampy put $<
	touch $@

.%.tpl: %.tpl
	ampy mkdir --exists-okay $(shell dirname $<)
	ampy put $< $<
	touch $@

install: $(UPTARGETS) $(TPLTARGETS)

clean:
	rm -vf $(UPTARGETS)

minicom:
	make install
	minicom -D $(PORT)

debug: $(TPLTARGETS)
