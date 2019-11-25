import discord
from discord.ext import commands
import random

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')


@client.event
async def member_removed(member):
    print(f'{member} has left the server. :(')

client.run('NjQ4NjE1MjQ2MTUxNDE3ODU2.Xdw1YQ.EB1j9wH2bC95xMuNnvErunsxhBE')
