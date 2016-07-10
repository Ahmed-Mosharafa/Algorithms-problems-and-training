time = raw_input().strip()
if time[-2] == "P" and time[0:2] != "12":
    time = str(int(time[0:2]) + 12)+ time[2:]
elif time[-2] == "A":
    if time [0:2] != "12":
        time = "0" + time[1] + time[2:]
    else:
        time = "00" + time[2:]
print time[:-2]