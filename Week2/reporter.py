# here this module takes in the loading of the data part.
def write_report(result, filename):
    total, unique_set, wrong_set, breakdown = result
    with open(filename, "w") as g:
        g.write("Pearl Review Report\n")
        g.write(f"Total reviews: {total}\n")
        g.write(f"Unique pearl reviews: {len(unique_set)}\n")
        g.write(f"Pearls needing review (wrong at least once): {wrong_set}\n")
        g.write(f"Difficulty breakdown: \n")
        for k, v in breakdown.items():
            g.write(f"  {k}: {v}\n")
