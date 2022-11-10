from re import compile, sub

CLEAN_TAG = compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

def clear_html_tags(raw_string: str) -> str:
    """Returns a string cleaned of HTML tags. For example, "<h1>Okayeg</h1>" will return "Okayeg".
    """

    return sub(CLEAN_TAG, '', raw_string)
