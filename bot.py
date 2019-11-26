import discord
from discord.ext import commands
import random
import os

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


@client.command(brief='Ping-->Pong!', description='Kinda like a hello world')
async def ping(ctx):
    await ctx.send('pong')


@client.command(brief='Ask an 8ball a Yes/No question.',
                description='Can also use ?8ball or ?8 for shorthand.',
                aliases=['8ball', '8'])
async def ask8ball(ctx, *, question):
    answers = ['Ask me again, see what happens.',
               'Ok fine, but you\'re gonna regret it.',
               'You won\'t.',
               'Sounds like an awful idea',
               'Carpe diem',
               'I honestly don\'t care.',
               'If you don\'t do it, I\'ll be hella disappointed.',
               'Do it.',
               'X, because I am full of doubt.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(answers)}')


client.run(os.getenv('DISCORD_BOT_TOKEN'))
