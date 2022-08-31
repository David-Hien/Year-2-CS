class ippacket:
    '''
    tx: Sender, rx: Receiver
    port: integer 0 – 2^16
    mac: string BA:AA:09:89:0A:00
    ip: string 192.168.0.2
    '''

    def __init__(self, port_tx, port_rx, mac_tx, mac_rx, ip_tx, ip_rx):
        self.port_tx = self.port2bin(port_tx)
        self.port_rx = self.port2bin(port_rx)
        self.mac_tx = self.mac2bin(mac_tx.split(':'))
        self.mac_rx = self.mac2bin(mac_rx.split(':'))
        self.ip_tx = self.ip2bin(ip_tx.split('.'))
        self.ip_rx = self.ip2bin(ip_rx.split('.'))

    def binirize(self, number: int) -> str:
        result = ""

        while number > 0:
            result = str(number % 2) + result
            number = number // 2

        return result.rjust(8, '0')

    def hex2dex(self, hex: str) -> int:
        symbols = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        result = 0

        for i in range(len(hex)):
            if hex[i].isalpha():
                result += symbols[hex[i]] * 16 ** (len(hex) - 1 - i)
            else:
                result += int(hex[i]) * 16 ** (len(hex) - 1 - i)

        return result

    def ip2bin(self, ip: list) -> str:
        result = ""

        for i in ip:
            result += self.binirize(int(i))

        return result

    def mac2bin(self, mac: list) -> str:
        result = ""

        for i in mac:
            result += self.binirize(self.hex2dex(i))

        return result

    def port2bin(self, port: int) -> str:
        return self.binirize(port)

    def build(self) -> str:
        result = self.ip_tx + self.mac_tx + self.port_tx + \
            self.ip_rx + self.mac_rx + self.port_rx

        return result


test1 = ippacket(port_tx=80, port_rx=443, mac_tx='BA:AA:09:89:0A:00',
                 mac_rx='BA:AA:09:89:0A:01', ip_tx='10.10.0.1', ip_rx='10.0.0.2')
print(test1.build())