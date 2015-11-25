# geoip2

Geo IP lookup using free downloadable database.

## Installation

```sh
pip install geoip2
```

## Example Response
```json
{
  "city": {
    "geoname_id": 5128581,
    "names": {
      "de": "New York City",
      "zh-CN": "纽约",
      "en": "New York",
      "fr": "New York",
      "ru": "Нью-Йорк",
      "pt-BR": "Nova Iorque",
      "es": "Nueva York",
      "ja": "ニューヨーク"
    }
  },
  "continent": {
    "names": {
      "fr": "Amérique du Nord",
      "zh-CN": "北美洲",
      "de": "Nordamerika",
      "en": "North America",
      "es": "Norteamérica",
      "ja": "北アメリカ",
      "ru": "Северная Америка",
      "pt-BR": "América do Norte"
    },
    "geoname_id": 6255149,
    "code": "NA"
  },
  "postal": {
    "code": "10009"
  },
  "country": {
    "names": {
      "ja": "アメリカ合衆国",
      "es": "Estados Unidos",
      "ru": "США",
      "pt-BR": "Estados Unidos",
      "fr": "États-Unis",
      "zh-CN": "美国",
      "de": "USA",
      "en": "United States"
    },
    "iso_code": "US",
    "geoname_id": 6252001
  },
  "location": {
    "latitude": 40.7252,
    "time_zone": "America/New_York",
    "longitude": -73.9802,
    "metro_code": 501
  },
  "registered_country": {
    "names": {
      "fr": "États-Unis",
      "en": "United States",
      "zh-CN": "美国",
      "de": "USA",
      "ja": "アメリカ合衆国",
      "es": "Estados Unidos",
      "pt-BR": "Estados Unidos",
      "ru": "США"
    },
    "iso_code": "US",
    "geoname_id": 6252001
  },
  "traits": {
    "domain": "cogentco.com",
    "ip_address": "38.99.201.211",
    "organization": "Cogent Communications",
    "isp": "Cogent Communications",
    "autonomous_system_number": 174,
    "autonomous_system_organization": "Cogent Communications"
  },
  "subdivisions": [
    {
      "iso_code": "NY",
      "names": {
        "ru": "Нью-Йорк",
        "pt-BR": "Nova Iorque",
        "ja": "ニューヨーク州",
        "es": "Nueva York",
        "zh-CN": "纽约州",
        "de": "New York",
        "en": "New York",
        "fr": "New York"
      },
      "geoname_id": 5128638
    }
  ],
  "represented_country": {
    "names": {}
  }
}
```

## Reference

http://dev.maxmind.com/geoip/geoip2/downloadable/
