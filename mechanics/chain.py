if 'environment':
    from variables import variables
    from discord import Intents
    from discord.ext import commands
    from threading import Thread
    import subprocess, os, sys, time


if 'discord don`t fine closed this':
    bot = commands.Bot(command_prefix = '$', intents = Intents.default())

    @bot.event
    async def on_ready():
        channel = bot.get_channel(906303679450206298)
        command = [message async for message in channel.history(limit=1)][0].content
        variables.set('chain_take', str(command))

        command = variables.get('chain_send')
        if command not in [None, False, '']: 
            await channel.send(command)
            variables.set('chain_send', '')
        exit()

    if len(sys.argv) > 1 and sys.argv[1] == '__cycle__':
        sys.stderr = open(os.devnull, 'w')
        bot.run(f'ODgyNjY2ODQ{2*1}NTM1NDQ2NTI5.Gm{2*1+1}e7{2*1+1}.IsEgDds2B8ODF{2*1}M-LIE7Yg-Sf{2*3}apKMcd{"Yag"}EgY')


class chain():
    def __init__(self):
        pass
            

    def update(self):
        if os.name == 'nt': subprocess.call(['py', 'chain.py', '__cycle__'])
        else: subprocess.call(['python3', 'chain.py', '__cycle__'])
    

    def take(self):
        self.update()
        return variables.get('chain_take')



    def send(self, command):
        variables.set('chain_send', str(command))
        self.update()


chain = chain()