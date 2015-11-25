import geoip2.database
import json

def to_list(input):
    input = input.split('\n')
    input = input[1:-1]
    return input


reader = geoip2.database.Reader('GeoLite2-City.mmdb')

ip_list = """
66.66.119.241
99.112.73.201
76.97.251.143
108.33.191.49
173.52.85.157
173.70.220.7
69.119.51.101
184.60.227.217
73.39.65.139
108.91.49.49
"""

#ip_list = to_list(ip_list)


f = open('ip-list.txt', 'r')

for i, ip in enumerate(f):

    ip = ip.strip()

    if not ip: continue

    response = reader.city(ip)

    # print response.country.iso_code
    # print response.location.time_zone

    if response.subdivisions:
        # print response.subdivisions[0].names['en']

        if response.subdivisions[0].iso_code == 'CA':
            if response.city:
                if 'en' in response.city.names:
                    print response.city.names['en'], ", CA"


f.close()

reader.close()
