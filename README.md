# kismet_parser
Some Random Scripts to Parse Kismet output for useful info

## Overview 
Kismet (at least 2017 and newer) store the logs in a sqlite db and ship with some utilities to parse them.
The Scripts in here are for dealing with the json version of these files.
In order to generate the json format from your .kismet files, you need to use the kismetdb_dump_devices.

An example is:
> kismetdb_dump_device --in Kismet-12345.kismet --out my_output.json -s

* The --in should point to the relevant kismet db file in question.
* The --out is whatever you want to name the output .json file
* The -s tells the command to not try to vacuum the database first. 
    This is optional, but if the service is running, you'll have to use this or it will fail.
    
## Nitty Gritty

Okay so we got that covered, now we can actually use this stuff.

### Hidden Networks

Sometimes you need to find hidden networks, what channel they're on, etc. 
There's a purpose-built script for that called kismet_hidden.py.
* Note: The first argument is your json file
> kismet_hidden.py my_output.json



### All Devices, SSIDs, Channels

As an attacker, we usually need some basic information. Those tend to be:
* Channel
* BSSID
* Type (Client, AP, etc.)
* ESSID
There's a purpose built script to quickly grab this out for you too.

> kismet_all_basic.py my_output.json

Where my_output.json is your json file generated using the first steps. 
Each field is separated with tabs (\t) so you can awk it out as needed.







### Some Notes
These were written in real time as I needed them so please excuse messy code.
I'll try to iron them out to be prettier or combine into a single script.
