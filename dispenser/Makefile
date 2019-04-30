WEBREPL_ADDR=192.168.5.114
WEBREPL_PASSWORD=dupadupa
# WEBREPL=../../webrepl/webrepl_cli.py
WEBREPL=webrepl-cli
PORT=/dev/ttyUSB0
export AMPY_PORT=$(PORT)


SRCS=main.py servo.py config.py config_local.py conn.py templates/index.tpl
WTARGETS=$(patsubst %, %.wput, $(SRCS))


%.wput: %
	$(WEBREPL) -p $(WEBREPL_PASSWORD) $< $(WEBREPL_ADDR):$<
	touch $@


install: $(WTARGETS)
	http http://$(WEBREPL_ADDR)/clear_templates

clean:
	rm -vf $(WTARGETS)

minicom:
	make install
	minicom -D $(PORT)

debug: $(WTARGETS)
