# Initializing the Telegram Bot API
import telebot

bot = telebot.TeleBot(<YOUR_API_TOKEN>)

# Adding the bot to a group
@bot.message_handler(commands=['add_bot'])
def add_bot_to_group(message):
    if message.chat.type == 'group':
        bot.add_chat_member(message.chat.id, bot.get_me().id)
        bot.reply_to(message, 'I\'ve been added to the group!')

# Creating an admin role for the Telegram Bot
@bot.message_handler(commands=['make_admin'])
def make_admin(message):
    if message.chat.type == 'group':
        bot.set_chat_administrator_custom_title(message.chat.id, message.from_user.id, 'Group Admin')
        bot.reply_to(message, 'Admin role has been assigned to the user!')

# Adding bot settings to allow admin to set custom limit to group users
@bot.message_handler(commands=['set_limit'])
def set_limit(message):
    if message.chat.type == 'group':
        # Get the custom limit from the user
        user_input = message.text.split()[1]
        # Set the custom limit
        bot.set_chat_permissions(message.chat.id, user_input)
        bot.reply_to(message, f'Custom limit of {user_input} has been set!')
