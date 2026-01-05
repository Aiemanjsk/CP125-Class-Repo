def find_station(stations, name):
    for i in range(len(stations)):
        if stations[i] == name:
            return i
    return -1
pass

def count_stops(stations, start, stop):
    for i in range(len(stations)):
        if stations[i] == start:
            for j in range(len(stations)):
                if stations[j] == stop:
                    if j > i:
                        return (j - i)
                    else:
                        return (i - j)
            return -1
    return -1 
    pass

stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]

