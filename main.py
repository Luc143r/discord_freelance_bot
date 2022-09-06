import discord
from discord.ext import commands
from discord import DMChannel

from config import settings, settings_db
from mongo import get_id, get_points


"""class Wallet(discord.ui.Modal, title='Testing input'):
    wallet = discord.ui.TextInput(
        label='Write text', placeholder='Your text here...', min_length=48)

    async def on_submit(self, interaction: discord.Interaction):
        wallet_value = interaction.data['components'][0]['components'][0]['value']
        await interaction.response.send_message(f'Your text:\n{wallet_value}\n**Writing in my database**', ephemeral=True)

    async def on_error(self, interaction: discord.Interaction):
        await interaction.response.send_message('Oops. Хуйня какая-то)', ephemeral=True)"""


class Button(discord.ui.View):
    def __init__(self):
        super().__init__()

    """@discord.ui.button(label='Test button', style=discord.ButtonStyle.green)
    async def registration(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(Wallet())"""

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
                    role = role = discord.utils.get(
                        user.guild.roles, name=list_roles[i])
                    await user.remove_roles(role)
                role = discord.utils.get(user.guild.roles, name=list_roles[0])
                await user.add_roles(role)
            elif count_points >= 10 and count_points < 100:
                for i in range(len(list_roles)):
                    role = role = discord.utils.get(
                        user.guild.roles, name=list_roles[i])
                    await user.remove_roles(role)
                role = discord.utils.get(user.guild.roles, name=list_roles[1])
                await user.add_roles(role)
            elif count_points >= 100 and count_points < 300:
                for i in range(len(list_roles)):
                    role = role = discord.utils.get(
                        user.guild.roles, name=list_roles[i])
                    await user.remove_roles(role)
                role = discord.utils.get(user.guild.roles, name=list_roles[2])
                await user.add_roles(role)
            elif count_points >= 300 and count_points < 500:
                for i in range(len(list_roles)):
                    role = role = discord.utils.get(
                        user.guild.roles, name=list_roles[i])
                    await user.remove_roles(role)
                role = discord.utils.get(user.guild.roles, name=list_roles[3])
                await user.add_roles(role)
            elif count_points >= 500 and count_points < 1000:
                for i in range(len(list_roles)):
                    role = role = discord.utils.get(
                        user.guild.roles, name=list_roles[i])
                    await user.remove_roles(role)
                role = discord.utils.get(user.guild.roles, name=list_roles[4])
                await user.add_roles(role)
            elif count_points >= 1000 and count_points < 2000:
                for i in range(len(list_roles)):
                    role = role = discord.utils.get(
                        user.guild.roles, name=list_roles[i])
                    await user.remove_roles(role)
                role = discord.utils.get(user.guild.roles, name=list_roles[5])
                await user.add_roles(role)
            elif count_points >= 2000 and count_points < 3000:
                for i in range(len(list_roles)):
                    role = role = discord.utils.get(
                        user.guild.roles, name=list_roles[i])
                    await user.remove_roles(role)
                role = discord.utils.get(user.guild.roles, name=list_roles[6])
                await user.add_roles(role)
            elif count_points >= 3000:
                for i in range(len(list_roles)):
                    role = role = discord.utils.get(
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
                role = role = discord.utils.get(user.guild.roles, name=list_roles[i])
                await user.remove_roles(role)
            #role = discord.utils.get(user.guild.roles, name='0 - Heir')
            #await user.add_roles(role)


intents = discord.Intents.all()

bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)


@bot.event
async def on_ready():
    print('[*] Bot started')


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
