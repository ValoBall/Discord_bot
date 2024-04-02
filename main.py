import discord
from bot_logic import gen_pass
# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_ready():
    print("ready")
    await client.change_presence(status=discord.Status.online)

@client.event   
async def on_message(message):  
    print('message')
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Cześć!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$password'):
        await message.channel.send(f'Twoje hasło to:\n{gen_pass(10)}')       
    else:
        await message.channel.send(message.content)

client.run('MTIyMDA0NzU5NDE1NjE5NTkyMA.GPaSJ7.99PbTmqna8YQpqM7mD1m03gS-02c3TBkMiH9AY')
   