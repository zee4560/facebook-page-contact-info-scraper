thondef clean_text(text):
"""Remove unnecessary spaces or special characters."""
return ' '.join(text.split()).strip()