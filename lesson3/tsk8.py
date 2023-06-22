items = {
    "John": {"bag", "fork", "axe"},
    "Mike": {"bag", "bread", "knife"},
    "Mary": {"bag", "rice", "fork"},
    "Mery": {"bag", "rice", "fork", "sword"},
}


def get_all_items(d: list):
    if len(d) == 1:
        return d[0]
    else:
        return d[0] | (get_all_items(d[1:]))


def get_unique_items(d: dict):
    tmp_dict = {key: d[key].copy() for key in d.keys()}
    tmp_item = set()
    for main in tmp_dict.keys():
        for other in tmp_dict.keys():
            if main == other:
                continue
            for item in tmp_dict[main] & tmp_dict[other]:
                tmp_item.add(item)
    for person in tmp_dict.keys():
        for item in tmp_item:
            tmp_dict[person].discard(item)
    return tmp_dict


def get_somebody(d: dict):
    for item in get_all_items(list(d.values())):
        character = None
        for person in d.keys():
            if item in d[person]:
                continue
            if not (item in d[person]) and (character is None):
                character = person
                continue
            if not (item in d[person]) and (character is not None):
                character = None
                break
        if character is not None:
            print(f"{character} единственный(ая) не взял(а) {item}")


print(f"Друзья взяли: {', '.join(get_all_items(list(items.values())))}")
print()
print("Уникальные вещи взятые кем-то одним")
unique = get_unique_items(items)
for key in unique.keys():
    if not unique[key]:
        continue
    print(f"\t{key} взял(а): {', '.join(unique[key])}")
print()
get_somebody(items)
