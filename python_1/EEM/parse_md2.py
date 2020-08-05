#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdt
import numpy as np
import dateparser
import re

# Replace with log file position
fp = r'./TAC-SF23042020.txt'

# Parse "show clock"
dt_re = r'(\d{2}:\d{2}:\d{2}.\d{3} EST \S{3} \S{3} \d{2} \d{4})'

# Per-MD log split
md_re = r'(Cable[8-9]\/0\/0) is up, line protocol is up'

# Parse per-MD US rate from "show interface CableXXX" (DS rate is wrong in this command thus useless)
md_rate_re = re.compile(r'^  30 second input rate (\d*) bits\/sec, \d* packets\/sec$', re.MULTILINE)

# Parse per-channel DS rate from "show controller XXX counters rf-channel"
chan_rate_re = re.compile(r'^\d\/0\/\d\s*\d{1,2}\s*\d*\s*\d*\s*\d*\.\d*\s*\d*\s*\d*\s*(\d{1,2}\.\d{2})$',
                          re.MULTILINE)

# Parse "show cable modem XXX counters" and extract (cm_mac, us_bytes, ds_bytes)
cm_traffic_re = re.compile(r'^([a-f0-9]{4}.[a-f0-9]{4}.[a-f0-9]{4})\s\s*\d*\s\s*(\d*)\s*\d*\s*(\d*)\s*$',
                           re.MULTILINE)

# Constants
MAX_CHAN_PER_PORT = 24
ONE_KILO = 1000
ONE_MEGA = ONE_KILO * 1000

# Interested MDs
MD_NAMES = ["Cable8/0/0", "Cable9/0/0"]
NUM_MD = len(MD_NAMES)

US_DIR = 0
DS_DIR = 1
NUM_DIR = 2

# 7KB for US, 6.3MB for DS
TRAFFIC_THRESH = [7.0 * ONE_KILO, 6.3 * ONE_MEGA]
STEP = 4    # For 1 hour

with open(fp, 'r') as fh:
    raw_log = fh.read()

    logs = re.split(dt_re, raw_log)
    logs = logs[1:]
    dt = [dateparser.parse(dt_str) for dt_str in logs[0::2]]
    logs = logs[1::2]
    num_dt = len(dt)
    assert len(logs) == num_dt

    md_us_rate = {}
    md_ds_rate = {}
    md_cm_cnt = {}
    md_cm_traffic = {}
    for md_name in MD_NAMES:
        md_us_rate[md_name] = np.zeros(num_dt, dtype=np.float)
        md_ds_rate[md_name] = np.zeros(num_dt, dtype=np.float)
        md_cm_cnt[md_name] = np.zeros(num_dt, dtype=np.int)
        md_cm_traffic[md_name] = {}

    for index, log in enumerate(logs):
        md_logs = re.split(md_re, log)
        md_logs = md_logs[1:]

        md_dict_logs = dict(zip(md_logs[0::2], md_logs[1::2]))

        # Error handling for incomplete log
        if NUM_MD != len(md_dict_logs):
            print("Index %d len %d" % (index, len(md_dict_logs)))
            continue

        for md_name, md_log in md_dict_logs.items():
            tmp = md_rate_re.search(md_log)
            assert tmp is not None

            md_us_rate[md_name][index] = float(tmp.group(1)) / ONE_MEGA

            tmp = chan_rate_re.findall(md_log)
            assert len(tmp) <= MAX_CHAN_PER_PORT
            chan_rate = [float(rate) for rate in tmp]
            md_ds_rate[md_name][index] = sum(chan_rate)

            for match in cm_traffic_re.finditer(md_log):
                cm_mac = match.group(1)
                if match.group(2) == '':
                    print("Missed CM Counter index %d %s CM %s str %s" % (index, md_name, cm_mac, match.group(0)))
                    continue
                us_byte = int(match.group(2))
                ds_byte = int(match.group(3))

                if cm_mac not in md_cm_traffic[md_name]:
                    md_cm_traffic[md_name][cm_mac] = np.zeros([NUM_DIR, num_dt], dtype=np.int)

                assert index < num_dt
                md_cm_traffic[md_name][cm_mac][US_DIR][index] = us_byte
                md_cm_traffic[md_name][cm_mac][DS_DIR][index] = ds_byte

            md_cm_cnt[md_name][index] = len(md_cm_traffic[md_name])

    dt_new = dt[1::STEP]
    num_dt_new = len(dt_new)
    assert num_dt_new == len(dt[0:-1:STEP])
    md_act_cm_cnt = {}
    for md_name, cm_traffic in md_cm_traffic.items():
        act_cm_cnt = np.zeros([NUM_DIR, num_dt_new], dtype=np.int)
        for mac, traffic in cm_traffic.items():
            traffic_delta = traffic[:, 1::STEP] - traffic[:, 0:-1:STEP]
            us_active = np.where(traffic_delta[US_DIR] >= (STEP * TRAFFIC_THRESH[US_DIR]), 1, 0)
            ds_active = np.where(traffic_delta[DS_DIR] >= (STEP * TRAFFIC_THRESH[DS_DIR]), 1, 0)
            assert len(us_active) == num_dt_new
            assert len(ds_active) == num_dt_new
            act_cm_cnt += np.stack((us_active, ds_active))
        md_act_cm_cnt[md_name] = act_cm_cnt

    for index, (md_name, act_cm_cnt) in enumerate(md_act_cm_cnt.items()):
        plt.figure(index + 1)
        plt.title(md_name)
        plt.plot(dt_new, md_cm_cnt[md_name][1::STEP], 'o', label="CM Count")
        plt.plot(dt_new, act_cm_cnt[US_DIR], 'o', label="Active CM US")
        plt.legend()
        plt.grid(True)
        plt.ylim(bottom=0)
        plt.gcf().autofmt_xdate()

    plt.figure(3)
    plt.title('US Throughput (Mbps)')
    for md_name, us_rate in md_us_rate.items():
        plt.plot(dt, us_rate, label=md_name)
    plt.legend()
    plt.grid(True)
    plt.ylim(bottom=0)
    #plt.gca().xaxis.set_major_formatter(mdt.DateFormatter('%m-%d %H:%M'))
    plt.gcf().autofmt_xdate()

    plt.figure(4)
    plt.title('DS Throughput (Mbps)')
    for md_name, ds_rate in md_ds_rate.items():
        plt.plot(dt, ds_rate, label=md_name)
    plt.legend()
    plt.grid(True)
    plt.ylim(bottom=0)
    #plt.gca().xaxis.set_major_formatter(mdt.DateFormatter('%m-%d %H:%M'))
    plt.gcf().autofmt_xdate()

    plt.show()
