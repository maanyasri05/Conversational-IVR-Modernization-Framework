import re

def detect_intent(message):

    message = message.lower()

    if "pnr" in message or "p n r" in message:
        return "PNR_STATUS"

    if "train" in message:
        return "TRAIN_SCHEDULE"

    if "book" in message:
        return "BOOK_TICKET"

    if "cancel" in message:
        return "CANCEL_TICKET"

    if "end" in message or "bye" in message:
        return "END_CALL"

    return "FALLBACK"