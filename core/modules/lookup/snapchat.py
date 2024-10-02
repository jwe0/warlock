def search(data, bs):
    soup = bs(data, "html.parser")
    title = soup.find("title")
    if title:
        return title.text

    return ""