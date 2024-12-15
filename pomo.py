from telegram import Update
from telegram.ext import CallbackContext
import asyncio


class Pomodoro:
    def __init__(self, session_time = 25*60, break_time = 5*60):
        self.session_time = session_time
        self.break_time = break_time

        self.active_session = False

    async def start_session(self, update: Update, context: CallbackContext):
        self.active_session = True
        await update.message.reply_text('Sua sessão começa agora!')

        await asyncio.sleep(self.session_time)
        await self.take_break(update, context)

    async def take_break(self, update: Update, context: CallbackContext):
        await update.message.reply_text(f"Você completou sua primeira sessão. Faça uma pausa de {int(self.break_time/60)} minutos")
        
        await asyncio.sleep(self.break_time)
        await self.back_to_pomo(update, context)

    async def back_to_pomo(self, update:Update, context: CallbackContext):
        await update.message.reply_text("Sua pausa acabou! Para iniciar uma nova sessão, utilize o comando /pomodoro")