import math
from dataclasses import dataclass, field
from typing import List

VERSION_SUM = 0


def hex_to_input(data_in: str):
    out = []
    for c in data_in:
        out.extend(bin(int(c, 16))[2:].zfill(4))
    return out


@dataclass
class Packet:
    data: List[str]
    version: int = 0
    type_id: int = 0
    value: int = 0
    sub_packets: List["Packet"] = field(default_factory=list)
    remainder: List[str] = field(default_factory=list)

    def __post_init__(self):
        global VERSION_SUM
        self.remainder = self.data.copy()
        self.version = self.bin_to_int(self.remainder[0:3])
        self.type_id = self.bin_to_int(self.remainder[3:6])
        self.remainder = self.remainder[6:]
        if self.type_id == 4:
            self.parse_number()
        else:
            if self.remainder[0] == '0':
                self.parse_sub_packet_zero()
            elif self.remainder[0] == '1':
                self.parse_sub_packet_one()
        VERSION_SUM += self.version

    def parse_sub_packet_zero(self):
        length = self.bin_to_int(self.remainder[1:16])
        self.remainder = self.remainder[16:]
        sub_packet_data = self.remainder[:length]
        self.remainder = self.remainder[length:]
        sub_packets = True
        while sub_packets:
            try:
                new_packet = Packet(sub_packet_data)
                self.sub_packets.append(new_packet)
                sub_packet_data = new_packet.remainder
            except ValueError:
                sub_packets = False
            except IndexError:
                sub_packets = False

    def parse_sub_packet_one(self):
        length = self.bin_to_int(self.remainder[1:12])
        self.remainder = self.remainder[12:]
        for _ in range(length):
            new_packet = Packet(self.remainder)
            self.sub_packets.append(new_packet)
            self.remainder = new_packet.remainder

    def parse_number(self):
        number = []
        finished = False
        while not finished:
            number.extend(self.remainder[1:5])
            if self.remainder[0] == '0':
                finished = True
            self.remainder = self.remainder[5:]
        self.value = self.bin_to_int(number)

    @staticmethod
    def bin_to_int(binary: List[str]):
        return int(''.join(binary), 2)


def get_value(pack: Packet):
    if pack.type_id == 0:
        return sum([get_value(p) for p in pack.sub_packets])
    elif pack.type_id == 1:
        return math.prod([get_value(p) for p in pack.sub_packets])
    elif pack.type_id == 2:
        return min([get_value(p) for p in pack.sub_packets])
    elif pack.type_id == 3:
        return max([get_value(p) for p in pack.sub_packets])
    elif pack.type_id == 4:
        return pack.value
    elif pack.type_id == 5:
        return 1 if get_value(pack.sub_packets[0]) > get_value(pack.sub_packets[1]) else 0
    elif pack.type_id == 6:
        return 1 if get_value(pack.sub_packets[0]) < get_value(pack.sub_packets[1]) else 0
    elif pack.type_id == 7:
        return 1 if get_value(pack.sub_packets[0]) == get_value(pack.sub_packets[1]) else 0


with open('01.txt') as f:
    packet = Packet(hex_to_input(f.read().strip()))

print('Part 1:', VERSION_SUM)

print('Part 1:', get_value(packet))
