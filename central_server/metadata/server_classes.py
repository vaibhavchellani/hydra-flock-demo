classes_ = [
        # 1. Drone Class
        {
            "@id": "http://hydrus.com/drone",
            "@type": "hydra:Class",
            "title": "drone",
            "description": "Contains specifications related to drones.",
            "supportedOperation": [
                {
                    "statusCodes": [
                        {
                            "code": 200,
                            "description": "Drone successfully created"
                        }
                    ],
                    "@type": "http://schema.org/AddAction",
                    "returns": "http://hydrus.com/drone",
                    "label": "Create a new drone entity in the database.",
                    "method": "POST",
                    "@id": "_:drone_create",
                    "description": None,
                    "expects": "http://hydrus.com/drone"
                },
                {
                    "statusCodes": [],
                    "@type": "hydra:Operation",
                    "returns": "http://hydrus.com/drone",
                    "label": "Retrieves all drone details.",
                    "method": "GET",
                    "@id": "_:drone_retrieve",
                    "description": None,
                    "expects": None
                }
            ],
            "supportedProperty": [
                {"@type": "SupportedProperty",
                 "property": "http://schema.org/identifier",
                 "title": "Identifier",
                 "hydra:description": "Id with which the drone is stored at the central server ( Initially None).",
                 "required": True,
                 "readonly": False,
                 "writeonly": False
                 },

                {
                    "@type": "SupportedProperty",
                    "property": "http://auto.schema.org/speed",
                    "hydra:description":"Current speed of the drone",
                    "readable": True,
                    "required": True,
                    "title": "Speed",
                    "writeable": True
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readable": True,
                    "required": True,
                    "hydra:description":"Current coordinates of the drone",
                    "title": "Position",
                    "writeable": True
                },
                {"@type": "SupportedProperty",
                 "property": "http://schema.org/geo",
                 "title": "Destination",
                 "hydra:description": "Coordinates of the new destination",
                 "required": True,
                 "readonly": False,
                 "writeonly": False
                 },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/fuelCapacity",
                    "readable": True,
                    "required": True,
                    "hydra:description": "Battery status of the drone.",
                    "title": "Battery",
                    "writeable": True
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/device",
                    "readable": True,
                    "required": True,
                    "title": "Sensor",
                    "hydra:description": "Sensors available in the drone.",
                    "writeable": False
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/name",
                    "readable": True,
                    "required": True,
                    "title": "Name",
                    "hydra:description":"Name of the drone ( will be used as the network alias)",
                    "writeable": False
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/status",
                    "readable": True,
                    "required": True,
                    "title": "Status",
                    "hydra:description":"Current status of the drone.",
                    "writeable": True
                }
            ]
        },

    # 2. Logs Class
    {
        "@id": "http://hydrus.com/logs",
        "@type": "hydra:Class",
        "title": "logs",
        "description": "Handle logs from the central server.",
        "supportedOperation": [
               {
                   "statusCodes": [
                       {
                           "code": 404,
                           "description": "If no logs were found."
                       }
                   ],
                   "@type": "hydra:Operation",
                   "returns": "http://hydrus.com/logs",
                   "label": "Retrieves all logs from the central server.",
                   "method": "GET",
                   "@id": "_:logs_retrieve",
                   "description": None,
                   "expects": None
               }
        ],
        "supportedProperty": [
            # Not finalized yet!
        ]
    },

    # 3. Message Class
    {
        "@id": "http://hydrus.com/message",
        "@type": "hydra:Class",
        "title": "message",
        "description": "Commands in NLP format issued by the user.",
        "supportedOperation": [
                 {
                     "statusCodes": [
                         {
                             "code": 200,
                             "description": "message successfully submitted."
                         }
                     ],
                     "@type": "http://schema.org/AddAction",
                     "returns": "http://hydrus.com/message",
                     "label": "Recieve command in NLP format from the GUI client.",
                     "method": "POST",
                     "@id": "_:message_create",
                     "description": None,
                     "expects": "http://hydrus.com/message"
                 },
            {
                     "statusCodes": [
                         {
                             "code": 404,
                             "description": "If no messages were found."
                         }
                     ],
                     "@type": "hydra:Operation",
                     "returns": "http://hydrus.com/message",
                                "label": "Retrieves all messages submitted to the central server.",
                                "method": "GET",
                                "@id": "_:message_retrieve",
                                "description": None,
                                "expects": None
                 }
        ],
        "supportedProperty": [

            {"@type": "SupportedProperty",
             "property": "http://schema.org/message",
             "title": "message",
             "hydra:description": "Message in NLP format submitted from GUI client.",
             "required": True,
             "readonly": False,
             "writeonly": False
             },
        ]
    },

    # 4. Order Class
    {
        "@id": "http://schema.org/order",
               "@type": "hydra:Class",
               "title": "order",
               "description": "Handle orders from the central server.",
               "supportedOperation": [
                   {
                       "statusCodes": [
                           {
                              "code": 200,
                              "description": "order successfully recieved."
                           }
                       ],
                       "@type": "http://schema.org/AddAction",
                       "returns": "http://schema.org/order",
                       "label": "Create orders.",
                       "method": "POST",
                       "@id": "_:order_create",
                       "description": None,
                       "expects": "http://schema.org/order"
                   },
                   {
                       "statusCodes": [
                           {
                               "code": 404,
                               "description": "If no orders were found."
                           }
                       ],
                       "@type": "hydra:Operation",
                       "returns": "http://schema.org/order",
                                  "label": "Retrieves all orders from the central server.",
                                  "method": "GET",
                                  "@id": "_:order_retrieve",
                                  "description": None,
                                  "expects": None
                   }
               ],
        "supportedProperty": [

                   {"@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "title": "Destination",
                    "hydra:description": "Coordinates of the new destination",
                    "required": True,
                    "readonly": False,
                    "writeonly": False
                    },
                   {"@type": "SupportedProperty",
                       "property": "http://auto.schema.org/speed",
                    "title": "Speed",
                    "hydra:description": "Speed of drone in Km/h",
                    "required": True,
                    "readonly": False,
                    "writeonly": False
                    },

                   {"@type": "SupportedProperty",
                       "property": "http://schema.org/identifier",
                    "title": "Identifier",
                    "hydra:description": "Identifier for drone to check if the recieved order was for the same drone.",
                    "required": True,
                    "readonly": False,
                    "writeonly": False
                    },
               ]
    },

    # 5. Status Class
    {
        "@id": "http://hydrus.com/status",
        "@type": "hydra:Class",
        "title": "status",
        "description": "Handle status requests from different drones.",
        "supportedOperation": [
            {
                "statusCodes": [
                    {
                        "code": 200,
                        "description": "Status successfully submitted."
                    }
                ],
                "@type": "http://schema.org/AddAction",
                "returns": "http://hydrus.com/status",
                "label": "Recieves status updates from different drones.",
                "method": "POST",
                "@id": "_:status_create",
                "description": None,
                "expects": "http://hydrus.com/status"
            },
            {
                "statusCodes": [
                    {
                        "code": 404,
                        "description": "If no status objects were found."
                    }
                ],
                "@type": "hydra:Operation",
                "returns": "http://hydrus.com/status",
                "label": "Retrieves all status objects submitted by differnt drones.",
                "method": "GET",
                "@id": "_:status_retrieve",
                "description": None,
                "expects": None
            }
        ],
        "supportedProperty": [
            {"@type": "SupportedProperty",
             "property": "http://schema.org/identifier",
             "title": "Identifier",
             "hydra:description": "Identifier for server to check if the drone is associated with the server.",
             "required": True,
             "readonly": False,
             "writeonly": False
             },

            {"@type": "SupportedProperty",
             "property": "http://schema.org/geo",
             "title": "Destination",
             "hydra:description": "Coordinates of the new destination",
             "required": True,
             "readonly": False,
             "writeonly": False
             },
            {"@type": "SupportedProperty",
             "property": "http://auto.schema.org/speed",
             "title": "Speed",
             "hydra:description": "Speed of Drone in Km/h",
             "required": True,
             "readonly": False,
             "writeonly": False
             },
            {
                "@type": "SupportedProperty",
                "property": "http://schema.org/geo",
                "readable": True,
                "required": True,
                "title": "Position",
                "writeable": True
            },
            {
                "@type": "SupportedProperty",
                "property": "http://schema.org/fuelCapacity",
                "readable": True,
                "required": True,
                "title": "Battery",
                "writeable": True
            },
            {
                "@type": "SupportedProperty",
                "property": "http://schema.org/OrderStatus",
                "readable": True,
                "required": True,
                "title": "Progress",
                "hydra:description": "Current status of the drone can be [ Charging| Moving| Reached Destination| Analysing ]",
                "writeable": True
            },



        ]
    },
    #   6. Datastream Class
    {
        "@id": "http://hydrus.com/datastream",
        "@type": "hydra:Class",
        "title": "datastream",
        "description": "Handle sensor datastreams submitted by different drones.",
        "supportedOperation": [
            {
                "statusCodes": [
                    {
                        "code": 200,
                        "description": "Datastream successfully recieved."
                    }
                ],
                "@type": "http://schema.org/AddAction",
                "returns": "http://hydrus.com/datastream",
                "label": "Recieves datastreams from differnet drones.",
                "method": "POST",
                "@id": "_:datastream_create",
                "description": None,
                "expects": "http://hydrus.com/datastream"
            },
            {
                "statusCodes": [
                    {
                        "code": 404,
                        "description": "No datastream objects were found."
                    }
                ],
                "@type": "hydra:Operation",
                "returns": "http://hydrus.com/datastream",
                "label": "Retrieves all datastream objects from the central server.",
                "method": "GET",
                "@id": "_:datastream_retrieve",
                "description": None,
                "expects": None
            }
        ],
        "supportedProperty": [

            {"@type": "SupportedProperty",
             "property": "http://schema.org/geo",
             "title": "Position",
             "hydra:description": "Coordinates of the current location",
             "required": True,
             "readonly": False,
             "writeonly": False
             },
            {"@type": "SupportedProperty",
             "property": "http://schema.org/QuantitativeValue",
             "title": "Temperature",
             "hydra:description": "Temperature of area can be [ Normal | Abnormal | Critical]",
             "required": True,
             "readonly": False,
             "writeonly": False
             },

            {"@type": "SupportedProperty",
             "property": "http://schema.org/identifier",
             "title": "Identifier",
             "hydra:description": "Identifier for drone to check if the recieved datastream was for the same drone.",
             "required": True,
             "readonly": False,
             "writeonly": False
             },
        ]
    },

]

## Classes that need to be a collection
collection_classes = ["drone", "logs", "message","order", "status", "datastream"]

## Classes that need to be shown at Entrypoint
entrypoint_classes = ["drone", "logs", "message", "order", "status", "datastream"]