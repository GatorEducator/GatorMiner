"""Text summary"""
import logging
from typing import Dict, List
from gensim.summarization import summarize
from . import markdown as md


logging.basicConfig(
    format="[%(asctime)s]{%(pathname)s:%(lineno)d}\n\
%(levelname)s: %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.WARNING,
)


def summarize_text(text: str) -> str:
    """Uses gensim's summarization to summarize the given text """
    return summarize(text, word_count=30)


def summarizer(directory: str) -> Dict[str, List[str]]:
    """A summarizing pipeline"""
    main_md_dict = md.collect_md(directory)
    del main_md_dict["Reflection by"]
    # initialize summarized dict with keys in sources
    summarized = {k: [] for k in main_md_dict.keys()}
    for key, values in main_md_dict.items():
        for item in values:
            try:
                summarized[key].append(summarize_text(item))
            except ValueError as err:
                logging.warning(f"Cannot summarize text: {err}")
    return summarized
