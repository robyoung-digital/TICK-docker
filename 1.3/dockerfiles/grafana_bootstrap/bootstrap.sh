#!/bin/bash

sleep 15

http -I -a "admin:admin" POST http://grafana:3000/api/datasources type=influxdb name=influx url=http://influxdb:8086 access=direct database=telegraf 
