# %%
full_dataset = [
    {"name": "Peach", "items": ["green shell", "banana", "green shell"], "finish": 3},
    {"name": "Peach", "items": ["green shell", "banana", "green shell"], "finish": 1},
    {"name": "Bowser", "items": ["green shell"], "finish": 1},
    {"name": None, "items": ["green shell"], "finish": 2},
    {"name": "Bowser", "items": ["green shell"], "finish": 1},
    {"name": None, "items": ["red shell"], "finish": 1},
    {"name": "Yoshi", "items": ["banana", "blue shell", "banana"], "finish": 7},
    {"name": "DK", "items": ["blue shell", "star"], "finish": 1},
]


# %%
def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # print(racer)
        # We're only interested in racers who finished in first
        if racer["finish"] == 1:
            for j in racer["items"]:
                # Add one to the count for this item (adding it to the dict if necessary)
                if j not in winner_item_counts:
                    winner_item_counts[j] = 0
                winner_item_counts[j] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer["name"] is None:
            print(
                "WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                    i + 1, len(racers), racer["name"]
                )
            )
    return winner_item_counts


print(best_items(full_dataset))

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
plt.plot(x)

plt.show()
# deneme

# %% [markdown]
#

