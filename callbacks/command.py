from telegram import InlineKeyboardButton, InlineKeyboardMarkup
def start(update, context):
    USERNAME = 0
    END = -1
    if not context.user_data.__contains__('logged_in'):
        keyboard_lan = [
            [InlineKeyboardButton("注 册", url='https://www.instapaper.com/'),
            InlineKeyboardButton("登 入", callback_data='login_confirm')]
        ]
        markup = InlineKeyboardMarkup(keyboard_lan)
        update.message.reply_text(
            '欢迎使用 Instasaver！\n开始使用前，请先登录您的账号。', 
            reply_markup=markup
        )
        return USERNAME
    else:
        context.bot.delete_message(
            update.message.chat_id,
            update.message.message_id
        )
        return END

def quit_(update, context):
    CONFIRM_QUIT = 0
    END = -1
    if context.user_data.__contains__('logged_in'):
        keyboard = [
            [InlineKeyboardButton("返 回", callback_data='cancel_quit'),
             InlineKeyboardButton("解 绑", callback_data='confirm_quit')
            ]
        ]
        markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(
                '确认解绑账号吗？', 
                reply_markup=markup
            )
        return CONFIRM_QUIT
    else:
        update.message.reply_text("你还没有登入呢。\n前往：/start")
        return END

def about(update, context):
    keyboard = [[InlineKeyboardButton("源 代 码", url='https://github.com/dahawong/instasaver'),
                 InlineKeyboardButton("工 作 室", url='https://office.daha.me/')]]
    markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_html('<strong>Instasaver</strong> v2.0.1', reply_markup=markup)