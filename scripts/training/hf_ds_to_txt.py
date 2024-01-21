from datasets import load_dataset
ds = load_dataset("uonlp/CulturaX",
                  "ta", split='train', cache_dir='../../../data/datasets/tamil_2l', streaming=True)

for batch in ds.iter(batch_size=200000):
    with open('../../../data/datasets/tamil_2l/tamil_2l.txt', 'w') as f:
        for ex in batch['text']:
            f.write(ex + '\n\n')
    break


