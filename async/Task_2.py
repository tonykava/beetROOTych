import asyncio
from psaw import PushshiftAPI
import pandas as pd
import json

async def func(subreddit, link):
    file_name = 'data.json'

    api = PushshiftAPI()

    gen = api.search_comments(subreddit=subreddit, link_id=link)

    cache = []

    for i in gen:
        cache.append(i)


    df = pd.DataFrame([i.d_ for i in cache])
    df_comments = df[['created', 'body']]
    df_time_cleaned = df_comments.copy()
    df_time_cleaned['created'] = pd.to_datetime(df_time_cleaned['created'], unit = 's', utc=True).dt.tz_convert('Europe/Kyiv')
    df_time_cleaned = df_time_cleaned.sort_values(by='created', ascending=True)
    df_final = df_time_cleaned

    print(df_final)

    df_final = df_final.to_json(orient='records', date_format='iso')

    with open('data.json', 'a') as f:
        json.dump(df_final, f)
        json.dump('------------------------------------------------------------------------------', f)

async def main():
    task1 = asyncio.create_task(func('ModernWarfareII', 'yqqbn8'))
    task2 = asyncio.create_task(func('Games', 'xfuh2a'))



asyncio.run(main())
