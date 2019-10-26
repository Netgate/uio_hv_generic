TARBALL=$(shell realpath ../../build-root/uio_hv_generic-latest.tar.xz)
BASENAME=$(shell basename $(TARBALL) | sed -e s/.tar.\*//)
VERSION=$(shell echo $(BASENAME) | cut -f2 -d-)
RELEASE=$(shell echo $(BASENAME) | cut -f3- -d- | sed -e s/-/_/g)
BR=$(shell realpath $(CURDIR)/../../build-root)
RPMBUILD=$(BR)/rpmbuild

all: RPM

spec:
	@echo $(TARBALL)
	mkdir -p $(RPMBUILD)/{RPMS,SRPMS,BUILD,SOURCES,SPECS}
	cp $(TARBALL) $(RPMBUILD)/SOURCES/uio_hv_generic-$(VERSION)-$(RELEASE).tar.xz
	cp uio_hv_generic.spec $(RPMBUILD)/SPECS

srpm: spec
	rpmbuild -bs \
	  --define "_topdir $(RPMBUILD)" \
	  --define "_version $(VERSION)" \
	  --define "_release $(RELEASE)" \
	  $(RPMBUILD)/SPECS/uio_hv_generic.spec
	mv $$(find $(RPMBUILD)/SRPMS -name \*.src.rpm -type f) $(BR)

RPM: spec
	@echo "BASENAME is ${BASENAME}"
	@echo "VERSION is ${VERSION}"
	rpmbuild -bb \
	  --define "_topdir $(RPMBUILD)" \
	  --define "_version $(VERSION)" \
	  --define "_release $(RELEASE)" \
	  $(RPMBUILD)/SPECS/uio_hv_generic.spec
	mv $$(find $(RPMBUILD)/RPMS -name \*.rpm -type f) $(BR)
