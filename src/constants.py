"""Constants used in GatorMiner."""
import os

# Gradle report
REPORT_ID = "userID"
REPORT_REFLECTION = "reflection"
REPORT_ASSIGNMENT = "assignment"
REPORT_KEYS = (REPORT_ASSIGNMENT, REPORT_REFLECTION)


# Extensions
JSON_EXT = ".json"
PYTHON_EXT = ".py"
TXT_EXT = ".txt"
MD_EXT = ".md"

# Dataframe
TOKEN = "tokens"
NORMAL = "normalized"
ASSIGNMENT = "assignment"
SENTI = "sentiment"
COMBINED = "combined"

# Columns
POSITIVE = "Positive words"
NEGATIVE = "Negative words"

# Path
IMG_DIR = f"resources{os.path.sep}images"

# Style
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid \
#e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">\
{}</div>"""
