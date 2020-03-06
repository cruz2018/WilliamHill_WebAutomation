
import json




 # def testRequestResponse():
 #     # Send a request to he API server and store the response
 #     response = request.get('https://api.carbonintensity.org.uk/regional')
 #     # Confirm thatt he request-response is complete
 #    assert response.status_code == 200
 #    print(response.json())


#payload = {'dnoregion': 'Scottish Hydro Electric Power Distribution', 'shortname': 'North Scotland'}
#json_response = r.json()
# assert r.status_code == 200
# print(json_response)
#print(json_response)

#API URL
# url =  requests.get('https://api.carbonintensity.org.uk/regional')
# # Read Input
# response = requests.get(url)
# print(url)
#
# import requests
# class MyTest:
#     def API_TESTER(self):
#         x = requests.get('https://api.carbonintensity.org.uk/regional')
#         print(x.status_code)
#

mydict = {
    {
        "data": [
            {
                "from": "2020-02-25T12:00Z",
                "to": "2020-02-25T12:30Z",
                "regions": [
                    {
                        "regionid": 1,
                        "dnoregion": "Scottish Hydro Electric Power Distribution",
                        "shortname": "North Scotland",
                        "intensity": {
                            "forecast": 108,
                            "index": "low"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 0
                            },
                            {
                                "fuel": "coal",
                                "perc": 0
                            },
                            {
                                "fuel": "imports",
                                "perc": 0
                            },
                            {
                                "fuel": "gas",
                                "perc": 27.9
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 0
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 51.3
                            },
                            {
                                "fuel": "solar",
                                "perc": 0
                            },
                            {
                                "fuel": "wind",
                                "perc": 20.8
                            }
                        ]
                    },
                    {
                        "regionid": 2,
                        "dnoregion": "SP Distribution",
                        "shortname": "South Scotland",
                        "intensity": {
                            "forecast": 31,
                            "index": "very low"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 2.7
                            },
                            {
                                "fuel": "coal",
                                "perc": 0
                            },
                            {
                                "fuel": "imports",
                                "perc": 0
                            },
                            {
                                "fuel": "gas",
                                "perc": 7.3
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 38.9
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 1.1
                            },
                            {
                                "fuel": "solar",
                                "perc": 2.3
                            },
                            {
                                "fuel": "wind",
                                "perc": 47.7
                            }
                        ]
                    },
                    {
                        "regionid": 3,
                        "dnoregion": "Electricity North West",
                        "shortname": "North West England",
                        "intensity": {
                            "forecast": 29,
                            "index": "very low"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 2.5
                            },
                            {
                                "fuel": "coal",
                                "perc": 0.3
                            },
                            {
                                "fuel": "imports",
                                "perc": 0
                            },
                            {
                                "fuel": "gas",
                                "perc": 6.2
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 47.9
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 1.6
                            },
                            {
                                "fuel": "solar",
                                "perc": 2.2
                            },
                            {
                                "fuel": "wind",
                                "perc": 39.3
                            }
                        ]
                    },
                    {
                        "regionid": 4,
                        "dnoregion": "NPG North East",
                        "shortname": "North East England",
                        "intensity": {
                            "forecast": 49,
                            "index": "very low"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 21.8
                            },
                            {
                                "fuel": "coal",
                                "perc": 0.4
                            },
                            {
                                "fuel": "imports",
                                "perc": 0
                            },
                            {
                                "fuel": "gas",
                                "perc": 4.9
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 59.7
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 1
                            },
                            {
                                "fuel": "solar",
                                "perc": 5.1
                            },
                            {
                                "fuel": "wind",
                                "perc": 7.1
                            }
                        ]
                    },
                    {
                        "regionid": 5,
                        "dnoregion": "NPG Yorkshire",
                        "shortname": "Yorkshire",
                        "intensity": {
                            "forecast": 285,
                            "index": "high"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 36
                            },
                            {
                                "fuel": "coal",
                                "perc": 4.9
                            },
                            {
                                "fuel": "imports",
                                "perc": 0
                            },
                            {
                                "fuel": "gas",
                                "perc": 49.9
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 0
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 0
                            },
                            {
                                "fuel": "solar",
                                "perc": 1.7
                            },
                            {
                                "fuel": "wind",
                                "perc": 7.5
                            }
                        ]
                    },
                    {
                        "regionid": 6,
                        "dnoregion": "SP Manweb",
                        "shortname": "North Wales and Merseyside",
                        "intensity": {
                            "forecast": 299,
                            "index": "high"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 0
                            },
                            {
                                "fuel": "coal",
                                "perc": 26.6
                            },
                            {
                                "fuel": "imports",
                                "perc": 0
                            },
                            {
                                "fuel": "gas",
                                "perc": 13.4
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 0
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 7.5
                            },
                            {
                                "fuel": "solar",
                                "perc": 8.3
                            },
                            {
                                "fuel": "wind",
                                "perc": 44.2
                            }
                        ]
                    },
                    {
                        "regionid": 7,
                        "dnoregion": "WPD South Wales",
                        "shortname": "South Wales",
                        "intensity": {
                            "forecast": 326,
                            "index": "high"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 0
                            },
                            {
                                "fuel": "coal",
                                "perc": 0
                            },
                            {
                                "fuel": "imports",
                                "perc": 0
                            },
                            {
                                "fuel": "gas",
                                "perc": 82.6
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 0
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 0
                            },
                            {
                                "fuel": "solar",
                                "perc": 7
                            },
                            {
                                "fuel": "wind",
                                "perc": 10.4
                            }
                        ]
                    },
                    {
                        "regionid": 8,
                        "dnoregion": "WPD West Midlands",
                        "shortname": "West Midlands",
                        "intensity": {
                            "forecast": 260,
                            "index": "high"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 11.5
                            },
                            {
                                "fuel": "coal",
                                "perc": 2.7
                            },
                            {
                                "fuel": "imports",
                                "perc": 0
                            },
                            {
                                "fuel": "gas",
                                "perc": 56.2
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 0.6
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 10.7
                            },
                            {
                                "fuel": "solar",
                                "perc": 5.5
                            },
                            {
                                "fuel": "wind",
                                "perc": 12.8
                            }
                        ]
                    },
                    {
                        "regionid": 9,
                        "dnoregion": "WPD East Midlands",
                        "shortname": "East Midlands",
                        "intensity": {
                            "forecast": 367,
                            "index": "very high"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 0
                            },
                            {
                                "fuel": "coal",
                                "perc": 12.1
                            },
                            {
                                "fuel": "imports",
                                "perc": 0
                            },
                            {
                                "fuel": "gas",
                                "perc": 64.1
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 0
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 0
                            },
                            {
                                "fuel": "solar",
                                "perc": 9
                            },
                            {
                                "fuel": "wind",
                                "perc": 14.8
                            }
                        ]
                    },
                    {
                        "regionid": 10,
                        "dnoregion": "UKPN East",
                        "shortname": "East England",
                        "intensity": {
                            "forecast": 70,
                            "index": "low"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 0.6
                            },
                            {
                                "fuel": "coal",
                                "perc": 0.2
                            },
                            {
                                "fuel": "imports",
                                "perc": 0.2
                            },
                            {
                                "fuel": "gas",
                                "perc": 17
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 23.7
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 0
                            },
                            {
                                "fuel": "solar",
                                "perc": 15.6
                            },
                            {
                                "fuel": "wind",
                                "perc": 42.7
                            }
                        ]
                    },
                    {
                        "regionid": 11,
                        "dnoregion": "WPD South West",
                        "shortname": "South West England",
                        "intensity": {
                            "forecast": 104,
                            "index": "low"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 0
                            },
                            {
                                "fuel": "coal",
                                "perc": 0
                            },
                            {
                                "fuel": "imports",
                                "perc": 0
                            },
                            {
                                "fuel": "gas",
                                "perc": 27.1
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 32.3
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 0
                            },
                            {
                                "fuel": "solar",
                                "perc": 34.6
                            },
                            {
                                "fuel": "wind",
                                "perc": 6
                            }
                        ]
                    },
                    {
                        "regionid": 12,
                        "dnoregion": "SSE South",
                        "shortname": "South England",
                        "intensity": {
                            "forecast": 237,
                            "index": "moderate"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 6.3
                            },
                            {
                                "fuel": "coal",
                                "perc": 2.1
                            },
                            {
                                "fuel": "imports",
                                "perc": 7.9
                            },
                            {
                                "fuel": "gas",
                                "perc": 49.7
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 5.3
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 1.1
                            },
                            {
                                "fuel": "solar",
                                "perc": 21.1
                            },
                            {
                                "fuel": "wind",
                                "perc": 6.5
                            }
                        ]
                    },
                    {
                        "regionid": 13,
                        "dnoregion": "UKPN London",
                        "shortname": "London",
                        "intensity": {
                            "forecast": 241,
                            "index": "moderate"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 7.4
                            },
                            {
                                "fuel": "coal",
                                "perc": 2.6
                            },
                            {
                                "fuel": "imports",
                                "perc": 39
                            },
                            {
                                "fuel": "gas",
                                "perc": 33.6
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 1.1
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 0.8
                            },
                            {
                                "fuel": "solar",
                                "perc": 5.5
                            },
                            {
                                "fuel": "wind",
                                "perc": 10
                            }
                        ]
                    },
                    {
                        "regionid": 14,
                        "dnoregion": "UKPN South East",
                        "shortname": "South East England",
                        "intensity": {
                            "forecast": 208,
                            "index": "moderate"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 0
                            },
                            {
                                "fuel": "coal",
                                "perc": 0
                            },
                            {
                                "fuel": "imports",
                                "perc": 62.8
                            },
                            {
                                "fuel": "gas",
                                "perc": 21.8
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 0
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 1
                            },
                            {
                                "fuel": "solar",
                                "perc": 4.5
                            },
                            {
                                "fuel": "wind",
                                "perc": 9.9
                            }
                        ]
                    },
                    {
                        "regionid": 15,
                        "dnoregion": "England",
                        "shortname": "England",
                        "intensity": {
                            "forecast": 204,
                            "index": "moderate"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 8.6
                            },
                            {
                                "fuel": "coal",
                                "perc": 4
                            },
                            {
                                "fuel": "imports",
                                "perc": 8.9
                            },
                            {
                                "fuel": "gas",
                                "perc": 35.4
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 13.4
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 1.5
                            },
                            {
                                "fuel": "solar",
                                "perc": 9.7
                            },
                            {
                                "fuel": "wind",
                                "perc": 18.5
                            }
                        ]
                    },
                    {
                        "regionid": 16,
                        "dnoregion": "Scotland",
                        "shortname": "Scotland",
                        "intensity": {
                            "forecast": 63,
                            "index": "low"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 1.6
                            },
                            {
                                "fuel": "coal",
                                "perc": 0
                            },
                            {
                                "fuel": "imports",
                                "perc": 0
                            },
                            {
                                "fuel": "gas",
                                "perc": 15.7
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 23
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 21.5
                            },
                            {
                                "fuel": "solar",
                                "perc": 1.4
                            },
                            {
                                "fuel": "wind",
                                "perc": 36.8
                            }
                        ]
                    },
                    {
                        "regionid": 17,
                        "dnoregion": "Wales",
                        "shortname": "Wales",
                        "intensity": {
                            "forecast": 249,
                            "index": "moderate"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 0
                            },
                            {
                                "fuel": "coal",
                                "perc": 0
                            },
                            {
                                "fuel": "imports",
                                "perc": 0
                            },
                            {
                                "fuel": "gas",
                                "perc": 63.1
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 0
                            },
                            {
                                "fuel": "other",
                                "perc": 0
                            },
                            {
                                "fuel": "hydro",
                                "perc": 3.6
                            },
                            {
                                "fuel": "solar",
                                "perc": 6.5
                            },
                            {
                                "fuel": "wind",
                                "perc": 26.8
                            }
                        ]
                    },
                    {
                        "regionid": 18,
                        "dnoregion": "GB",
                        "shortname": "GB",
                        "intensity": {
                            "forecast": 201,
                            "index": "moderate"
                        },
                        "generationmix": [
                            {
                                "fuel": "biomass",
                                "perc": 7.8
                            },
                            {
                                "fuel": "coal",
                                "perc": 4
                            },
                            {
                                "fuel": "imports",
                                "perc": 8.1
                            },
                            {
                                "fuel": "gas",
                                "perc": 36
                            },
                            {
                                "fuel": "nuclear",
                                "perc": 13.7
                            },
                            {
                                "fuel": "other",
                                "perc": 0.4
                            },
                            {
                                "fuel": "hydro",
                                "perc": 2.9
                            },
                            {
                                "fuel": "solar",
                                "perc": 9.1
                            },
                            {
                                "fuel": "wind",
                                "perc": 18
                            }
                        ]
                    }
                ]
            }
        ]
    }
}

for key, value in sorted(mydict.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))






# import requests
#
# def test():
#     ploads = {'things':2,'total':25}
#     r = requests.get('https://httpbin.org/get',params=ploads)
#     print(r.text)
#     print(r.content)
