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
    if message.content == '/roleset':
        role = discord.utils.get(message.guild.roles, name='うんこ')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} うんこ！'
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
