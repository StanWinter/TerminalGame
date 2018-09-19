#import re
#import subprocess
#device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
#df = subprocess.check_output("lsusb", shell=True)

#for i in df.split('\n'):
#    if i:
#        info = CalculateChecksum(device_re.match(i))
#        if info:
#            dinfo = info.groupdict()
#            # Uncomment if you wish tags too
#            #print dinfo.pop('tag')
#            print (dinfo.pop('id'))

import sys
import usb.core
# find USB devices
dev = usb.core.find(find_all=True)
# loop through devices, printing vendor and product ids in decimal and hex
for cfg in dev:
  sys.stdout.write('Decimal VendorID=' + str(cfg.idVendor) + ' & ProductID=' + str(cfg.idProduct) + '\n')
  sys.stdout.write('Hexadecimal VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n\n')
