# backend/app/utils.py

# Här kan vi lägga hjälpfunktioner!

# tar bort inledande nollor
# fyller ut med nollor framför
# ger fel för tom sträng, bokstäver och för stora tal
def normalize_message(message: str) -> str:
    result = message.strip()
    if not message:
        return "-"

    if len(message) > 20:
        raise ValueError("Message to long (max 999 characters)")

    return result.zfill(3)
