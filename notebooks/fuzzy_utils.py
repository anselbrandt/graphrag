from rapidfuzz import process, fuzz


def group_similar_names(names, threshold):
    if not names:
        return []

    names = sorted(set(names))
    grouped = []
    used = set()

    for name in names:
        if name in used:
            continue

        matches = process.extract(
            name, names, scorer=fuzz.ratio, score_cutoff=threshold
        )
        group = [match[0] for match in matches if match[0] not in used]

        used.update(group)
        grouped.append(group)

    return grouped
