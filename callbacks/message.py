from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils.persistence import bot_persistence
import re
from utils.api_method import get_client, save

VERIFY = 2
def request_password(update, context):
  context.user_data['username'] = update.message.text # 记录使用者的 Instapaper 登录名（username）
  update.message.reply_text('请输入密码：')
  return VERIFY


def verify_login(update, context):
  END = -1
  USERNAME = 0
  bot = context.bot
  context.user_data['password'] = update.message.text # 记录使用者的 Instapaper 密码（password）
  message = update.message.reply_text('登入中，请稍候…')
  if get_client(context.user_data):
    context.user_data['client'] = get_client(context.user_data)
    bot_persistence.flush()
    bot.edit_message_text(
      chat_id = message.chat_id,
      message_id = message.message_id,
      text = '登入成功！试试发送带链接的消息'
    ) 
    context.user_data['logged_in'] = True
    return END

  else:
    keyboard = [[InlineKeyboardButton("重新尝试",callback_data = 'login_confirm')]]
    markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
      chat_id = message.chat_id,
      message_id = message.message_id,
      text = '抱歉，未登入成功。',
      reply_markup = markup
    ) 
    context.user_data.pop('username')
    context.user_data.pop('password')
    return USERNAME

def save_link(update, context):
  logged_in = context.user_data.__contains__('client')
  if logged_in:
      client = context.user_data['client']
      message = update.message.text_html
      pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+') 
      links = re.findall(pattern, message)
      link_ids = {}
      titles = {}
      # pattern_ignore = r'https://readhacker\.news/c/.+'
      if not links:
        update.message.reply_text('消息中没有发现链接。')
      else:
        supported_iv = {r"http[s]?://liqi\.io/":"7610e8062aab10",
                        r"http[s]?://m\.qdaily\.com/mobile/articles/.+":"19c55d0f6b1acb",
                        r"http[s]?://www\.douban\.com/.+":"100c1db4937b79",
                        r"http[s]?://www\.ifanr\.com/.+":"00b04cf87f66cb",
                        r"http[s]?://sspai\.com/post/.+":"a6663c627d6258",
                        r"http[s]?://matters\.news/.+":"6382d3f855b181",
                        r"http[s]?://mp\.weixin\.qq\.com":"cc652f39dd9149"
        }
        def can_iv(link):
            for pattern in supported_iv.keys():
                if re.match(pattern, link):
                    return pattern
            return False
        def use_iv(rhash):
            return f"https://t.me/iv?url={link}&rhash={rhash}"
        count = 0
        failed = 0
        illegal_end = [")","(","!","."]
        message_saving = update.message.reply_text(f"保存中 …")
        for link in links:
          if link[-1] in illegal_end:
            link = link.strip(f"{link[-1]}")
          bookmark_id, title = save(client, link)
          link_ids[link] = bookmark_id
          titles[bookmark_id] = title
          if bookmark_id:
            count += 1
            context.bot.edit_message_text(
                chat_id = message_saving.chat.id,
                message_id = message_saving.message_id,
                text=f"已保存（{count}/{len(links)}）…"
              )
          else:
            failed += 1
        if count:
          failed_saving = f"另有 {failed} 篇未能保存。" if failed else ""
          context.bot.edit_message_text(
            chat_id = message_saving.chat.id,
            message_id = message_saving.message_id,
            text = f"成功保存 {count} 篇文章!\n"+ failed_saving
          )
        else:
          update.message.reply_text("未能成功保存 :(")
        for link in links:
          bookmark_id = link_ids[link]
          title = titles[bookmark_id]
          keyboard = [[
            InlineKeyboardButton("🗑", callback_data=f'delete_{bookmark_id}'),
            InlineKeyboardButton("💙", callback_data=f'like_{bookmark_id}')
          ]]
          markup = InlineKeyboardMarkup(keyboard)
          if can_iv(link):
            rhash = supported_iv[can_iv(link)]
            link = use_iv(rhash)
          update.message.reply_text(
            text=f"[{title}]({link})",
            reply_markup=markup, 
            parse_mode='MARKDOWN'
          )  
  else:
    update.message.reply_text('你还没有登入呢。\n前往：/start')