def clean_school_email(email: str) -> str:
    name = email.split("@")[0].replace(".", "_")
    for d in "0123456789":
        name = name.replace(d, "")
    return name

clean_school_email("stefanos2343@stcats.gr")