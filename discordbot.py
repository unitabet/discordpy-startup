from discord.ext import commands
import os
import traceback
import random
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
        
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/state」と発言したら「active」が返る処理、起動確認用
    if message.content == '/state':
        await message.channel.send('active')
    # 「/roleset」と発言したら乱数に応じた役職が付与される機能、拡張性追加のためにリスト参照型に変更予定
    if message.content == '/roleset':
        rand = random.randint(0,9999)
        if rand == 0:
                role = discord.utils.get(message.guild.roles, name='神')
                await message.author.add_roles(role)
                reply = f'{message.author} は神です…新たなる神話の始まりだ。'
                await message.channel.send(reply)
        elif rand < 50:
                role = discord.utils.get(message.guild.roles, name='パリピ')
                await message.author.add_roles(role)
                reply = f'{message.author} はパリピです。'
                await message.channel.send(reply)
        elif rand < 150:
                role = discord.utils.get(message.guild.roles, name='デモゴルゴン')
                await message.author.add_roles(role)
                reply = f'{message.author} はデモゴルゴンです。'
                await message.channel.send(reply)         
        elif rand < 350:
                role = discord.utils.get(message.guild.roles, name='Premiam Kintama')
                await message.author.add_roles(role)
                reply = f'{message.author} はPremiam Kintamaです。'
                await message.channel.send(reply)        
        elif rand < 1000:
                role = discord.utils.get(message.guild.roles, name='厨二病')
                await message.author.add_roles(role)
                reply = f'{message.author} は、厨二病です。'
                await message.channel.send(reply) 
        elif rand < 2500:
                role = discord.utils.get(message.guild.roles, name='ヤドン秋山')
                await message.author.add_roles(role)
                reply = f'{message.author} は、ヤドン秋山です。'
                await message.channel.send(reply)
        elif rand < 4500:
                role = discord.utils.get(message.guild.roles, name='ショーン')
                await message.author.add_roles(role)
                reply = f'{message.author} は、ショーンです。'
                await message.channel.send(reply) 
        elif rand < 9500:
                role = discord.utils.get(message.guild.roles, name='陰キャ')
                await message.author.add_roles(role)
                reply = f'{message.author} は、陰キャです。'
                await message.channel.send(reply) 
         else:
                role = discord.utils.get(message.guild.roles, name='うんこ')
                await message.author.add_roles(role)
                reply = f'{message.author} は、うんこです。'
                await message.channel.send(reply) 
    # メンバーのリストを取得して表示
    if message.content == '/members':
        await message.channel.send(message.guild.members)
    # 役職のリストを取得して表示
    if message.content == '/roles':
        await message.channel.send(message.guild.roles)
    # テキストチャンネルのリストを取得して表示
    if message.content == '/text_channels':
        await message.channel.send(message.guild.text_channels)
    # ボイスチャンネルのリストを取得して表示
    if message.content == '/voice_channels':
        await message.channel.send(message.guild.voice_channels)
    # カテゴリチャンネルのリストを取得して表示
    if message.content == '/category_channels':
        await message.channel.send(message.guild.categories)
    

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)
