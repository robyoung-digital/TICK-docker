import statsd
import time
import random

client = statsd.StatsClient('telegraf', 8125)

# create some data
services = [
    'agent_service',
    'complex_service',
]

routes = [
    'POST/api/v1/agent/link_test',
    'GET/api/v1/agent/link_test',
    'POST/api/v1/agent/register',
    'POST/api/v1/agent/sync',
]

for _ in range(1000):
    service_name = random.choice(services)
    route_name = random.choice(routes)
    timing = random.randint(1, 2000)

    metric = f'ts.{service_name}.routes.{route_name}.time'

    print(f'{metric} {timing}')
    client.timing(metric, timing)
    time.sleep(0.2)
