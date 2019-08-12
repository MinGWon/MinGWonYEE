import discord
import os

client = discord.Cilent();

@client.event
    print("Ready")
    
    
@client.event
async def on_message(message):
    if message.content.startwith("명령어");
        await message.channel.send("")
        

        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
