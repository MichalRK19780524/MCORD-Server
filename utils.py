import re


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
