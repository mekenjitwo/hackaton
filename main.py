import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

ımza_kampanyaları=['https://www.change.org/p/santraller-yatırımları-tamamlamadan-tekrar-havamızı-kirletmeye-başladı-izinvermeyin-temizhavahaktır-csbgovtr-murat-kurum', 'https://www.change.org/p/%C3%A7evre-ve-%C5%9Fehircilik-bakanl%C4%B1%C4%9F%C4%B1-deniz-kirlili%C4%9Fi?source_location=search', 'https://www.change.org/p/%C3%A7evre-ve-%C5%9Fehircilik-bakanl%C4%B1%C4%9F%C4%B1-hava-kirlili%C4%9Fi?source_location=search', 'https://www.change.org/p/soma-da-termik-santrale-filtre-tak%C4%B1lmas%C4%B1n%C4%B1-talep-ediyoruz-csbgovtr-manisavaliligi?source_location=search', 'https://www.change.org/p/karbon-n%C3%B6tr-gelecek-ve-iklim-krizi-zorunlu-kamu-spotu-olsun-csbgovtr-rtukkurumsal?source_location=search']


@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben sizin çevre danışmanı botunuzum.')

@bot.command()
async def kampanya(ctx):
    mevcutimza=random.choice(ımza_kampanyaları)
    await ctx.send(f'{mevcutimza}')

bot.run("token")