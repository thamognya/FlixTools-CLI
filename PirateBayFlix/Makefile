PREFIX = /usr

all:
	@echo Run \'make install\' to install piratebayflix.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p piratebayflix $(DESTDIR)$(PREFIX)/bin/piratebayflix
	@chmod +x $(DESTDIR)$(PREFIX)/bin/piratebayflix

uninstall:
	@rm -f $(DESTDIR)$(PREFIX)/bin/piratebayflix

