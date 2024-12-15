from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from pomo import Pomodoro
from summary import Summary

class StudyBot:
    def __init__(self, token = "YOUR-BOT-TOKEN") -> None:
        self.application = ApplicationBuilder().token(token).build()
        self.summary = Summary()
        self.pomo = Pomodoro()

        self.start_handler = CommandHandler('start', self.start)
        self.summary_handler = CommandHandler('resumir', self.summary_command)
        self.pomodoro_handler = CommandHandler('pomodoro', self.handle_pomodoro)

        self.run()
        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'Olá, {update.effective_user.first_name}!')

    async def summary_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        summary_text = self.summary.fetch_summary(' '.join(context.args))
        await update.message.reply_text(summary_text)

    async def handle_pomodoro(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "Sua sessão pomodoro está prestes a começar. Foque por 25 minutos e notificarei sua pausa!"
        )
        await self.pomo.start_session(update=update, context=context)

    def run(self):
        self.application.add_handler(self.start_handler)
        self.application.add_handler(self.summary_handler)
        self.application.add_handler(self.pomodoro_handler)

        self.application.run_polling()
