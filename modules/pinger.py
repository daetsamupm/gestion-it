import nmap


nm = nmap.PortScanner()

# nm.scan('127.0.0.1', '22-443')
# nm.command_line()
#
# nm.scaninfo()
#
# nm.all_hosts()
#
# nm['127.0.0.1'].hostname()
#
# nm['127.0.0.1'].state()
#
# nm['127.0.0.1'].all_protocols()

# nm.scan(hosts='10.102.83.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
# hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
# for host, status in hosts_list:
#     print('{0}:{1}'.format(host, status))

# nm1 = nmap.PortScannerYield()
# for progressive_result in nm1.scan('10.102.83.0/24', '22-25'):
#     print(progressive_result)

nma = nmap.PortScannerAsync()
def callback_result(host, scan_result):
    print('------------------')
    print(host, scan_result)

nma.scan(hosts='10.102.83.0/24', arguments='-sP', callback=callback_result)
while nma.still_scanning():
    print("Waiting >>>")
    nma.wait(2)