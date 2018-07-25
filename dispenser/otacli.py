import network
import machine
import os
import time

import ospath
import usocket
import utarfile

import config

def url_open(url):
    """ copied from micropython-lib - library upip """
    
    print("url=%s" % url)

    proto, _, host, urlpath = url.split('/', 3)
    host, port = host.split(":", 2)
    try:
        s = usocket.socket()
        # s.bind((config.OTA["bind_ip"], 1415))
        ai = usocket.getaddrinfo(host, port)
        print("ai = %r" % ai)
        print("ai[0][-1] = %s" % (ai[0][-1],))
    except OSError as e:
        fatal("Unable to resolve %s:%s (no Internet?)" % host, port,  e)
    
    try:
        s.settimeout(10)
        s.connect(ai[0][-1])
        # s.settimeout(None)
        print("after connect")

        # MicroPython rawsocket module supports file interface directly
        s.write("GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n" % (urlpath, host))
        l = s.readline()
        protover, status, msg = l.split(None, 2)
        if status != b"200":
            if status == b"404" or status == b"301":
                raise NotFoundError("URL not found")
            raise ValueError(status)
        while 1:
            l = s.readline()
            if not l:
                raise ValueError("Unexpected EOF in HTTP headers")
            if l == b'\r\n':
                break
    except Exception as e:
        s.close()
        raise e

    return s

def check():
    """ connect to service WIFI network, connect to service addr/port and check if 
        there are new files to put here """

    print('connecting to service %s network' % config.OTA["SSID"])
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(config.OTA["SSID"], config.OTA["password"])

    for x in range(config.OTA["wifi_conn_timeout"]):
        if station.isconnected():
            print("connected to service wifi")
            break
        time.sleep(1)
    else:
        print("service wifi timeout. network not active or too slow, giving up")
        return False

    try:
        # set ip to service ip
        ifconfig = station.ifconfig()
        station.ifconfig((config.OTA["bind_ip"], "255.255.255.0", ifconfig[2], ifconfig[3]))
        return check_over_ip(config.OTA["node_type"])
    finally:
        # set it back
        station.ifconfig(ifconfig)




def check_over_ip(node_type):
    """ tcp/ip stage of checking of OTA"""

    try:
        resp = url_open("http://10.11.12.13:1415/%s/version.txt" % node_type)
    except OSError:
        print("no version found")
        return False

    remote_version = resp.read().decode("utf-8").strip()
    print("remote version = %s", remote_version)

    try:
        local_version = open(".otaversion").read().strip()
    except OSError:
        print("no local version found")
        local_version = ""

    print("local_version = %s remote_version=%s" % (local_version, remote_version))

    if local_version == remote_version:
        print("skipping")
        return False

    print("doing OTA")

    resp = url_open("http://10.11.12.13:1415/%s/%s.tar" % (node_type, remote_version))

    ftar = utarfile.TarFile(fileobj=resp)
    meta = install_tar(ftar)

    fver = open(".otaversion", "wb")
    fver.write(remote_version)
    fver.close()

    del fver
    del resp
    del ftar
    del meta
    
    print("OTA PERFORMED, doing reboot")
    machine.reset()



def install_tar(f):
    """ copied and modified from micropython-lib/upip """
    meta = {}
    for info in f:
        print(info)
        fname = info.name

        outfname = fname
        if info.type != utarfile.DIRTYPE:
            print("Extracting " + outfname)
            _makedirs(outfname)
            subf = f.extractfile(info)
            save_file(outfname, subf)
    return meta


# Expects *file* name
def _makedirs(name, mode=0o777):
    """ copied (and modified?) from micropython-lib upython """
    dirname = ospath.dirname(name)
    print("mkdir dirname=%s" % dirname)
    try:
        os.mkdir(dirname)
        print("made dir %s" % dirname)
    except OSError as e:
        if e.args[0] != errno.EEXIST and e.args[0] != errno.EISDIR:
            raise

file_buf = bytearray(512)

def save_file(fname, subf):
    global file_buf

    with open(fname, "wb") as outf:
        while True:
            sz = subf.readinto(file_buf)
            if not sz:
                break
            outf.write(file_buf, sz)






