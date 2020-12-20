import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('Nzg5ODg2MjI5MTY3ODY1ODc3.X94k4A.4JVtDI8-mKftvNGdwtN_tjPKEIE')
