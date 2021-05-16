# creator tg: @dentlyftgmod

from .. import loader, utils

import requests

@loader.tds

class WttrInMod(loader.Module):

    """WttrIn"""

    strings = {'name': 'WttrIn'}

    @loader.owner

    async def wthrcmd(self, m):

        """.wthr <Р“РѕСЂРѕРґ РµСЃР»Рё РЅР°РґРѕ>

        РџРѕР»СѓС‡РёС‚СЊ С‚РµРєСѓС‰СѓСЋ РїРѕРіРѕРґСѓ

        """

        rr = utils.get_args_raw(m)

        await m.edit("<code>{}</code>".format(requests.get(f"https://wttr.in/{rr if rr != None else ''}?0Tq&lang=ru").text))
