def search(data, bs):
    soup = bs(data, "html.parser")
    h1_ = soup.find("h1", class_="text-5xl font-bold text-center sm:pb-4 tooltip flex justify-center items-center")
    if h1_:
        return h1_[0].text
    return ""