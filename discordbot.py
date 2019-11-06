from discord.ext import commands
import os
import traceback
import random
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
menberID = []
memberEXP = []
        
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
        await message.channel.send('```➢現在稼働中です \n  ver1.1.17です \n  定期メンテナンスは毎週日曜の0時からです```')
    if message.content == '/help':
        await message.channel.send('```➢/state \n  稼働状況を確認します \n 　\n　/roleset \n　役職をランダムに付与します \n 　\n　/probability \n　rolesetコマンドの確率内訳を表示します \n 　\n  /members \n  現在サーバーに所属するメンバーをすべて表示します \n　\n  /roles \n　現在サーバーにある役職をすべて表示します \n　\n  /text_channels \n　現在サーバーにあるテキストチャンネルをすべて表示します \n　\n  /voice_channels \n　現在サーバーにあるテキストチャンネルをすべて表示します \n　\n  /category_channels \n　現在サーバーにあるカテゴリチャンネルをすべて表示します```')
    # 「/roleset」と発言したら乱数に応じた役職が付与される機能、拡張性追加のためにリスト参照型に変更予定
    if message.content == '/roleset':
        rand = random.randint(0,9999)
        if rand == 0:
                role = discord.utils.get(message.guild.roles, name='神')
                await message.author.add_roles(role)
                reply = f'{message.author.mention} は神です。新たなる神話の始まりだ。'
                await message.channel.send(reply)
        elif rand < 50:
                role = discord.utils.get(message.guild.roles, name='パリピ')
                await message.author.add_roles(role)
                reply = f'{message.author.mention} はパリピです。'
                await message.channel.send(reply)
        elif rand < 150:
                role = discord.utils.get(message.guild.roles, name='DEMOGORGON')
                await message.author.add_roles(role)
                reply = f'{message.author.mention} はDEMOGORGONです。'
                await message.channel.send(reply)
        elif rand < 350:
                role = discord.utils.get(message.guild.roles, name='Premium　KINTAMA')
                await message.author.add_roles(role)
                reply = f'{message.author.mention} はPremium　KINTAMAです。'
                await message.channel.send(reply)
        elif rand < 1000:
                role = discord.utils.get(message.guild.roles, name='厨二病')
                await message.author.add_roles(role)
                reply = f'{message.author.mention} は厨二病です。'
                await message.channel.send(reply)
        elif rand < 2500:
                role = discord.utils.get(message.guild.roles, name='ヤドン秋山')
                await message.author.add_roles(role)
                reply = f'{message.author.mention} はヤドン秋山です。'
                await message.channel.send(reply)
        elif rand < 4500:
                role = discord.utils.get(message.guild.roles, name='ショーン')
                await message.author.add_roles(role)
                reply = f'{message.author.mention} はショーンです。'
                await message.channel.send(reply)
        elif rand < 9500:
                role = discord.utils.get(message.guild.roles, name='陰キャ')
                await message.author.add_roles(role)
                reply = f'{message.author.mention} は陰キャです。'
                await message.channel.send(reply)
        elif rand < 10000:
                role = discord.utils.get(message.guild.roles, name='うんこ')
                await message.author.add_roles(role)
                reply = f'{message.author.mention} はうんこ。'
                await message.channel.send(reply)
    if message.content == '/probability':
        await message.channel.send('```➢[神] 0.01% \n　[パリピ] 0.49% \n　[デモゴルゴン] 1.0% \n　[Premiam Kintama] 2.0%  \n　[厨二病] 6.5%  \n　[ヤドン秋山] 15.0%  \n　[ショーン] 20.0%  \n　[陰キャ] 50.0%  \n　[うんこ] 5.0% ```')
    # 0~9999の間で乱数を返す
    if message.content == '/rand':
        rand = random.randint(0,9999)   
        await message.channel.send(rand)
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
