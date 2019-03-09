#
# module name and path
#
MODULE_PATH = extra

SRCDIR := $(CURDIR)
VPATH += $(SRCDIR)

KERNEL_DIR ?= /usr/lib/modules/$(KERNELRELEASE)/build

obj-m		+= uio_hv_generic.o
obj-m		+= hv_vmbus.o

hv_vmbus-y := vmbus_drv.o hv.o connection.o channel.o channel_mgmt.o \
		ring_buffer.o hv_trace.o \
		hv_init.o

.PHONY: default
default: build

build modules all:
	$(MAKE) -C $(KERNEL_DIR) M=$(CURDIR) O=$(KERNEL_DIR)

install:
	$(MAKE) -C $(KERNEL_DIR) M=$(CURDIR) O=$(KERNEL_DIR) modules_install

clean:
	$(MAKE) -C $(KERNEL_DIR) M=$(CURDIR) O=$(KERNEL_DIR) clean
