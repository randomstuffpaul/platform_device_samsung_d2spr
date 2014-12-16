# Copyright (C) 2012 The Android Open Source Project
# Copyright (C) 2013 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

""" Custom OTA commands for d2lterefreshspr """

def FullOTA_InstallEnd(info):
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b00"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b01"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b02"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b03"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b04"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b05"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b06"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b07"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b08"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b09"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b10"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b13"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b14"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b21"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b22"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b23"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b25"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b26"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.b29"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/firmware/modem_fw.mdt"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem.b08", "/system/etc/firmware/modem.b08"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem.b09", "/system/etc/firmware/modem.b09"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem.b10", "/system/etc/firmware/modem.b10"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b00", "/system/etc/firmware/modem_fw.b00"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b01", "/system/etc/firmware/modem_fw.b01"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b02", "/system/etc/firmware/modem_fw.b02"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b03", "/system/etc/firmware/modem_fw.b03"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b04", "/system/etc/firmware/modem_fw.b04"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b05", "/system/etc/firmware/modem_fw.b05"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b09", "/system/etc/firmware/modem_fw.b09"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b10", "/system/etc/firmware/modem_fw.b10"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b11", "/system/etc/firmware/modem_fw.b11"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b12", "/system/etc/firmware/modem_fw.b12"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b13", "/system/etc/firmware/modem_fw.b13"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b15", "/system/etc/firmware/modem_fw.b15"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b16", "/system/etc/firmware/modem_fw.b16"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b17", "/system/etc/firmware/modem_fw.b17"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b18", "/system/etc/firmware/modem_fw.b18"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b23", "/system/etc/firmware/modem_fw.b23"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b25", "/system/etc/firmware/modem_fw.b25"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b24", "/system/etc/firmware/modem_fw.b24"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b27", "/system/etc/firmware/modem_fw.b27"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b28", "/system/etc/firmware/modem_fw.b28"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.b31", "/system/etc/firmware/modem_fw.b31"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), symlink("/firmware-mdm/image/modem_fw.mdt", "/system/etc/firmware/modem_fw.mdt"));')
  info.script.AppendExtra('ifelse(is_substring("L710V", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/apns-conf-boost.xml"));')
  info.script.AppendExtra('ifelse(is_substring("L710V", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/eri-boost.xml"));')
  info.script.AppendExtra('ifelse(is_substring("S960L", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/apns-conf-boost.xml"));')
  info.script.AppendExtra('ifelse(is_substring("S960L", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/eri-boost.xml"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /system/etc/apns-conf.xml"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/etc/apns-conf-boost.xml /system/etc/apns-conf.xml"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "echo gsm.operator.alpha=Boost Mobile >> /system/build.prop"));')
  info.script.AppendExtra('ifelse(is_mounted("/data"), unmount("/data"));')
  info.script.AppendExtra('mount("ext4", "EMMC", "/dev/block/platform/msm_sdcc.1/by-name/userdata", "/data", "");')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox mv /system/etc/eri-boost.xml /data/eri.xml"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /data/data/com.android.providers.telephony/databases/telephony.db"));')
  info.script.AppendExtra('ifelse(is_substring("L710T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox rm -f /data/data/com.android.providers.telephony/databases/telephony.db-journal"));')
  info.script.AppendExtra('unmount("/data");')
