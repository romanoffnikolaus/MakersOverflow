def filter_text(body: str) -> str:
    with open('questions/forbidden_words.txt') as forbidden_words:
        bad_words = forbidden_words.read().split()
        lower_text = body.lower()
        for word in bad_words:
            quantity = lower_text.count(word)
            if word in lower_text:
                for iteration in range(quantity):
                    start = lower_text.find(word)
                    lower_text = lower_text.replace(word, '*' * len(word), 1)
                    body = body.replace(
                        body[start:start + len(word):], '*' * len(word))
    return body
