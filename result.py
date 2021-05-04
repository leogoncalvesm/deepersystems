import json
import pandas as pd

df = pd.read_json('source_file_2.json').explode('managers').explode('watchers').sort_values('priority')
managers = dict(df.drop_duplicates(['managers', 'name']).groupby('managers')['name'].apply(list))
watchers = dict(df.drop_duplicates(['watchers', 'name']).groupby('managers')['name'].apply(list))

with open('managers.json', 'w') as f: json.dump(managers, f)
with open('watchers.json', 'w') as f: json.dump(watchers, f)
