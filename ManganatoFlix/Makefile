PREFIX = /usr

all:
	@echo Run \'make install\' to install mangaflix.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p mangaflix $(DESTDIR)$(PREFIX)/bin/mangaflix
	@chmod +x $(DESTDIR)$(PREFIX)/bin/mangaflix

uninstall:
	@rm -f $(DESTDIR)$(PREFIX)/bin/mangaflix
