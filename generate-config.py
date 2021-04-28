#!/usr/bin/env python3

import datetime
from yaml import dump

weekday = datetime.datetime.now().weekday() < 5

config = {
    "version": 2.1,
    "jobs": {
        "build": {
            "docker": [
                {
                    "image": "ubuntu:14.04"
                }
            ],
            "steps": [
                "checkout",
                {
                    "run": {
                        "command": 'echo "Config API works!"'
                    }
                }
            ]
        }
    },
    "workflows": {
        "build-server": {
            "jobs": [
                "build"
            ]
        }
    }
}

if weekday:
    config["jobs"]["weekday_job"] = {
        "docker": [
            {
                "image": "ubuntu:14.04"
            }
        ],
        "steps": [
            "checkout",
            {
                "run": {
                    "command": 'echo "This is the weekday job!"'
                }
            }
        ]
    }

    config["workflows"]["build-server"]["jobs"].append(
        {"weekday_job": {"requires": ["build"]}}
    )

print(dump(config))
