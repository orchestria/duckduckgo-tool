# /// script
# requires-python = "~=3.12"
# dependencies = ["duckduckgo-search"]
# ///


import json
import sys

from duckduckgo_search import DDGS
from duckduckgo_search.exceptions import (
    DuckDuckGoSearchException,
    RatelimitException,
    TimeoutException,
)


def search():
    args = sys.argv[-1]
    data = json.loads(args)
    if "query" not in data:
        raise ValueError("TODO")
    query = data["query"]
    duck = DDGS()
    try:
        answers = duck.answers(keywords=query)
    except RatelimitException as e:
        raise e
    except TimeoutException as e:
        raise e
    except DuckDuckGoSearchException as e:
        raise e

    print(json.dumps([a["text"] for a in answers]))


if __name__ == "__main__":
    search()
