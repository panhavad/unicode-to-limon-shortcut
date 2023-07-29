def checkSpecialException(text):
    if "ba" in text:
        text = text.replace("ba", ")a")
    if "¼" in text:
        text = text.replace("¼", ",")
    return text