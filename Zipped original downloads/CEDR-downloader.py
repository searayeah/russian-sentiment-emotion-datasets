from datasets import load_dataset
for name in ["main", "enriched"]:
    dataset = load_dataset("cedr", name=name)
    for split in ["train", "test"]:
        data = dataset[split]
        data.to_csv(f"cedr-{name}-{split}.csv")