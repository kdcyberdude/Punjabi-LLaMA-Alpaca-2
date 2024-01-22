from datasets import load_dataset
ds = load_dataset("uonlp/CulturaX",
                  "pa", split='train', cache_dir='../../../data/datasets/punjabi_ds', streaming=True)

for batch in ds.iter(batch_size=800000):
    with open('../../../data/datasets/punjabi_ds/punjabi_ds.txt', 'w') as f:
        for ex in batch['text']:
            f.write(ex + '\n\n')
    break
