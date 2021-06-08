import re
from network.connection import Connection


def read_ip_addresses_file(file_name: str) -> dict:
    s = set()
    ip_address_dict = dict()
    with open(file_name, 'rt') as reader:
        for line in reader:
            split = re.split(r'\(|\)[ \t]*:|,', line)
            try:
                ip_address = split[3].strip()
                i1 = int(split[1])
                i2 = int(split[2])
            except (ValueError, IndexError):
                raise SyntaxError('Syntax error in file with ip addresses')
            length_ip_address = len(s)
            s.add(ip_address)
            if length_ip_address == len(s):
                raise ValueError('Non unique ip address')
            length_key = len(ip_address_dict)
            ip_address_dict[(i1, i2)] = ip_address
            if length_key == len(ip_address_dict):
                raise ValueError('Non unique key')
    return ip_address_dict


class DetectorSet:
    def __init__(self, ip_map: dict):
        self.connections = dict()
        for key, ip in ip_map.items():
            connection = Connection(ip, Connection.PORT)
            self.connections[key] = connection

    def start_all_detectors(self, voltages: dict) -> dict:
        result_dict = dict()
        for key, connection in self.connections:
            result = connection.do_cmd(('start_all', voltages[key]))
            result_dict[key] = result
        return result_dict

    def stop_all_detectors(self) -> dict:
        result_dict = dict()
        for key, connection in self.connections:
            result = connection.do_cmd(('stop_all', ))
            result_dict[key] = result
        return result_dict

    def start_hub_detectors(self, key: tuple, voltages: list) -> list:
        return self.connections[key].do_cmd(('start_hub', voltages))

    def stop_hub_detectors(self, key: tuple) -> list:
        return self.connections[key].do_cmd(('stop_hub', ))

    def start_detector_bar(self, key: tuple, no: int, voltage: float) -> list:
        return self.connections[key].do_cmd(('start_bar', no, voltage))

    def stop_detector_bar(self, no: int, key: tuple) -> list:
        return self.connections[key].do_cmd(('stop_bar', no))
