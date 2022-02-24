PREFIX = /usr

all:
	@echo Run \'make install\' to install mangaflix.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p rawmangaflix $(DESTDIR)$(PREFIX)/bin/rawmangaflix
	@chmod +x $(DESTDIR)$(PREFIX)/bin/rawmangaflix

uninstall:
	@rm -f $(DESTDIR)$(PREFIX)/bin/rawmangaflix
