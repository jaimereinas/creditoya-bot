#!/usr/bin/env python3
"""
Bot de Telegram - Créditos Rápidos Colombia
Requiere: pip install python-telegram-bot==20.7
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ──────────────────────────────────────────────
# CONFIGURACIÓN — cambia estos valores
# ──────────────────────────────────────────────
BOT_TOKEN = "8665908848:AAEXwx8_SrF4JdwsuUTHMO9Sj8PSMUiT4hk"
OFERTAS_URL = "https://TU-PAGINA.com" # ← Cambia esto por tu URL real
BOT_USERNAME = "@CreditoYaOnline_bot"

# Imagen de bienvenida (URL pública o file_id de Telegram)
WELCOME_IMAGE_URL = "https://i.imgur.com/tu-imagen.jpg"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# ──────────────────────────────────────────────
# /start — Mensaje principal
# ──────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    first_name = user.first_name if user.first_name else "amigo"

    caption = (
        f"🎉 *¡BIENVENIDO, {first_name}!*\n\n"
        "¡Puedes pasar al proceso ahora mismo!\n\n"
        "💚 *PRIMER CRÉDITO — 0%*\n"
        "_Sin condiciones ocultas ni costos extra_\n\n"
        "⚡ Rápido  •  🖥️ Fácil  •  🌐 Online\n\n"
        "Todo el proceso toma solo *unos minutos*\n\n"
        "👇 Haz clic abajo y elige el monto"
    )

    keyboard = [
        [InlineKeyboardButton("💳 OBTENER CRÉDITO AHORA", url=OFERTAS_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        # Enviar imagen + texto + botón
        await update.message.reply_photo(
            photo=WELCOME_IMAGE_URL,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
    except Exception:
        # Si la imagen falla, enviar solo texto
        await update.message.reply_text(
            text=caption,
            parse_mode="Markdown",
            reply_markup=reply_markup
        )


# ──────────────────────────────────────────────
# /ayuda — Comandos disponibles
# ──────────────────────────────────────────────
async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📋 *Comandos disponibles:*\n\n"
        "/start — Ver ofertas de crédito\n"
        "/credito — Solicitar crédito ahora\n"
        "/requisitos — Ver requisitos\n"
        "/ayuda — Este mensaje\n\n"
        "💬 Para más info escríbenos directamente."
    )
    await update.message.reply_text(text, parse_mode="Markdown")


# ──────────────────────────────────────────────
# /credito — Acceso directo a ofertas
# ──────────────────────────────────────────────
async def credito(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💳 Ver todas las ofertas", url=OFERTAS_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        "💰 *Montos disponibles:*\n\n"
        "• $100.000 — $500.000 pesos\n"
        "• $500.000 — $2.000.000 pesos\n"
        "• $2.000.000 — $10.000.000 pesos\n\n"
        "✅ Aprobación en *5–7 minutos*\n"
        "🏦 Transferencia directa a tu cuenta\n"
        "🔒 100% seguro y confidencial\n\n"
        "👇 Elige tu monto:"
    )
    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=reply_markup)


# ──────────────────────────────────────────────
# /requisitos
# ──────────────────────────────────────────────
async def requisitos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📄 *Requisitos mínimos:*\n\n"
        "✅ Ser mayor de 18 años\n"
        "✅ Cédula de ciudadanía colombiana\n"
        "✅ Cuenta bancaria a tu nombre\n"
        "✅ Celular activo\n\n"
        "❌ Sin codeudor\n"
        "❌ Sin finca raíz\n"
        "❌ Sin papeleo\n\n"
        "💚 *¡Aplica en minutos!*"
    )
    keyboard = [
        [InlineKeyboardButton("💳 Solicitar ahora", url=OFERTAS_URL)]
    ]
    await update.message.reply_text(
        text, parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ──────────────────────────────────────────────
# Mensaje genérico para cualquier texto
# ──────────────────────────────────────────────
async def mensaje_generico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("💳 Ver ofertas de crédito", url=OFERTAS_URL)]]
    await update.message.reply_text(
        "👋 Para ver las ofertas disponibles presiona el botón 👇\n\n"
        "O escribe /start para comenzar.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ayuda", ayuda))
    app.add_handler(CommandHandler("help", ayuda))
    app.add_handler(CommandHandler("credito", credito))
    app.add_handler(CommandHandler("requisitos", requisitos))

    # Captura cualquier mensaje de texto
    from telegram.ext import MessageHandler, filters
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensaje_generico))

    logger.info("✅ Bot iniciado correctamente...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
