export BR=$(CURDIR)/build-root

$(BR)/scripts/.version:
ifneq ("$(wildcard /etc/redhat-release)","")
	$(shell $(BR)/scripts/version rpm-string > $(BR)/scripts/.version)
else
	$(shell $(BR)/scripts/version > $(BR)/scripts/.version)
endif

DIST_FILE = $(BR)/uio_hv_generic-$(shell extras/scripts/version).tar
DIST_SUBDIR = uio_hv_generic-$(shell extras/scripts/version | cut -f1 -d-)

dist:
	@if git rev-parse 2> /dev/null ; then \
	    git archive \
	      --prefix=$(DIST_SUBDIR)/ \
	      --format=tar \
	      -o $(DIST_FILE) \
	    HEAD ; \
	    git describe > $(BR)/.version ; \
	else \
	    (cd .. ; tar -cf $(DIST_FILE) $(DIST_SUBDIR) --exclude=*.tar) ; \
	    extras/scripts/version > $(BR)/.version ; \
	fi
	@tar --append \
	  --file $(DIST_FILE) \
	  --transform='s,.*/.version,$(DIST_SUBDIR)/extras/scripts/.version,' \
	  $(BR)/.version
	@for f in $$(git status --porcelain | grep '^D' | awk '{print $$2}'); do \
	  tar --delete --file $(DIST_FILE) $(DIST_SUBDIR)/$${f}; \
	done
	@for f in $$(git status --porcelain -u | grep -v '^D' | awk '{print $$2}'); do \
	  tar --append --file $(DIST_FILE) \
	  --transform="s,$${f},$(DIST_SUBDIR)/$${f}," \
	  $${f}; \
	done
	@$(RM) $(BR)/.version $(DIST_FILE).xz
	@$(RM) $(BR)/.version $(DIST_FILE).xz
	@xz -v --threads=0 $(DIST_FILE)
	@$(RM) $(BR)/uio_hv_generic-latest.tar.xz
	@ln -rs $(DIST_FILE).xz $(BR)/uio_hv_generic-latest.tar.xz

pkg-rpm: dist
	make -C extras/rpm

pkg-srpm: dist
	make -C extras/rpm srpm

clean:
	@$(RM) $(BR)/*.tar.xz
	@$(RM) $(BR)/*.rpm
	@$(RM) -r $(BR)/rpmbuild
