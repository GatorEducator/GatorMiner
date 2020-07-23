"""Text summary"""
import logging
from typing import Dict, List
from gensim.summarization import summarize
from . import markdown as md


logging.basicConfig(
    format="[%(asctime)s]{%(pathname)s:%(lineno)d}\n\
%(levelname)s: %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.ERROR,
)


def summarize_text(text: str) -> str:
    """Uses gensim's summarization to summarize the given text """
    summarized = ""
    try:
        summarized = summarize(text, word_count=30)
    except ValueError as err:
        logging.warning(f"Cannot summarize text: {err}")
    except TypeError as err:
        logging.warning(f"Cannot summarize text: {err}")
    return summarized


def summarizer(directory: str) -> Dict[str, List[str]]:
    """A summarizing pipeline"""
    main_md_dict = md.collect_md(directory, is_clean=False)
    del main_md_dict["reflection by"]
    # initialize summarized dict with keys in sources
    summarized = {k: [] for k in main_md_dict.keys()}
    for key, values in main_md_dict.items():
        for item in values:
            try:
                summarized[key].append(summarize_text(item))
            except ValueError as err:
                summarized[key].append("")
                logging.warning(f"Cannot summarize text: {err}")
    return summarized
