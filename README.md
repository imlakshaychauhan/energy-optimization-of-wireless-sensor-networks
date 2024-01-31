# Wireless Sensor Network Simulation using GDLR

## Overview

This project implements a Wireless Sensor Network (WSN) simulation using the Grey Wolf Optimizer driven LEACH Routing (GDLR) algorithm. The simulation is designed to optimize energy consumption, cluster formation, and data aggregation in a WSN. The project is implemented in Python.

## Model Description

The simulation model is encapsulated in the `Model` class. Key parameters and their values include:

- `n`: Number of nodes in the network.
- `x`, `y`: Dimensions of the field.
- `sink_x`, `sink_y`: Coordinates of the sink node.
- `sinkE`: Initial energy of the sink node.
- `p`: Probability of a node becoming a cluster head.
- Energy Model Parameters:
  - `Eo`: Initial energy of nodes.
  - `Eelec`, `ETX`, `ERX`: Energy dissipation parameters.
  - `Efs`, `Emp`: Transmit amplifier energy.
  - `EDA`: Data aggregation energy.
  - `do`: Optimal distance for energy-efficient transmission.
- Runtime Parameters:
  - `rmax`: Maximum number of simulation rounds.
  - `data_packet_len`: Size of data packets.
  - `hello_packet_len`: Size of hello packets.
  - `NumPacket`: Number of packets sent in steady-state.
  - `RR`: Radio range of nodes.

## Simulation Results

### Screenshots

1. **Alive Nodes Graph:**
   - ![Alive Nodes](https://github.com/imlakshaychauhan/energy-optimization-of-wireless-sensor-networks/assets/70480042/4a5caf67-3d81-4e91-bbb9-5f5e1ceec44c)

2. **Top 4 Solutions:**
   - ![GWO Solution](https://github.com/imlakshaychauhan/energy-optimization-of-wireless-sensor-networks/assets/70480042/bb9e2059-f369-4d5f-b9cf-7ce5ff112902)


## Dependencies
- Python 3.x

## Usage

```bash
git clone https://github.com/imlakshaychauhan/energy-optimization-of-wireless-sensor-networks
cd energy-optimization-of-wireless-sensor-networks
cd src
python gwo.py
cd ..
python Leach.py
