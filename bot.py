import discord
from discord.ext import commands
import config
import pickle
import time

students = config.students
present = []
missing = []
client = commands.Bot(command_prefix=config.prefix)
homework = pickle.load(open(config.way, 'rb'))


# Homework
@client.command(name='homework')
async def answer(ctx):
    global homework
    text = ''
    homework = pickle.load(open(config.way, 'rb'))
    for x in range(0, len(homework)):
        text = text + str(x + 1) + '       ' + 'Дз№' + str(x + 1) + '\n'
    text = text + 'To choose which homework to print, write "/print_homework homework_number" '
    embed = discord.Embed(color=config.color)
    embed.add_field(name='№', value=text, inline=False)
    await ctx.send(embed=embed)


# Print Homework
@client.command(name='print_homework')
async def answer(ctx, context1):
    global homework
    text = ''
    homework = pickle.load(open(config.way, 'rb'))
    d = list(homework[int(context1) - 1])
    text = text + '№' + '\n'
    for x in range(0, len(homework[int(context1) - 1])):
        text = text + str(x + 1) + '                   ' + d[x] + '\n'
    text = text + 'To print the exercise, write "/print_exercise homework_number exercise_number" '
    embed = discord.Embed(color=config.color)
    embed.add_field(name='Homework№' + context1, value=text, inline=False)
    await ctx.send(embed=embed)


# Print Exercise
@client.command(name='print_exercise')
async def answer(ctx, context1, context2):
    global homework
    homework = pickle.load(open(config.way, 'rb'))
    await ctx.send('Homework№' + context1 + '  exercise ' + context2)
    await ctx.send(homework[int(context1) - 1][context2])


# Create Homework
@client.command(name='create_homework')
@commands.has_role(config.edit_role)
async def answer(ctx):
    global homework
    homework = pickle.load(open(config.way, 'rb'))
    if len(homework) > 19:
        text = 'Coder Bogdasha did not provide such a number of homework, please contact technical support'
        embed = discord.Embed(color=config.color)
        embed.add_field(name='Error', value=text, inline=False)
        await ctx.send(embed=embed)
    else:
        if len(homework) == 0:
            dz1 = {}
            homework.append(dz1)
        elif len(homework) == 1:
            dz2 = {}
            homework.append(dz2)
        elif len(homework) == 2:
            dz3 = {}
            homework.append(dz3)
        elif len(homework) == 3:
            dz4 = {}
            homework.append(dz4)
        elif len(homework) == 4:
            dz5 = {}
            homework.append(dz5)
        elif len(homework) == 5:
            dz5 = {}
            homework.append(dz5)
        elif len(homework) == 6:
            dz7 = {}
            homework.append(dz7)
        elif len(homework) == 7:
            dz8 = {}
            homework.append(dz8)
        elif len(homework) == 8:
            dz8 = {}
            homework.append(dz8)
        elif len(homework) == 9:
            dz10 = {}
            homework.append(dz10)
        elif len(homework) == 10:
            dz11 = {}
            homework.append(dz11)
        elif len(homework) == 11:
            dz12 = {}
            homework.append(dz12)
        elif len(homework) == 12:
            dz13 = {}
            homework.append(dz13)
        elif len(homework) == 14:
            dz15 = {}
            homework.append(dz15)
        elif len(homework) == 15:
            dz16 = {}
            homework.append(dz16)
        elif len(homework) == 16:
            dz17 = {}
            homework.append(dz17)
        elif len(homework) == 17:
            dz18 = {}
            homework.append(dz18)
        elif len(homework) == 18:
            dz19 = {}
            homework.append(dz19)
        elif len(homework) == 19:
            dz20 = {}
            homework.append(dz20)
        pickle.dump(homework, open(config.way, 'wb'))
        embed = discord.Embed(color=config.color)
        embed.add_field(name='Successfully', value='Homework№' + str(len(homework)) + ' created', inline=False)
        await ctx.send(embed=embed)


# Edit Homework
@client.command(name='edit_homework')
@commands.has_role(config.edit_role)
async def answer(ctx, context1, context2, context3):
    global homework
    homework = pickle.load(open(config.way, 'rb'))
    homework[int(context1)-1][context2] = context3
    pickle.dump(homework, open(config.way, 'wb'))
    embed = discord.Embed(color=config.color)
    embed.add_field(name='Successfully', value='', inline=False)
    await ctx.send(embed=embed)


# Roll Call
@client.command(name='rollcall')
async def answer(ctx, argument1, argument2):
    global present
    isis = False
    good = False
    text = str(argument1) + ' ' + str(argument2)
    for x in range(0, len(present)):
        if text == present[x]:
            embed = discord.Embed(color=config.color)
            embed.add_field(name='Error', value='%s have already been marked' % present[x], inline=False)
            await ctx.send(embed=embed)
            isis = True
    for y in range(0, len(students)):
        if text == students[y]:
            good = True
    if not good:
        embed = discord.Embed(color=config.color)
        embed.add_field(name='Error', value="Invalid name or surname", inline=False)
        await ctx.send(embed=embed)
    if not isis and good:
        present.append(text)


# Present
@client.command(name='present')
async def answer(ctx):
    global present
    global missing
    global students
    message = ''
    text = ''
    text1 = ''
    embed = discord.Embed(color=config.color)
    # Present
    message = message + 'Present at the lesson:' + '\n'
    if present:
        for x in range(0, len(present)):
            text = text + str(x+1) + '   ' + present[x] + '\n'
        message = message + text + '\n'
    # Absent
    if present == students:
        missing = []
    elif not present:
        missing = students
    else:
        for z in range(0, len(students)):
            presented = False
            for y in range(0, len(present)):
                if students[z] == present[y]:
                    presented = True
            if not presented:
                missing.append(students[z])
    message = message + 'Absent from lesson:' + '\n'

    for s in range(0, len(missing)):
        text1 = text1 + str(s + 1) + '   ' + missing[s] + '\n'
    message = message + text1
    embed.add_field(name="Roll Call" + ' ' + time.asctime(), value=message, inline=False)
    await ctx.send(embed=embed)
    present = []
    missing = []


# Discord Activity
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=config.bot_activity))

client.run(config.TOKEN)
