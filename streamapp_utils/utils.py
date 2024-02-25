
def get_vars(session, *args: str, starts_with: str):
    if starts_with:
        add_vars = tuple(
            filter(lambda i: i.startswith(starts_with), session.keys())
            )
        args += add_vars
    vars = dict(filter(lambda i: i[0] in args, session.items()))
    return vars


def page_selector(session, page_key: str, page_options: dict):
    from streamlit import markdown
    page = page_options.get(
        session.get(page_key)
    )
    if callable(page):
        page()
    else:
        markdown('# Select an option!!! ⬆️')
    return


def clear_enviroment(session, *args: str):
    for i in args:
        variables = list(get_vars(session=session, starts_with=i).keys())
        for i in variables:
            del session[i]


def get_chunks(data: list, chunk_size: int = 1) -> list[list]:
    chunks = [
        data[x:x+chunk_size] for x in range(
            0,
            len(data),
            chunk_size
        )
    ]
    return chunks
