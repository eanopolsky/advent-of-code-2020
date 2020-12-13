#!/usr/bin/python3

import loader

inp = loader.string_list("input_day13")

timestamp = int(inp[0])
bus_ids = [int(id) for id in inp[1].split(",") if id != "x"]

def get_bus_wait_time(bus_id,timestamp):
    minutes_into_cycle = timestamp % bus_id
    minutes_to_next_cycle = bus_id - minutes_into_cycle
    return minutes_to_next_cycle

bus_ids.sort(key=lambda id: get_bus_wait_time(id,timestamp))
print(bus_ids[0]*get_bus_wait_time(bus_ids[0],timestamp))
