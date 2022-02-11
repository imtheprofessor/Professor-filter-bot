from random import choice
from config import START_MSG, FORCES_SUB, BOT_PICS, ADMINS, bot_info, DEV_NAME
from pyrogram import Client as LuciferMoringstar_Robot, filters as Worker
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import LuciferMoringstar
from LuciferMoringstar_Robot.database.broadcast_db import Database

db = Database()


@LuciferMoringstar_Robot.on_message(Worker.private & Worker.command(["start"]))
async def start_message(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
    if len(message.command) != 2:
        if message.from_user.id not in ADMINS: 
            buttons = [[
             InlineKeyboardButton('🔍𝐒𝐄𝐀𝐑𝐂𝐇 𝐅𝐈𝐋𝐄', switch_inline_query_current_chat='')
             ],[
             InlineKeyboardButton("🧐 𝐇𝐄𝐋𝐏 🍿", callback_data="help"),
             InlineKeyboardButton("🧐 𝐀𝐁𝐎𝐔𝐓 🍿", callback_data="about") 
             ],[
             InlineKeyboardButton("🧐 𝐆𝐑𝐎𝐔𝐏 🍿", url="https://t.me/freakersfilmy"),
             InlineKeyboardButton("🧐 𝐌𝐎𝐕𝐈𝐄𝐒 🍿", url="https://t.me/freakersmovies")
             ]]
        else:
            buttons = [[
             InlineKeyboardButton('🔍𝐒𝐄𝐀𝐑𝐂𝐇 𝐅𝐈𝐋𝐄', switch_inline_query_current_chat='')
             ],[
             InlineKeyboardButton("🧐 𝐇𝐄𝐋𝐏 🍿", callback_data="bot_owner"),
             InlineKeyboardButton("🧐 𝐀𝐁𝐎𝐔𝐓 🍿", callback_data="about") 
             ],[
             InlineKeyboardButton("🧐 𝐆𝐑𝐎𝐔𝐏 🍿", url="https://t.me/freakersfilmy"),
             InlineKeyboardButton("🧐 𝐌𝐎𝐕𝐈𝐄𝐒  🍿", url="https://t.me/freakersmovies")
             ]]    
        await message.reply_photo(photo = choice(BOT_PICS), caption=START_MSG.format(mention = message.from_user.mention, bot_name = bot_info.BOT_NAME, bot_username = bot_info.BOT_USERNAME), reply_markup=InlineKeyboardMarkup(buttons))
        
    elif len(message.command) ==2 and message.command[1] in ["subscribe"]:
        FORCES=["https://telegra.ph/file/b2acb2586995d0e107760.jpg"]
        invite_link = await bot.create_chat_invite_link(int(FORCES_SUB))
        button=[[
         InlineKeyboardButton("🧐 𝐉𝐎𝐈𝐍 𝐇𝐄𝐑𝐄 🍿", url=invite_link.invite_link)
         ]]
        reply_markup = InlineKeyboardMarkup(button)
        await message.reply_photo(
            photo=choice(FORCES),
            caption=f"""<i><b>Hello {message.from_user.mention}. \nYou Have <a href="{invite_link.invite_link}">Not Subscribed</a> To <a href="{invite_link.invite_link}">My Update Channel</a>.So you do not get the Files on Inline Mode, Bot Pm and Group</i></b>""",
            reply_markup=reply_markup
        )
        return
   
@LuciferMoringstar_Robot.on_message(Worker.private & Worker.command(["help"]))
async def help(bot, message):
    button = [[
     InlineKeyboardButton("🧐 𝐇𝐎𝐌𝐄 🍿", callback_data="start"),
     InlineKeyboardButton("🧐 𝐀𝐁𝐎𝐔𝐓 🍿", callback_data="about")
     ]]
    await message.reply_photo(
        photo = choice(BOT_PICS),
        caption=LuciferMoringstar.HELP_MSG.format(mention=message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(button))
      
@LuciferMoringstar_Robot.on_message(Worker.private & Worker.command(["about"]))
async def about(bot, message):
    button = [[
     InlineKeyboardButton("🧐 𝐇𝐎𝐌𝐄 🍿", callback_data="start"),
     InlineKeyboardButton("🧐 𝐂𝐋𝐎𝐒𝐄 🍿", callback_data="close")
     ]]  
    await message.reply_photo(
        photo = choice(BOT_PICS),
        caption=LuciferMoringstar.ABOUT_MSG.format(mention=message.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME, dev_name=DEV_NAME),
        reply_markup=InlineKeyboardMarkup(button))
        
