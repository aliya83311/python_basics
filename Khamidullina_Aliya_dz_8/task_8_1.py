import re

# Version 1
# EMAIL_USERNAME = re.compile(r"[a-zA-Z0-9]+[_.-]*[a-zA-Z0-9]+")
# EMAIL_DOMAIN = re.compile(r"[a-z]+\.[a-z]{2,}")
#
#
# def validate_email(email):
#   names_domaines = {}
#   pattern = r"@"
#   temp = re.split(pattern, email, maxsplit=1)
#   if re.fullmatch(EMAIL_USERNAME, temp[0]) and re.fullmatch(EMAIL_DOMAIN, temp[1]):
#     names_domaines.setdefault("username", temp[0])
#     names_domaines.setdefault("domaine", temp[1])
#     return names_domaines
#   else:
#     raise ValueError ("Email is not valid")
#
#
# test_emails = ["someone@geekbrains.ru", "dfhshWR44_dfd@mail.ru", "kdhfkkjkj@yandexru"]
#
# temp = map(validate_email, test_emails)
# for item in temp:
#   print(item)


# Version 2
test_emails = ["someone@geekbrains.ru", "dfhshWR44_dfd@mail.ru", "someone@gmailcom"]

EMAIL = re.compile(r"(?P<username>[a-zA-Z0-9]+[_.-]*[a-zA-Z0-9]+)@(?P<domain>[a-z]+\.[a-z]{2,})")


def email_parse(address):
    match = re.search(EMAIL, address)
    if not match:
        raise ValueError("Email is not valid")
    return match.groupdict()


temp = map(email_parse, test_emails)
for item in temp:
    print(item)
