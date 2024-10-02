def search(data, bs):
    soup = bs(data, "html.parser")
    h1_title = soup.find("h1", class_="profile-test")
    if h1_title:
        return h1_title[0].text

    return ""