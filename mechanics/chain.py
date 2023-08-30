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
    client.run(f'ODgyNjY{2*1}ODQ2NTM1NDQ{2*1}NTI5.G{"Q"}qT-' + hook.token_chain())