# distilgpt2-finetuned-microbiology

## Model description

Small model for language modeling based on [distilgpt2](https://huggingface.co/distilgpt2) and on microbiology-related text data.
It achieves the following results on the evaluation set:
- Loss: 2.1073


## Intended uses & limitations

This model was finetuned solely for academic purposes, specifically:

- Notes enhancement
- Study
- Research

Keep in mind that the model itself does not always provide correct informtion, so **always** double check everything.

_distilgpt2-finetuned-microbiology_ must not be used for medical/health purposes, as it was not trained for that.

Besides the limitations already highlighted for distilgpt2, _distilgpt2-finetuned-microbiology_ was trained on a small microbiology-related texts dataset, so its knowledge is not nearly as comprehensive as many other sources of information. It is still useful when employed as _assistant_, not as substitute of human researchers/experts.  

## Training and evaluation data

Training data were taken from [Biology dataset on HuggingFace](https://huggingface.co/datasets/andersonbcdefg/biology), and microbiology texts were extracted from the `.parquet` file associated with this dataset, following this workflow:

### Data preprocessing and extraction

```bash
# UNZIP LARGE DATA FILES
gzip -d data/*.gz
# CONVERT .parquet FILE TO .jsonl
python3 scripts/parquet_to_jsonl.py
# FILTER MICROBIOLOGY TEXTS FROM microbiology.jsonl
python3 scripts/data_preprocess.py
```


## Training procedure
Training procedure is as descripted by this [HuggingFace notebook](https://github.com/huggingface/notebooks/blob/main/examples/language_modeling.ipynb). 

You only have to run this command, once you preprocessed and extracted everything.
```bash
#GENERATE MODEL
python3 scripts/build_distilgpt2-finetuned-microbiology.py
```

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 364  | 2.2399          |
| 2.4867        | 2.0   | 728  | 2.1351          |
| 2.213         | 3.0   | 1092 | 2.1073          |


### Framework versions

- Transformers 4.38.1
- Pytorch 2.1.0+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
- accelerate 0.27.2
- scikit-learn 1.2.2
- huggingface_hub 0.20.3

## Use the model in python

Here is a snippet code on how to load the model in python:

model_checkpoint = "as-cle-bert/distilgpt2-finetuned-microbiology"

```python3
# Load necessary dependencies
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForCausalLM.from_pretrained(model_checkpoint)
```


## References
- [HuggingFace notebook](https://github.com/huggingface/notebooks/blob/main/examples/language_modeling.ipynb) - template for building _distilgpt2-finetuned-microbiology_
- [Biology dataset on HuggingFace](https://huggingface.co/datasets/andersonbcdefg/biology) - microbiology texts were extracted from the `.parquet` file associated with this dataset and put in [microbiology.jsonl](./data/microbiology.jsonl)
