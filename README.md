# distilgpt2-finetuned-microbiology

## Description

Small model for language modeling based on Distil-GPT2 and on microbiology-related text data.

## Data preprocessing and extraction

```bash
# CONVERT .parquet FILE TO .jsonl
python3 scripts/parquet_to_jsonl.py

# FILTER MICROBIOLOGY TEXTS FROM microbiology.jsonl
python3 scripts/data_preprocess.py
```

## References

- [HuggingFace notebook](https://github.com/huggingface/notebooks/blob/main/examples/language_modeling.ipynb) - template for building _distilgpt2-finetuned-microbiology_
- [Biology dataset on HuggingFace](https://huggingface.co/datasets/andersonbcdefg/biology) - microbiology texts were extracted from the `.parquet` file associated with this dataset and put in [microbiology.jsonl](./data/microbiology.jsonl)
