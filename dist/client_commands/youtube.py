import pytube
from random import choice, randint
from string import ascii_letters
from colored import fg, attr
from string import ascii_lowercase

def SearchVideo(__search__: str=None):
    
    if __search__ is None:
        __search__ = str()
        for i in range(randint(0, 10)):
            __search__ += choice(ascii_letters)
    
    s = pytube.Search(__search__).results[0]
    video_url = 'https://www.youtube.com/watch?v=%s' % (str(s)[int(str(s).find('=')+1):][:-1])
    return video_url

async def Youtube(ctx, search_):

    if not search_: 
        video_url = SearchVideo()
    else:
        
        __search__ = str()
        for w in search_:
            __search__ += w + ' '
        
        video_url = SearchVideo(__search__)
        
    await ctx.reply(video_url)
