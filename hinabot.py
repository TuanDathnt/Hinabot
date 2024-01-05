import discord
import os
from discord.ext import commands
import datetime
from datetime import timedelta

bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())
bot.remove_command('help')

member_time_in = {}
member_time_total= {}

@bot.event
async def on_ready():
  print('Logged in as ' + bot.user.name + '!')


@bot.event
async def on_message(message):
  await bot.process_commands(message)


@bot.command(name='hello')
async def hello(ctx):
  await ctx.send('Hello There!')


@bot.command(name='ping')
async def ping(ctx):
  await ctx.send(f'Pong! ||{round(bot.latency * 1000)} ms||')

@bot.command(name='studytime')
async def studytime(ctx):
  if ctx.author.id not in member_time_total:
     member_time_total[ctx.author.id]=timedelta(days=0, hours=0, minutes=0, seconds=0)
  time_study = member_time_total[ctx.author.id]
  days = time_study.days
  hours, remainder = divmod(time_study.seconds, 3600)
  minutes, seconds = divmod(remainder, 60)
  formatted_study = f"{days} days, {hours:02}:{minutes:02}:{seconds:02}"
  await ctx.send(f"You have been studying for {formatted_study}!")
@bot.command(name='help')
async def help(ctx):
  em = discord.Embed(title='Help',
                     description='See what all I could do for you!',
                     color=000000)
  em.add_field(
      name='Commands',
      value=
      '`?hello` to say hello to me!\n`?ping` to check my ping!\n`?help` to see this message!',
      inline=False)
  await ctx.send(embed=em)





@bot.event
async def on_voice_state_update(member, before, after):
  target_voice_room_id = 1192416081889988609  # ID của phòng thoại mục tiêu
  channel_id = 1192414676978507781  # ID của kênh tin nhắn
  channel = bot.get_channel(channel_id)

  if after.channel and after.channel.id == target_voice_room_id:
    # Người dùng vừa vào phòng thoại mục tiêu
    start_time = datetime.datetime.now()
    member_time_in[member.id] = datetime.datetime.now()
    formatted_timestart = start_time.strftime("%Y-%m-%d %H:%M:%S")
    await channel.send(
        f"{member.name} đã bắt đầu học lúc {formatted_timestart}")

  elif (before.channel.id == target_voice_room_id and before.channel and before.channel != after.channel):
    # Người dùng vừa rời khỏi phòng thoại
    end_time = datetime.datetime.now() - member_time_in[member.id]
    days = end_time.days
    hours, remainder = divmod(end_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if member.id not in member_time_total:
       member_time_total[member.id]=timedelta(days=0, hours=0, minutes=0, seconds=0)
    member_time_total[member.id] = end_time+member_time_total[member.id]
    # Định dạng thành chuỗi
    formatted_timedelta = f"{days} days, {hours:02}:{minutes:02}:{seconds:02}"

    await channel.send(
        f"{member.name} đã cảm thấy bất lực: thời gian học{formatted_timedelta}"
    )


bot.run('MTE5Mjc5OTkyMjQ5NjQ3NTIxOA.GuKIB-.AMTl0Wz-GIoWOHqGpQRlXtx4_yhoGAwZwI3sYM')
