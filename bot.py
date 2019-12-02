import discord
from discord.ext import commands
import random
import os

client = commands.Bot(command_prefix='?')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Game('?help for commands.'))


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')


@client.event
async def member_removed(member):
    print(f'{member} has left the server. :cry:')


@client.command(brief='Ping-->Pong!', description='My hello world alternative.')
async def ping(ctx):
    await ctx.send('pong')


@client.command(brief='Ask an 8ball a Yes/No question.',
                description='Can also use ?8ball or ?8 for shorthand.',
                aliases=['8ball', '8'])
async def ask8ball(ctx, *, question):
    answers = ['Ask me again, see what happens.',
               'Ok fine, but you\'re gonna regret it.',
               'Nah.',
               'Sounds like an awful idea.',
               'Carpe diem',
               'I honestly don\'t care.',
               'If you don\'t do it, I\'ll be hella disappointed.',
               'Do it.',
               'I press X to doubt.']
    if question is None:
        await ctx.send(f'Please enter in the following format:\n?8ball <insert question here>')
    else:
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(answers)}')


@client.command(brief='Crack open a fortune cookie.',
                description='Can also use ?cookie or ?fc for shorthand.',
                aliases=['fc', 'cookie'])
async def fortune(ctx):
    fortunes = ['Your near future is too murky to decipher',
                'Do not mistake temptation for opportunity.',
                'Investing in Bitcoin after 2017 was a mistake.',
                'A foolish man listens to his heart. A wise man listens to cookies.',
                'Never forget a friend. Especially if he owes you something.',
                'You crave food right now.',
                'You can read. Take advantage of that.',
                '']
    await ctx.send(f'Fortune Cookie: {random.choice(fortunes)}')


@client.command(brief='Chooses from provided choices at random.',
                description='Provide a list of choices. Separate choices with a space.')
async def pick(ctx, *, s):
    choices = s.split()
    await ctx.send(f'Choices: {choices}\nChosen One: {random.choice(choices)}')


@client.command(brief='PA Powerball Lottery Number Generator.', aliases=['lotto1', 'pball', 'pb'])
async def powerball(ctx):
    await ctx.send('1')


@client.command(brief='PA Mega Millions Lottery Number Generator.', aliases=['lotto2', 'mega', 'mm'])
async def megaMillions(ctx):
    await ctx.send('2')


@client.command(brief='Higher/Lower Number Guessing Game.', aliases=['higherOrLower', 'higher', 'lower'])
async def numGuess(ctx, *, num1, num2):
    gameInProgress = True
    number = random.choice(range(num1, num2))
    """
    Start game. Let bot message the user saying the game has started.
    Then, the user should guess numbers between the inputted range (inclusive).
    After this, the bot will continue to message the user with a response saying
    'higher', 'lower', or 'invalid input' if the user gives a non-numeric input.
    """
    await ctx.send(number)

client.run(os.getenv('DISCORD_BOT_TOKEN'))
