# GraghRAG

### Metadata

For entity answer:

```
metadata = {
    "chunks": indexes,
    "show": "Roderick on the Line",
    "episode": episode_number,
    "title": episode_title,
    "subject": entity,
    "category": labels,
    "tags": tags,
}
```

For chunk:

```
metadata = {
    "chunks": [chunk],
    "show": "Roderick on the Line",
    "episode": episode_number,
    "title": episode_title,
    "subject": [],
    "category": [],
    "tags": [],
}
```

```
"""
Alyeska

Location

Alaska, Alyeska, paper towels, ski resort

Here's what John and Merlin say about Alyeska:
* **Alyeska is the name of a ski resort where John grew up.**  He says it's a name you might want to give a dog or child, but not in Girdwood, Alaska.
* **In Girdwood, many dogs are named Alyeska and many are named Max** (after Mount Max's Mountain). John finds this strange and doesn't understand the trend.
* **John's cat is named Alyeska.** He says that if you named your dog Alyeska in Girdwood, they would bury you in a peat bog.
Let me know if you have any other questions about their conversation!

metadata: {
            "chunks":[5, 6, 7],
            "show":"Roderick on the Line",
            "episode":"389",
            "title":"The New March",
            "subject":"Alyeska",
            "Category":["Location","Person"]
            "tags":[
                    "Alaska", "Alyeska", "Girdwood", "Max"
                    ]
            }

id: rotl_398_Alyeska
"""
```
