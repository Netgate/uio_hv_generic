#
# module name and path
#
MODULE_PATH = extra

SRCDIR := $(CURDIR)
VPATH += $(SRCDIR)

KERNEL_DIR ?= /usr/lib/modules/$(KERNELRELEASE)/build

obj-m		+= uio_hv_generic.o
obj-m		+= hv_vmbus.o
obj-m		+= hv_balloon.o
obj-m		+= hyperv_fb.o
obj-m		+= hid-hyperv.o
obj-m		+= hyperv-keyboard.o
obj-m		+= pci-hyperv.o
obj-m		+= hv_utils.o
obj-m		+= hv_storvsc.o
obj-m		+= hv_netvsc.o
obj-m		+= hv_sock.o

hv_vmbus-y := vmbus_drv.o hv.o connection.o channel.o channel_mgmt.o \
		ring_buffer.o hv_trace.o \
		hv_init.o
hv_utils-y := hv_util.o hv_kvp.o hv_snapshot.o hv_fcopy.o hv_utils_transport.o
hv_storvsc-y := storvsc_drv.o
hv_netvsc-y := netvsc_drv.o netvsc.o rndis_filter.o
hv_sock-y := hyperv_transport.o

.PHONY: default
default: build

build modules all:
	$(MAKE) -C $(KERNEL_DIR) M=$(CURDIR) O=$(KERNEL_DIR)

install:
	$(MAKE) -C $(KERNEL_DIR) M=$(CURDIR) O=$(KERNEL_DIR) modules_install

clean:
	$(MAKE) -C $(KERNEL_DIR) M=$(CURDIR) O=$(KERNEL_DIR) clean
