def search(data, bs):
  name = ""
  email = ""
  results = {}
  soup = bs(data, "html.parser")

  title = soup.find("title")
  if title:
    name = title.text
    results["name"] = name

  a = soup.find_all("a", href=True)
  for link in a:
    if "mailto:" in link["href"]:
      email = link["href"]
      results["email"] = email

  return results


      