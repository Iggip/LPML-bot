import discord
from discord.ext import commands
import config
import time

students = ['Бойко Роман', 'Бойко Юрій', 'Гарбуз Кирило', 'Голець Роман', 'Гринюк Христина', 'Губаль Софія', 'Гурняк '
                                                                                                             'Захар',
            'Гурняк Станіслав', 'Гупало Богдан', "Діус В'ячеслав", 'Козак Наталія', 'Коновалов Лука', 'Коренівський '
                                                                                                      'Анатолій',
            'Костюк Остап', 'Кундис Вадим', 'Кшик Олена', 'Левчук Артем', 'Лукачина Юрій', 'Мандзій Юрій',
            'Марущак Данило', 'Прокопець Максим', 'Середницький Богдан', 'Скрипник Роман', 'Слюсаренко Анна',
            'Стасюк Зоя', 'Сторонянський Маркіян', 'Троян Юрій', 'Фаренюк Максим', 'Шевченко Таїсія', 'Яремчишин '
                                                                                                      'Данило',
            'Ярошенко Владислава']
present = []
missing = []
client = commands.Bot(command_prefix='/')


@client.command(name='rollcall')
async def answer(ctx, argument1, argument2):
    global present
    isis = False
    good = False
    text = str(argument1) + ' ' + str(argument2)
    for x in range(0, len(present)):
        if text == present[x]:
            embed = discord.Embed(color=0xff8080)
            embed.add_field(name='Помилка', value='%s вже відмічений' % present[x], inline=False)
            await ctx.send(embed=embed)
            isis = True
    for y in range(0, len(students)):
        if text == students[y]:
            good = True
    if not good:
        embed = discord.Embed(color=0xff8080)
        embed.add_field(name='Помилка', value="Невірне ім'я або прізвище", inline=False)
        await ctx.send(embed=embed)
    if not isis and good:
        present.append(text)


@client.command(name='present')
async def answer(ctx):
    global present
    global missing
    global students
    message = ''
    text = ''
    text1 = ''
    embed = discord.Embed(color=0xff8080)
    # Присутні
    message = message + 'Присутні на уроці:' + '\n'
    if present:
        for x in range(0, len(present)):
            text = text + str(x+1) + '   ' + present[x] + '\n'
        message = message + text + '\n'
    # Відсутні
    if present == students:
        missing = []
    elif present == []:
        missing = students
    else:
        for z in range(0, len(students)):
            presented = False
            for y in range(0, len(present)):
                if students[z] == present[y]:
                    presented = True
            if not presented:
                missing.append(students[z])
    message = message + 'Відсутні на уроці:' + '\n'

    for s in range(0, len(missing)):
        text1 = text1 + str(s + 1) + '   ' + missing[s] + '\n'
    message = message + text1
    embed.add_field(name="Перекличка"+' '+time.asctime(), value=message, inline=False)
    await ctx.send(embed=embed)
    present = []
    missing = []


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="тиск SAS-а"))


client.run(config.TOKEN)
