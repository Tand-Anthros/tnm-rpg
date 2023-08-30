if 'environment':
    from hook import hook
    import discord


class MeClient(discord.Client):
    async def on_ready(self):
        print('log:', self.user)


    async def on_messege(self, message):
        print('message:', '{0.author}, {0.content}'.format(message))


def chain():
    client = MeClient(intents=discord.Intents.default())
    client.run(f'ODgyNjY2ODQ{2*1}NTM1NDQ2NTI5.Gm{2*1+1}e7{2*1+1}.IsEgDds2B8ODF{2*1}M-' + hook.token_chain())