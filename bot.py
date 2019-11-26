import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='?')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')


@client.event
async def member_removed(member):
    print(f'{member} has left the server. :cry:')


@client.command()
async def ping(ctx):
    await ctx.send('pong')


@client.command(aliases=['8ball', '8'])
async def ask8ball(ctx, *, question):
    answers = ['Ask me again, see what happens.',
               'Ok fine, but you\'re gonna regret it.',
               'You won\'t.',
               'Sounds like an awful idea',
               'Carpe diem',
               'I honestly don\'t care.',
               'If you don\'t do it, I\'ll be hella disappointed.']
    await ctx.send(f'Question: {question}\n Answer: {random.choice(answers)}')


client.run('NjQ4NjE1MjQ2MTUxNDE3ODU2.XdxZ8Q.tLP7w1U-jwZsh01Q7KT1igSKOsM')
