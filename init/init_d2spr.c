/*
   Copyright (c) 2013, The Linux Foundation. All rights reserved.

   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions are
   met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above
      copyright notice, this list of conditions and the following
      disclaimer in the documentation and/or other materials provided
      with the distribution.
    * Neither the name of The Linux Foundation nor the names of its
      contributors may be used to endorse or promote products derived
      from this software without specific prior written permission.

   THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESS OR IMPLIED
   WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
   MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT
   ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS
   BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
   CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
   SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
   BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
   WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
   OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
   IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include <stdlib.h>

#include "vendor_init.h"
#include "property_service.h"
#include "log.h"
#include "util.h"

void vendor_load_properties()
{
    char platform[PROP_VALUE_MAX];
    char bootloader[PROP_VALUE_MAX];
    char device[PROP_VALUE_MAX];
    char devicename[PROP_VALUE_MAX];
    int rc;

    rc = property_get("ro.board.platform", platform);
    if (!rc || strncmp(platform, ANDROID_TARGET, PROP_VALUE_MAX))
        return;

    property_get("ro.bootloader", bootloader);

    if (strstr(bootloader, "L710T")) {
        /* d2lterefreshspr */
        property_set("ro.build.fingerprint", "samsung/d2lterefreshspr/d2lterefreshspr:4.4.2/KOT49H/L710TVPU0ANF4:user/release-keys");
        property_set("ro.build.description", "d2lterefreshspr-user 4.4.2 KOT49H L710TVPU0ANF4 release-keys");
        property_set("ro.product.device", "d2lterefreshspr");
        property_set("ro.product.model", "SPH-L710T");
        property_set("ro.cdma.home.operator.numeric", "311870");
        property_set("ro.cdma.home.operator.alpha", "Boost Mobile");
        property_set("ro.product.locale.region", "US");
        property_set("gsm.sim.operator.alpha", "Boost Mobile");
        property_set("gsm.sim.operator.numeric", "311870");
        property_set("gsm.operator.alpha", "Boost Mobile");
        property_set("gsm.operator.numeric", "311870");
        property_set("gsm.sim.operator.iso-country", "US");
        property_set("gsm.operator.iso-country", "US");
    } else {
        /* d2spr */
        property_set("ro.build.fingerprint", "samsung/d2spr/d2spr:4.4.2/KOT49H/L710VPUDND8:user/release-keys");
        property_set("ro.build.description", "d2spr-user 4.4.2 KOT49H L710VPUDND8 release-keys");
        property_set("ro.product.device", "d2spr");
        property_set("ro.product.model", "SPH-L710");
        property_set("ro.cdma.home.operator.numeric", "310120");
        property_set("ro.cdma.home.operator.alpha", "Sprint");

    }
    /* common */
    property_set("rild.libargs", "-d /dev/smd0");
    property_set("ro.telephony.default_network", "8");
    property_set("telephony.lteOnCdmaDevice", "1");
    property_set("telephony.sms.pseudo_multipart", "1");
    property_set("persist.radio.snapshot_enabled", "1");
    property_set("persist.radio.snapshot_timer", "22");
    property_set("persist.eons.enabled", "false");
    property_set("ro.ril.svdo", "true");


    property_get("ro.product.device", device);
    ERROR("Found bootloader id %s setting build properties for %s device\n", bootloader, device);

}

