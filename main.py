import discord

client = discord.Cilent();

@client.event
    print(client.user.id)
    print("Ready")
    
    
@client.event
async def on_message(message):
    if message.content.startwith("명령어");
        await message.channel.send("")
        
  
client.run("")