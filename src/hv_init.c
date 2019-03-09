/*
 * X86 specific Hyper-V initialization code.
 *
 * Copyright (C) 2016, Microsoft, Inc.
 *
 * Author : K. Y. Srinivasan <kys@microsoft.com>
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 as published
 * by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE, GOOD TITLE or
 * NON INFRINGEMENT.  See the GNU General Public License for more
 * details.
 *
 */

#include <linux/types.h>
#include "include/asm/hyperv-tlfs.h"
#include "include/asm/mshyperv.h"
#include <asm/fixmap.h>
#include <linux/version.h>
#include <linux/vmalloc.h>
#include <linux/mm.h>
#include <linux/clockchips.h>
#include "include/linux/hyperv.h"
#include <linux/slab.h>
#include <linux/cpu.h>
#include <linux/kaiser.h>

/**
 * hyperv_report_panic_msg - report panic message to Hyper-V
 * @pa: physical address of the panic page containing the message
 * @size: size of the message in the page
 */
void hyperv_report_panic_msg(phys_addr_t pa, size_t size)
{
	/*
	 * P3 to contain the physical address of the panic page & P4 to
	 * contain the size of the panic data in that page. Rest of the
	 * registers are no-op when the NOTIFY_MSG flag is set.
	 */
	wrmsrl(HV_X64_MSR_CRASH_P0, 0);
	wrmsrl(HV_X64_MSR_CRASH_P1, 0);
	wrmsrl(HV_X64_MSR_CRASH_P2, 0);
	wrmsrl(HV_X64_MSR_CRASH_P3, pa);
	wrmsrl(HV_X64_MSR_CRASH_P4, size);

	/*
	 * Let Hyper-V know there is crash data available along with
	 * the panic message.
	 */
	wrmsrl(HV_X64_MSR_CRASH_CTL,
	       (HV_CRASH_CTL_CRASH_NOTIFY | HV_CRASH_CTL_CRASH_NOTIFY_MSG));
}
EXPORT_SYMBOL_GPL(hyperv_report_panic_msg);
