# Copyright (C) 2015 Jurriaan Bremer <jbr@cuckoo.sh>
# This file is part of HTTPReplay - http://jbremer.org/httpreplay/
# See the file 'LICENSE' for copying permission.

import httpreplay.cobweb
import httpreplay.reader
import httpreplay.smegma

def readpcap(pcap_file, tlsmaster):
    pass

def http_handler():
    return httpreplay.cobweb.HttpProtocol()

def https_handler(tlsmaster={}):
    return httpreplay.smegma.TLSStream(
        httpreplay.cobweb.HttpProtocol(), tlsmaster
    )