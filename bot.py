import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):

    if message.content.startswith('!help'):
        await client.send_message(
            message.channel,
            'This bot is intended to be used as test bot.\nThe bot does not have any important functions yet.\nCurrently, it has function like:\n!help : will display help messsage.\n!test : will reply back with word test!!!!\n'
        )

    elif message.content.startswith('!test'):
        await client.send_message(message.channel, 'test!!!!')
    elif message.content.startswith('!version_info'):
        trial = client.is_logged_in
        await client.send_message(message.channel, trial)

    elif message.content.startswith('!say'):
        await client.send_message(message.channel, 'leave message')
        msg = await client.wait_for_message(
            timeout=15.0, author=message.author)

        if msg is None:
            await client.send_message(message.channel,
                                      '15초내로 입력해주세요. 다시시도: !say')
            return
        else:
            await client.send_message(message.channel, msg.content)


client.run('token')


