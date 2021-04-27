from yaml import dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
import datetime

if datetime.datetime.now().weekday() < 5:
  weekday = True
else:
  weekday = False


data = {
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
                                                  "command": "echo \"Config via APi works!\""
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
  data["jobs"]["weekday_job"] = { "docker": [
                                        {
                                          "image": "ubuntu:14.04"
                                        }
                                      ],
                                  "steps": [
                                            "checkout",
                                            {
                                              "run": {
                                                  "command": "echo \"This is the weekday job!\""
                                                }
                                            }
                                            ]
                                }

  data["workflows"]["build-server"]["jobs"].append({"weekday_job":{"requires":["build"]}})
print(dump(data, Dumper=Dumper))
