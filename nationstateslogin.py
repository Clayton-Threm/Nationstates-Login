import nationstates
import time
import os

PASSWORD = os.environ.get('API_PASSWORD')
PASSWORD2 = os.environ.get('API_PASSWORD2')

days = 0.49
api = nationstates.Nationstates('Nation Login Script')
nation = api.nation("Oustrie", password=PASSWORD)
nation2 = api.nation('Letterspasta', password=PASSWORD2)
while True:
    nation.get_shards("ping")
    nation2.get_shards("ping")
    time.sleep(days*24*60)