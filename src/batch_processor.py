"""Batch processor that splits work into chunks for parallel execution."""

from config_loader import load_batch_config


def get_batch_count(total_items, config=None):
    """Calculate how many batches are needed to process all items.
    
    Bug: Does not validate that batch_size > 0 before dividing.
    When config is missing 'batch_size', config_loader returns 0,
    causing ZeroDivisionError here.
    """
    settings = load_batch_config(config)
    batch_size = settings["batch_size"]
    batch_count = (total_items + batch_size - 1) // batch_size  # ZeroDivisionError
    return batch_count


def process_items(items, config=None):
    """Process a list of items in batches.
    
    Entry point that triggers the bug when config has no batch_size key.
    """
    total = len(items)
    num_batches = get_batch_count(total, config)

    results = []
    settings = load_batch_config(config)
    batch_size = settings["batch_size"]

    for i in range(num_batches):
        batch = items[i * batch_size : (i + 1) * batch_size]
        results.append({"batch": i + 1, "items_processed": len(batch)})

    return results


if __name__ == "__main__":
    # Bug trigger: no batch_size in config, so config_loader defaults it to 0
    tasks = ["task1", "task2", "task3", "task4", "task5"]
    result = process_items(tasks, config={"max_retries": 5})
    print(result)
