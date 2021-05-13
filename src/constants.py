"""Constants used in GatorMining"""
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
