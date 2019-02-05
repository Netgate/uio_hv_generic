#
# module name and path
#
MODULE = uio_hv_generic
MODULE_PATH = drivers/uio/uio_hv_generic

SRCDIR := $(CURDIR)
VPATH += $(SRCDIR)

KERNEL_DIR ?= /usr/lib/modules/$(KERNELRELEASE)/build

obj-m		+= $(MODULE).o

.PHONY: default
default: build

build module all: $(MODULE).ko

$(MODULE).ko:
	$(MAKE) -C $(KERNEL_DIR) M=$(CURDIR) O=$(KERNEL_DIR)

install:
	$(MAKE) -C $(KERNEL_DIR) M=$(CURDIR) O=$(KERNEL_DIR) modules_install

clean:
	$(MAKE) -C $(KERNEL_DIR) M=$(CURDIR) O=$(KERNEL_DIR) clean
