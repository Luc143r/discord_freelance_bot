import discord
from discord.ext import commands
from discord.utils import get
from discord.guild import Guild
from discord import DMChannel
import json
import asyncio
import os.path
from os import remove
from time import sleep

from config import settings, settings_db
from mongo import get_id, get_points


class Button(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='Check points', style=discord.ButtonStyle.blurple)
    async def check_points(self, interaction: discord.Interaction, button: discord.ui.Button):
        list_roles = ('0 - Heir', '1 - Capitan', '2 - Despot', '3 - Legate',
                      '4 - Tonarch', '5 - Strategos', '6 - Praetor', '7 - Prince')
        try:
            count_points = get_points(get_id(str(interaction.user)))
            embed = discord.Embed(
                color=000, title=f'Your point bellow', description=f'You have {count_points} points.')
            embed.set_footer(
                text='Prod by Luc143r || 🖤 || @insearchofmyself666')
            embed.set_image(
                url='https://i.pinimg.com/originals/2d/ec/5a/2dec5a7d09a41d02b606c6aa4803ee4b.jpg')
            await interaction.response.send_message(embed=embed, ephemeral=True)
            user = interaction.user
            if count_points < 10:
                for i in range(len(list_roles)):
                    role = discord.utils.get(
                        user.guild.roles, name=list_roles[i])
                    await user.remove_roles(role)
                role = discord.utils.get(user.guild.roles, name=list_roles[0])
                await user.add_roles(role)
            elif count_points >= 10 and count_points < 100:
                for i in range(len(list_roles)):
                    role = discord.utils.get(
                        user.guild.roles, name=list_roles[i])
                    await user.remove_roles(role)
                role = discord.utils.get(user.guild.roles, name=list_roles[1])
                await user.add_roles(role)
            elif count_points >= 100 and count_points < 300:
                for i in range(len(list_roles)):
                    role = discord.utils.get(
                        user.guild.roles, name=list_roles[i])
                    await user.remove_roles(role)
                role = discord.utils.get(user.guild.roles, name=list_roles[2])
                await user.add_roles(role)
            elif count_points >= 300 and count_points < 500:
                for i in range(len(list_roles)):
                    role = discord.utils.get(
                        user.guild.roles, name=list_roles[i])
                    await user.remove_roles(role)
                role = discord.utils.get(user.guild.roles, name=list_roles[3])
                await user.add_roles(role)
            elif count_points >= 500 and count_points < 1000:
                for i in range(len(list_roles)):
                    role = discord.utils.get(
                        user.guild.roles, name=list_roles[i])
                    await user.remove_roles(role)
                role = discord.utils.get(user.guild.roles, name=list_roles[4])
                await user.add_roles(role)
            elif count_points >= 1000 and count_points < 2000:
                for i in range(len(list_roles)):
                    role = discord.utils.get(
                        user.guild.roles, name=list_roles[i])
                    await user.remove_roles(role)
                role = discord.utils.get(user.guild.roles, name=list_roles[5])
                await user.add_roles(role)
            elif count_points >= 2000 and count_points < 3000:
                for i in range(len(list_roles)):
                    role = discord.utils.get(
                        user.guild.roles, name=list_roles[i])
                    await user.remove_roles(role)
                role = discord.utils.get(user.guild.roles, name=list_roles[6])
                await user.add_roles(role)
            elif count_points >= 3000:
                for i in range(len(list_roles)):
                    role = discord.utils.get(
                        user.guild.roles, name=list_roles[i])
                    await user.remove_roles(role)
                role = discord.utils.get(user.guild.roles, name=list_roles[7])
                await user.add_roles(role)
        except TypeError:
            embed = discord.Embed(color=000, title='Something went wrong',
                                  description=f'Link your discord to **Telegram bot**')
            embed.set_footer(
                text='Prod by Luc143r || 🖤 || @insearchofmyself666')
            embed.set_image(
                url='https://i.pinimg.com/originals/2d/ec/5a/2dec5a7d09a41d02b606c6aa4803ee4b.jpg')
            await interaction.response.send_message(embed=embed, ephemeral=True)
            user = interaction.user
            for i in range(len(list_roles)):
                role = discord.utils.get(
                    user.guild.roles, name=list_roles[i])
                await user.remove_roles(role)


intents = discord.Intents.all()

bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)


async def check_guild():
    print('start thread check guild')
    type_req = ''
    name_guild = ''
    user = ''
    guild = bot.get_guild(695597338714177616)
    while 1:
        if os.path.exists('logs.json'):
            print('file is exists')
            with open('logs.json') as json_file:
                data = json.load(json_file)
                type_req = data['type_req']
                if type_req == 'create':
                    name_guild = data['name_guild']
                    await guild.create_role(name=name_guild)
                    admin_role = get(guild.roles, name=name_guild)
                    user = get(
                        guild.members, name=data['name'], discriminator=data['discr'])
                    overwrites = {
                        guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        admin_role: discord.PermissionOverwrite(
                            read_messages=True)
                    }
                    await guild.create_text_channel(name_guild, overwrites=overwrites)
                    await user.add_roles(admin_role)
                elif type_req == 'delete':
                    name_guild = data['name_guild']
                    try:
                        channel = discord.utils.get(
                            guild.channels, name=name_guild.lower())
                        role = get(guild.roles, name=name_guild)
                        await channel.delete()
                        await role.delete()
                        print('Guild and roles is delete!')
                    except:
                        print('Guild or roles is not found')
                elif type_req == 'add':
                    name_guild = data['name_guild']
                    try:
                        user = get(
                            guild.members, name=data['name'], discriminator=data['discr'])
                        role = get(guild.roles, name=name_guild)
                        await user.add_roles(role)
                        print('User add to guilds')
                    except:
                        print('User or roles is not found')
                elif type_req == 'remove':
                    name_guild = data['name_guild']
                    try:
                        user = get(
                            guild.members, name=data['name'], discriminator=data['discr'])
                        role = get(guild.roles, name=name_guild)
                        await user.remove_roles(role)
                        print('User remove to guilds')
                    except:
                        print('User or guilds is not found')
                elif type_req == 'rename':
                    name_guild = data['old_name']
                    new_name = data['new_name']
                    try:
                        channel = get(guild.channels, name=name_guild.lower())
                        await channel.edit(name=new_name)
                        role = get(guild.roles, name=name_guild)
                        await role.edit(name=new_name)
                        print('Guild is rename')
                    except:
                        print('Guild or roles is not found')
            remove('logs.json')
            await asyncio.sleep(10)
        else:
            await asyncio.sleep(15)


@bot.event
async def on_ready():
    print('[*] Bot started [*]')
    loop = asyncio.get_event_loop()
    loop.create_task(check_guild())


@bot.command()
async def get_forms(ctx: commands.Context):
    embed = discord.Embed(
        color=000, title=f'Hi! Glad to see you!', description="Hey! I'm a bot.")
    embed.set_footer(text='Prod by Luc143r || 🖤 || @insearchofmyself666')
    embed.set_image(
        url='https://i.pinimg.com/originals/2d/ec/5a/2dec5a7d09a41d02b606c6aa4803ee4b.jpg')
    view = Button()
    view.timeout = None
    await ctx.send(embed=embed, view=view)


bot.run(settings['token'])
