import json
import discord
from discord.ext import commands 
from misc import time_getter as time, news_getter as news, weather_getter as weather, color_getter as color, meme_getter as meme, shower_getter as shower, date_getter as date

bot = commands.Bot(command_prefix='.', intents = discord.Intents.all() , help_command = None)

def member_list():
    guild = bot.get_guild(857595321559416852)
    users = guild.members
    ids = []

    for user in users:
        if user.id != 877967717087461406:
            ids.append(user.id)

    with open("users.json", "r") as f:
        data = json.load(f)
    data['users'] = ids
    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)

@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name)
    print('Ready!\n')
    await time_notif()

async def time_notif():
  while True:
    member_list()

    h, m = time()
    if h == 1 and m > -1 and m < 1:
      with open("users.json", "r") as f:
        data = json.load(f)
      data['sent'] = False
      with open("users.json", "w") as f:
        json.dump(data, f)

    if h == 16 and m > 53 and m < 55:
      await send()


async def embed_maker():
    desc, temp, feel, min, max, humid, image_url = weather()
    weather_embed = discord.Embed(title="Weather", color = 0x82d1f1)
    weather_embed.add_field(name="Temperature", value=temp, inline=True)
    weather_embed.add_field(name="Feels Like", value=feel, inline=True)
    weather_embed.add_field(name="Humidity", value=humid, inline=True)

    weather_embed.add_field(name="Description", value=desc, inline=True)
    weather_embed.add_field(name="Minimum", value=min, inline=True)
    weather_embed.add_field(name="Maximum", value=max, inline=True)

    weather_embed.set_thumbnail(url = image_url)
    weather_embed.set_footer(text="weather")


    title, description, url, image_url = news()
    news_embed = discord.Embed(title="News", color = 0xd0db61)
    news_embed.add_field(name=title, value=f"""{description}

    Read the article here: {url}
    """, inline=False)

    news_embed.set_thumbnail(url = image_url)
    news_embed.set_footer(text="news")


    hex = color()
    color_embed = discord.Embed(title="Random Color", color = 0xffffff)
    color_embed.add_field(name="Hex Code", value=f"#{hex}", inline=False)

    color_embed.set_image(url = f"https://www.colorbook.io/imagecreator.php?hex={hex}&width=100&height=100")
    color_embed.set_footer(text="color")


    post, image_url, title = meme()
    meme_embed = discord.Embed(title=title, color = 0xffb448)

    meme_embed.set_image(url = image_url)
    meme_embed.set_footer(text=f"meme | {post}")


    post, title = shower()
    shower_embed = discord.Embed(title=title, color = 0x9b111e)

    shower_embed.set_footer(text=f"shower thoughts | {post}")

    return weather_embed, news_embed, color_embed, meme_embed, shower_embed

TOKEN = "LMAO"

@bot.command()
async def send():
    weather_embed, news_embed, color_embed, meme_embed, shower_embed = await embed_maker()

    with open("users.json", "r") as f:
        data = json.load(f)
    users = data['users']
  
    if data['sent'] == False:
        for user in users:
            print(user)
            discord_user = bot.get_user(user)
            try:
                await discord_user.send(embed=weather_embed)
            except:
                pass
            
            try:
                await discord_user.send(embed=news_embed)
            except:
                pass
            
            try:
                await discord_user.send(embed=meme_embed)
            except:
                pass

            try:
                await discord_user.send(embed=shower_embed)
            except:
                pass

            try:
                await discord_user.send(embed=color_embed)
            except:
                pass
    
    channel = bot.get_channel(936450391053307905)
    d,m,y = date()
    send = ""
    for user in users:
        user = bot.get_user(user)
        user = f"{user.name}#{user.discriminator}"
        send = f"""{user}
{send}
"""
    embed = discord.Embed(title=f"Log for {d}-{m}-{y}", description=f"user count: {len(users)}\n\nusers:\n\n{send}")
    await channel.send(embed=embed)
      
    with open("users.json", "r") as f:
        data = json.load(f)
        data['sent'] = True
    with open("users.json", "w") as f:
        json.dump(data, f)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run(TOKEN)