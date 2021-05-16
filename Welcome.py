# creator tg: @dentlyftgmod



from .. import loader, utils





@loader.tds

class WelcomeMod(loader.Module):

    """??иве???вие нов?? пол?зова?елей в ?а?е."""

    strings = {'name': 'Welcome'}



    async def client_ready(self, client, db):

        self.db = db

        self.client = client



    async def welcomecmd(self, message):

        """?кл??и??/в?кл??и?? п?иве???вие нов?? пол?зова?елей в ?а?е. ??пол?з?й: .welcome <clearall (по желани?)>."""

        welcome = self.db.get("Welcome", "welcome", {})

        chatid = str(message.chat_id)

        args = utils.get_args_raw(message)

        if args == "clearall":

            self.db.set("Welcome", "welcome", {})

            return await message.edit("<b>[Welcome Mode]</b> ??е на???ойки мод?л? ?б?о?ен?.")



        if chatid in welcome:

            welcome.pop(chatid)

            self.db.set("Welcome", "welcome", welcome)

            return await message.edit("<b>[Welcome Mode]</b> ?еак?иви?ован!")



        welcome.setdefault(chatid, {})

        welcome[chatid].setdefault("message", "?об?о пожалова?? в ?а?!")

        welcome[chatid].setdefault("is_reply", False)

        self.db.set("Welcome", "welcome", welcome)

        await message.edit("<b>[Welcome Mode]</b> ?к?иви?ован!")





    async def setwelcomecmd(self, message):

        """У??анови?? новое п?иве???вие нов?? пол?зова?елей в ?а?е.\n??пол?з?й: .setwelcome <?ек?? (можно и?пол?зова?? {name}; {chat})>; ни?его."""

        welcome = self.db.get("Welcome", "welcome", {})

        args = utils.get_args_raw(message)

        reply = await message.get_reply_message()

        chatid = str(message.chat_id)

        chat = await message.client.get_entity(int(chatid)) 

        try:

            if not args and not reply:

                return await message.edit(f'<b>??иве???вие нов?? пол?зова?елей в "{chat.title}":</b>\n\n'

                                          f'<b>С?а???:</b> ?кл??ено.\n'

                                          f'<b>??иве???вие:</b> {welcome[chatid]["message"]}\n\n'

                                          f'<b>~ У??анови?? новое п?иве???вие можно ? помо??? команд?:</b> .setwelcome <?ек??>.')

            else:

                if reply:

                    welcome[chatid]["message"] = reply.id

                    welcome[chatid]["is_reply"] = True

                else:

                    welcome[chatid]["message"] = args

                    welcome[chatid]["is_reply"] = False

                self.db.set("Welcome", "welcome", welcome)

                return await message.edit("<b>?овое п?иве???вие ???ановлено ??пе?но!</b>")

        except KeyError: return await message.edit(f'<b>??иве???вие нов?? пол?зова?елей в "{chat.title}":</b>\n\n'

                                                   f'<b>С?а???:</b> ??кл??ено')





    async def watcher(self, message):

        """?н?е?е?но, по?ем? он именно watcher наз?вае???... ??"""

        try:

            welcome = self.db.get("Welcome", "welcome", {})

            chatid = str(message.chat_id)

            if chatid not in welcome: return

            if message.user_joined or message.user_added:

                user = await message.get_user()

                chat = await message.get_chat()

                if welcome[chatid]["is_reply"] == False:

                    return await message.reply((welcome[chatid]["message"]).format(name=user.first_name, chat=chat.title))

                msg = await self.client.get_messages(int(chatid), ids=welcome[chatid]["message"])

                await message.reply(msg)

        except: pass
