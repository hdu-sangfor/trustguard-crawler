# Linux Kernel

### 来源信息
- **URL**: https://www.opencve.io/cve/?q=vendor:linux+AND+product:linux_kernel
- **来源站点**: OpenCVE
- **页面抓取**: 成功

### 页面正文
| CVE | Vendors | Products | Updated | CVSS v3.1 | 
  | In the Linux kernel, the following vulnerability has been resolved:
ipv4: account for fraggap on the paged allocation path
In __ip_append_data(), when the paged-allocation branch is taken,
alloclen and pagedlen are computed as
	alloclen = fragheaderlen + transhdrlen;
	pagedlen = datalen - transhdrlen;
datalen already includes fraggap, but the fraggap bytes carried over
from the previous skb are copied into the new skb's linear area at
offset transhdrlen by the subsequent skb_copy_and_csum_bits(). The
linear area is therefore undersized by fraggap bytes while pagedlen is
overstated by the same amount.
The non-paged branch sets alloclen to fraglen, which already accounts
for fraggap because datalen does. Bring the paged branch in line by
adding fraggap to alloclen and subtracting it from pagedlen.
After this adjustment, copy no longer collapses to -fraggap on the
paged path, so remove the stale comment describing that old arithmetic. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
xfs: resample the data fork mapping after cycling ILOCK
xfs_reflink_fill_{cow_hole,delalloc} are both presented with an inode,
a data fork mapping, and a cow fork mapping.  Unfortunately, these two
helpers cycle the ILOCK to grab a transaction, which means that the
mappings are stale as soon as we reacquire the ILOCK.  Currently we
refresh the cow fork mapping by re-calling xfs_find_trim_cow_extent, but
we don't refresh the data fork mapping beforehand, which means that the
xfs_bmap_trim_cow in that function queries the refcount btree about the
wrong physical blocks and returns an inaccurate value in *shared.
If *shared is now false, the directio write proceeds with a stale data
fork mapping.  Fix this by querying the data fork mapping if the
sequence counter changes across the ILOCK cycle. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
KVM: s390: pci: fix GAIT table indexing due to double-scaling pointer arithmetic
kvm_s390_pci_aif_enable(), kvm_s390_pci_aif_disable(), and
aen_host_forward() index the GAIT by manually multiplying the index
with sizeof(struct zpci_gaite).
Since aift->gait is already a struct zpci_gaite pointer, this
double-scales the offset, accessing element aisb*16 instead of aisb.
This causes out-of-bounds accesses when aisb >= 32 (with
ZPCI_NR_DEVICES=512)
Fix by removing the erroneous sizeof multiplication. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
drm/amdgpu/vcn: set no_user_fence for VCN v2.0 enc/dec rings
VCN encoder and decoder rings do not support 64-bit user fence writes,
reject CS submissions with user fences.
(cherry picked from commit e2b5499fca55f1a32960a311bbb62e35891eaf73) | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
net: airoha: Do not read uninitialized fragment address in airoha_dev_xmit()
The transmit loop in airoha_dev_xmit() reads fragment address and length
during its final iteration, when the loop index equals
skb_shinfo(skb)->nr_frags, at which point the fragment data is
uninitialized. While these values are never consumed, the read itself is
unsafe and may trigger a page fault. Fix this by avoiding the fragment
read on the last iteration.
Additionally, move the skb pointer from the first to the last used packet
descriptor, so that airoha_qdma_tx_napi_poll() defers freeing the skb
until the final descriptor is processed. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
drm/amdgpu: fix amdgpu_hmm_range_get_pages
The notifier sequence must only be read once or otherwise we could work
with invalid pages.
While at it also fix the coding style, e.g. drop the pre-initialized
return value and use the common define for 2G range.
(cherry picked from commit c08972f555945cda57b0adb72272a37910153390) | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
drm/amdgpu: fix lock leak on ENOMEM in AMDGPU_GEM_OP_GET_MAPPING_INFO
The AMDGPU_GEM_OP_GET_MAPPING_INFO branch of amdgpu_gem_op_ioctl()
holds three cleanup-tracked resources before calling kvcalloc():
the drm_gem_object reference from drm_gem_object_lookup(), the
drm_exec lock on the looked-up GEM via drm_exec_lock_obj(), and
the drm_exec lock on the per-process VM root page directory via
amdgpu_vm_lock_pd().  All three are released by the out_exec
label that every other error path in this function jumps to.
The kvcalloc() failure path returns -ENOMEM directly, skipping
out_exec and leaking all three.
The leaked per-process VM root PD dma_resv lock is the
load-bearing leak: any subsequent operation on the same VM
(further GEM ops, command-submission, eviction, TTM shrinker
callbacks) blocks on the held lock.  DRM_IOCTL_AMDGPU_GEM_OP is
DRM_AUTH | DRM_RENDER_ALLOW, so this is an unprivileged-local
denial of service against the caller's GPU context, reachable
by any process with /dev/dri/renderD* access.
Route the failure through out_exec so drm_exec_fini() and
drm_gem_object_put() run.
Reproduced on stock 7.0.0-10, Ryzen 7 5700U / Radeon Vega
(Lucienne): the failing ioctl returns -ENOMEM and a second
GET_MAPPING_INFO on the same fd then blocks in
drm_exec_lock_obj() on the leaked dma_resv.  SIGKILL on the
caller does not reap the task; the fd-release path during
process exit goes through amdgpu_gem_object_close() ->
drm_exec_prepare_obj() on the same lock, leaving the task in D
state until the box is rebooted.  The patched kernel was not
rebuilt and re-tested on this hardware; the fix is mechanical.
Tested on a single Lucienne / Vega box only.
Ziyi Guo posted an independent INT_MAX-bound check for
args->num_entries in the same branch [1]; the two patches are
complementary and can land in either order.
(cherry picked from commit b69d3256d79de15f54c322986ff4da68f1d65b0a) | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
drm/gem: fix race between change_handle and handle_delete
drm_gem_change_handle_ioctl leaves the old handle live in the IDR
during the window between spin_unlock(table_lock) and the final
spin_lock(table_lock). A concurrent drm_gem_handle_delete on the old
handle succeeds in this window, decrements handle_count to 0, and frees
the GEM object while the new handle's IDR entry still references it.
NULL the old handle's IDR entry before dropping table_lock so that any
concurrent GEM_CLOSE on the old handle sees NULL and returns -EINVAL.
Restore the old entry on the prime-bookkeeping error path. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
scsi: target: iscsi: Fix CRC overread and double-free in iscsit_handle_text_cmd()
Two latent bugs in the Text-phase handler, both present since the
original LIO integration in commit e48354ce078c ("iscsi-target: Add
iSCSI fabric support for target v4.1"):
1) DataDigest CRC buffer overread (4 bytes past text_in).
  text_in is kzalloc()'d at ALIGN(payload_length, 4).  rx_size is then
  incremented by ISCSI_CRC_LEN to make room for the received DataDigest
  in the iovec, but the same (now-bumped) rx_size is passed as the
  buffer length to iscsit_crc_buf():
  if (conn->conn_ops->DataDigest) {
  ...
  rx_size += ISCSI_CRC_LEN;
  }
  ...
  if (conn->conn_ops->DataDigest) {
  data_crc = iscsit_crc_buf(text_in, rx_size, 0, NULL);
  iscsit_crc_buf() walks rx_size bytes of text_in with crc32c(), so
  when DataDigest is negotiated it reads 4 bytes past the end of the
  text_in allocation.  KASAN reproduces this directly on the unpatched
  mainline tree as slab-out-of-bounds in crc32c() called from the Text
  PDU path.  The OOB bytes feed crc32c() and are then compared against
  the initiator-supplied checksum, so the value does not flow back to
  the attacker, but the kernel does read past the buffer on every Text
  PDU with DataDigest=CRC32C.
  Fix by passing the actual padded payload length
  (ALIGN(payload_length, 4)) that was used for the kzalloc().
2) Stale cmd->text_in_ptr re-free (double-free) on ERL>0 bad DataDigest
  drop.
  On DataDigest mismatch with ErrorRecoveryLevel > 0 the handler
  silently drops the PDU and lets the initiator plug the CmdSN gap:
  kfree(text_in);
  return 0;
  cmd->text_in_ptr still points at the freed buffer.  The next Text
  Request on the same ITT re-enters iscsit_setup_text_cmd(), which
  unconditionally does
  kfree(cmd->text_in_ptr);
  cmd->text_in_ptr = NULL;
  freeing the same pointer a second time.  Session teardown via
  iscsit_release_cmd() has the same shape and hits the same double-free
  if the connection is dropped before a second Text Request arrives.
  On an unmodified mainline tree the bug-1 CRC overread fires first on
  the initial valid Text Request and perturbs the subsequent state, so
  #4 was isolated by building a kernel with only the bug-1 hunk of this
  patch applied plus temporary printk() observability around the three
  relevant kfree() sites.  The observability prints are not part of
  this patch.  On that build, a three-PDU Text Request sequence after
  login produces two back-to-back splats:
  BUG: KASAN: double-free in iscsit_setup_text_cmd+0x??
  BUG: KASAN: double-free in iscsit_release_cmd+0x??
  showing the same pointer freed in the ERL>0 drop path and again in
  iscsit_setup_text_cmd() (next Text Request on the same ITT) and once
  more in iscsit_release_cmd() (session teardown).  On distro kernels
  with CONFIG_SLAB_FREELIST_HARDENED=y (default) the double-free
  becomes a remote kernel BUG(); on non-hardened kernels it corrupts
  the slab freelist.
  Fix by clearing cmd->text_in_ptr after the kfree() in the ERL>0 drop
  path.  With both hunks applied #4 is directly observable on the stock
  tree without observability printks; fixing bug-1 alone would mask #4
  less, not more, so the hunks are submitted together.
Both fixes are one-liners.  The Text PDU state machine is unchanged and
the wire protocol is unaffected. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
scsi: fcoe: Reject FIP descriptors with zero fip_dlen in CVL walker
drivers/scsi/fcoe/fcoe_ctlr.c::fcoe_ctlr_recv_clr_vlink() advanced the
descriptor cursor by an attacker-supplied fip_dlen without ever
requiring dlen >= sizeof(struct fip_desc) in the default branch.  The
named descriptor cases (FIP_DT_MAC, FIP_DT_NAME, FIP_DT_VN_ID) checked
their per-type minimum lengths, but a FIP_DT_NON_CRITICAL descriptor
(fip_dtype >= 128, which the standard requires receivers to silently
ignore) skipped that check entirely.
An unauthenticated L2 peer on the FCoE control VLAN could hang
fcoe_ctlr_recv_work on an fcoe, qedf, or bnx2fc initiator indefinitely
by emitting one FIP CVL frame whose single descriptor had fip_dtype ==
FIP_DT_NON_CRITICAL and fip_dlen == 0: the cursor advanced zero bytes
per iteration and the loop condition rlen >= sizeof(*desc) stayed true
forever, blocking every subsequent FIP frame on that controller.
Tighten the outer dlen guard to also reject dlen < sizeof(struct
fip_desc), so a malformed descriptor whose length cannot even cover the
descriptor header is rejected before the switch.  This is the same
lower-bound the named cases already apply and is the minimum scope that
closes the loop. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
thunderbolt: property: Reject dir_len < 4 to prevent size_t underflow
On the non-root path, __tb_property_parse_dir() takes dir_len from
entry->length (u16 widened to size_t).  Two distinct OOB conditions
follow when entry->length < 4:
1. The non-root path begins with kmemdup(&block[dir_offset],
  sizeof(*dir->uuid), ...) which always reads 4 dwords from
  dir_offset.  tb_property_entry_valid() only enforces
  dir_offset + entry->length <= block_len, so a crafted entry
  with dir_offset close to the end of the property block and
  entry->length in 0..3 passes that gate but lets the UUID copy
  run off the block (e.g. dir_offset = 497, dir_len = 3 in a
  500-dword block reads block[497..501]).
2. After the kmemdup, content_len = dir_len - 4 underflows size_t
  to ~SIZE_MAX, nentries becomes SIZE_MAX / 4, and the entry
  walk runs OOB on each iteration until an entry fails
  validation or the kernel oopses on an unmapped page.
Reject dir_len < 4 on the non-root path *before* the UUID kmemdup,
which closes both holes.
Also move INIT_LIST_HEAD(&dir->properties) up to immediately after
the dir allocation so the new error-return path (and the existing
uuid-alloc failure path) calling tb_property_free_dir() sees a
walkable list rather than the zero-initialized NULL next/prev that
list_for_each_entry_safe() would oops on. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
usb: gadget: f_fs: copy only received bytes on short ep0 read
ffs_ep0_read() allocates its control-OUT data buffer with
kmalloc() (not kzalloc) at the Length value from the Setup
packet, then copies that full len to userspace regardless of
how many bytes were actually received:
  data = kmalloc(len, GFP_KERNEL);
  ...
  ret = __ffs_ep0_queue_wait(ffs, data, len);
  if ((ret > 0) && (copy_to_user(buf, data, len)))
  ret = -EFAULT;
__ffs_ep0_queue_wait() returns req->actual, which on a short
control OUT transfer is strictly less than len.  The
copy_to_user() call still copies len bytes, so on a short OUT
the last (len - ret) bytes of the kmalloc() buffer --
uninitialised slab residue -- are delivered to the FunctionFS
daemon.
Short ep0 OUT completions are specified USB control-transfer
behavior and are produced by in-tree UDCs:
  * dwc2 continues on req->actual < req->length for ep0 DATA OUT
  (short-not-ok is the only ep0-OUT stall path).
  * aspeed_udc ends ep0 OUT on rx_len < ep->ep.maxpacket.
  * renesas_usbf logs "ep0 short packet" and completes the
  request.
  * dwc3 stalls on short IN but not on short OUT.
A short ep0 OUT is therefore not evidence of a broken UDC; it is
a normal condition f_fs has to cope with.  The sibling gadgetfs
implementation in drivers/usb/gadget/legacy/inode.c already does
this correctly via min(len, dev->req->actual) before
copy_to_user().  This patch brings f_fs.c to the same safe
pattern rather than trimming at a defensive layer.
The bug is reached from the FunctionFS device node, which in
real deployments is owned by the privileged gadget daemon
(adbd, UMS, composite gadget services, etc.); it is not
reachable from unprivileged userspace.  Linux host stacks
normally reject short-wLength control OUTs before they reach
the gadget, so reproducing this required a build that
bypasses that host-side check.  With the bypass in place, a
1-byte payload on a 64-byte Setup produces 63 bytes of
non-canary slab residue in the daemon's read buffer.
Fix by copying only ret (actually received) bytes to
userspace. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
USB: serial: mct_u232: fix memory corruption with small endpoint
The driver overrides the maximum transfer size for a specific device
which only accepts 16 byte packets for its 32 byte bulk-out endpoint.
Make sure to never increase the maximum transfer size to prevent slab
corruption should a malicious device report a smaller endpoint max
packet size than expected. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
USB: serial: keyspan: fix missing indat transfer sanity check
Add the missing sanity check on the size of usa49wg indat transfers to
avoid parsing stale or uninitialised slab data. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
USB: serial: belkin_sa: validate interrupt status length
The Belkin interrupt callback treats interrupt data as a four-byte
status report and reads LSR/MSR fields at offsets 2 and 3. The
interrupt-in buffer length is derived from endpoint wMaxPacketSize, and
short interrupt transfers may complete successfully with a smaller
actual_length.
Check the completed interrupt packet length before parsing status
fields so short interrupt endpoints and short successful packets are
ignored instead of causing out-of-bounds or stale status-byte reads.
KASAN report as below:
BUG: KASAN: slab-out-of-bounds in belkin_sa_read_int_callback()
Read of size 1
Call trace:
  belkin_sa_read_int_callback() (drivers/usb/serial/belkin_sa.c:202)
  __usb_hcd_giveback_urb() (drivers/usb/core/hcd.c:1630)
  dummy_timer() (?:?) | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
usbip: vudc: Fix use after free bug in vudc_remove due to race condition
This patch follows up Zheng Wang's 2023 report of a use-after-free in
vudc_remove(). The original thread stalled on Shuah Khan's request for
runtime testing of the unplug/unbind path. This patch supplies that
testing and keeps Zheng's original fix shape.
In vudc_probe(), v_init_timer() binds udc->tr_timer.timer to v_timer().
usbip_sockfd_store() starts the timer via v_start_timer()/v_kick_timer().
vudc_remove() can then free the containing struct vudc while the timer is
still pending or executing.
KASAN confirms the race on an unpatched x86_64 QEMU guest with
CONFIG_KASAN=y, CONFIG_USBIP_VUDC=y, CONFIG_USB_ZERO=y, and a tight loop
that repeatedly writes a socket fd to usbip_sockfd, closes the socket
pair, and unbinds/rebinds usbip-vudc.0:
  BUG: KASAN: slab-use-after-free in __run_timer_base.part.0+0x8ba/0x8e0
  Write of size 8 at addr ffff888001b80740 by task trigger_and_unb/239
  Allocated by task 239:
  vudc_probe+0x4d/0xaa0
  Freed by task 239:
  kfree+0x18f/0x520
  device_release_driver_internal+0x388/0x540
  unbind_store+0xd9/0x100
This lands in the timer core rather than v_timer() itself because the
embedded timer_list is being walked after its containing struct vudc has
already been freed. The underlying lifetime bug is the same one Zheng
reported.
With v_stop_timer() called from vudc_remove() and the timer deleted
synchronously, the same harness completed 5000 bind/unbind iterations
with no KASAN report. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
usb: musb: omap2430: Fix use-after-free in omap2430_probe()
In omap2430_probe(), of_node_put(np) is called prematurely before the
last access to np, leading to a use-after-free if the node's reference
count drops to zero. Move the of_node_put() calls after the last use of
np in both the success and error paths. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
Input: atmel_mxt_ts - fix boundary check in mxt_prepare_cfg_mem
When a configuration file provides an object size that is larger than the
driver's known mxt_obj_size(object), the driver intends to discard the
extra bytes.
The loop iterates using for (i = 0; i < size; i++). Inside the loop, the
condition to skip processing extra bytes is:
  if (i > mxt_obj_size(object))
  continue;
Since i is a 0-based index, the valid indices for the object are 0 through
mxt_obj_size(object) - 1.
When i == mxt_obj_size(object), the condition evaluates to false, and the
code processes the byte instead of discarding it.
This causes the code to calculate byte_offset = reg + i - cfg->start_ofs
and writes the byte there, overwriting exactly one byte of the adjacent
instance or object.
Update the boundary check to skip extra bytes correctly by using >=. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
dma-buf: fix UAF in dma_buf_fd() tracepoint
Once FD_ADD() returns, the fd is live in the file descriptor table
and a thread sharing that table can close() it before DMA_BUF_TRACE()
runs. The close drops the last reference, __fput() frees the dma_buf,
and the tracepoint then dereferences dmabuf to take dmabuf->name_lock
-- slab-use-after-free.
Split FD_ADD() back into get_unused_fd_flags() + fd_install() and
emit the tracepoint between them. While the fdtable slot is reserved
with a NULL file pointer, a racing close() returns -EBADF without
entering __fput(), so the dma_buf stays alive across the trace. Same
approach as commit 2d76319c4cbb ("dma-buf: fix UAF in dma_buf_put()
tracepoint").
This undoes the FD_ADD() conversion done in commit 34dfce523c90
("dma: convert dma_buf_fd() to FD_ADD()"); FD_ADD() has no place to
hook the tracepoint safely. | 
  
  
  
  | In the Linux kernel, the following vulnerability has been resolved:
xfrm: route MIGRATE notifications to caller's netns
xfrm_send_migrate() in net/xfrm/xfrm_user.c and pfkey_send_migrate()
in net/key/af_key.c both hardcode &init_net for the multicast that
announces a successful XFRM_MSG_MIGRATE / SADB_X_MIGRATE.
XFRM_MSG_MIGRATE arrives on a per-netns NETLINK_XFRM socket, and the
rest of the xfrm/af_key netlink path was made netns-aware in 2008.
The other 14 multicast paths in xfrm_user.c route their event using
xs_net(x), xp_net(xp) or sock_net(skb->sk); only the migrate path
was missed.
Two consequences of the init_net hardcoding:
  1. The notification (selector, old/new endpoint addresses, and the
  km_address) is delivered to listeners on init_net's
  XFRMNLGRP_MIGRATE / pfkey BROADCAST_ALL groups rather than on
  the issuing netns. An IKE daemon running in init_net therefore
  receives migration notifications originating from any other
  netns on the host.
  2. An IKE daemon running inside a non-init netns and subscribed
  to its own XFRMNLGRP_MIGRATE / pfkey groups never receives the
  notification of its own migration. IKEv2 MOBIKE / address-update
  handling inside a netns is silently broken.
Thread struct net through km_migrate() and the xfrm_mgr.migrate
function pointer, drop the &init_net override in xfrm_send_migrate()
and pfkey_send_migrate(), and pass the caller's net (already in
scope in xfrm_migrate() via sock_net(skb->sk)) all the way down.
struct xfrm_mgr is in-tree only and not exported as a stable API,
so the function-pointer signature change is internal.
pfkey_broadcast() is already netns-aware via net_generic(net,
pfkey_net_id) since the pernet conversion. The five other
pfkey_broadcast() callers in af_key.c already pass xs_net(x),
sock_net(sk) or a per-netns net, so this only removes the
&init_net outlier. |

---
*爬取时间: 2026-07-24 16:11:38*
*来源: 直接站点爬取*
