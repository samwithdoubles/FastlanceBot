#note: if you do not know how to make a discord bot, there is a file called how2create.txt that will guide you
import disnake
from disnake.ext import commands
import keepalive
import os
from datetime import datetime as date

#Create intents
intents = disnake.Intents(messages=True, message_content=True, guilds=True, members=True)

#Create the bot object
client = commands.Bot(command_prefix='!', intents=intents, case_insensitive = True)

#You can change the prefix to whatever you would like

#remove default help command
client.remove_command('help')

# Set bot presence
@client.event
async def on_ready():
	#set presence to do not disturb and playing "prefix is !"
	await client.change_presence(status=disnake.Status.dnd, activity=disnake.Activity(type=disnake.ActivityType.playing, name = "prefix is !"))
	# print to console that bot is ready
	print("bot is ready")

# Our first command!
@client.command()
async def ping(ctx):
	#time at which command was sent
	start = date.timestamp(date.now())
	#send back how long it took for bot to respond
	await ctx.send(f':ping_pong: Pong! {( date.timestamp( date.now() ) - start ) * 10000000}ms.')

#create new command
@client.command()
#check that user has ban permissions **IMPORTANT**
@commands.has_permissions(ban_members = True)
async def ban(ctx, member:disnake.Member):
	# ban the user
	await member.ban()
	# confirmation message
	await ctx.send(member.mention + " has been banned")

#create a help command
@client.command()
async def help(ctx):
	# create an embed
	embed = disnake.Embed(title = "Help", color = disnake.Color.blue())
	#add field to embed
	embed.add_field(name = "Ping", value = "Sends a message saying how long it took for the bot to respond")
	#add another field to embed
	embed.add_field(name = "ban", value = "Bans given user. Required ")

	#send embed
	await ctx.send(embed = embed)

#Get token from environment secrets
token = os.getenv("TOKEN")

#Run keep alive (can be commented out if 24/7 is not wanted)
#note: if you want to have 24/7 hosting, there is a file called how2host.txt that will guide you
keepalive.keep_alive()

#Run the bot
# note: you can put your token directly into client.run() if you do not want to make an environment secret
# not putting it into an environment secret is risky because anyone can access it and take over your bot! there is a link in the readme explaining how to add a secret. 
client.run(token)

