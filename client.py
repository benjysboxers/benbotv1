
#client.py
import discord
import random # this is not needed if you dont want it, I just found it fun


# ur discord token is inserted here
TOKEN = {insert your discord token}
client = discord.Client()

@client.event
    # changes how call will behave
    # must list event loop to run this part of code
async def on_ready(): # event handler
    print('User Is connected as {0.user}'.format(client))


@client.event
async def on_message(message): # event handler
    username = str(message.author).split('#')[0] #split by # as this is what discord uses
    user_msg = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_msg} {channel})') # logs everything on server

    if message.author == client.user:
        return                   # setting discord channel name
    if message.channel.name == 'the-bubble': # set channel you wish commands to display in
        if user_msg.lower() == 'Greetings benbot': 
            await message.channel.send(f'Scrumptious day we are having {username}') #using fstring more efficient 
            return
        elif user_msg.lower() == 'goodbye':
            await message.channel.send(f'See you later {username}')
        elif user_msg.lower() == '!random':
            res = f'This is your generated number: {random.randrange(10000000000)}'
            await message.channel.send(res)
            return
        
    
    if user_msg.lower() == '!anywhere':
        await message.channel.send('This message can be sent anywhere')
        return
