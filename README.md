# Seed-based Weakly Supervised Named Entity Recognization

## Required Packages and Softwares
Auto Phrasing, CatE, skweak, Sklearn, Spacy, SciSpacy, BOND

## Data
Related data: <br>
[Texts](https://drive.google.com/file/d/1mHpSWhg5df_UzOChAB4RgNuqp0vOrXjf/view?usp=sharing) containing 12k articles. <br>
[Seeds](https://drive.google.com/file/d/1GYjXaxPXT7zZHinnZRR4bSrTO3Wj6zef/view?usp=sharing) list generated from CatE. <br>
Spacy format data can be found [here](https://drive.google.com/file/d/1XY6fgM4vCtbLEzjI7pPDwnj9F3VEEej3/view?usp=sharing) and IOB format data can be found in [IOB_scripts](https://github.com/Sherryhh/NER-CORD19/tree/main/IOB_scripts) and [BOND_training_scripts](https://github.com/Sherryhh/NER-CORD19/tree/main/Bond_training_scripts).

## Model
Spacy model en_ner_bc5cdr_md could be installed using pip inside the notebook or download [here](https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_bc5cdr_md-0.4.0.tar.gz). <br>
Modified en_ner_bc5cdr_md model that was trained with custom entity type can be download [here](https://drive.google.com/file/d/1Hn-KT0ErMbz5iGPfv6nFTJdMQet5wF3I/view?usp=sharing). <br>
BOND model can be found [here](https://drive.google.com/file/d/1oJGnfq34qzZZ3MskL_RzEi8BlZP2aopc/view?usp=sharing). <br>

## Code
### Data Processsing
Use `utils.py` to extract body texts from Covid19 JSON files: <br>
> python3 utils.py

To generate indice for seeds in the raw text, uncomment the last in `utils.py`. <br>

To run AutoPhrase for phrase mining, you can either download the [AutoPhrase](https://github.com/shangjingbo1226/AutoPhrase) repository or download the [CatE](https://github.com/yumeng5/CatE) repository which contains a copy of AutoPhrase. <br>
> ./auto_phrase.sh

To run CatE for seed set expansion, download the [CatE](https://github.com/yumeng5/CatE) repository. <br>
Place `run_CatE.sh` in the root folder of CatE. <br>
> ./run_CatE.sh

### Baseline
To test results with en_ner_bc5cdr_md directly: <br>
> base.ipynb

To test results with re-trained model or re-training en_ner_bc5cdr_md with custom entity types: <br>
> baseline.ipynb

### BOND
To covert Spacy format date to IOB format: <br>
> IOB_scripts/spacy_form_to_iob.ipynb

To train/test results for BOND: <br>
> Bond_training_scripts/Google_Colab_Train_BOND.ipynb

## Results

|                        | CORONAVIRUS | EVOLUTION | WILDLIFE | PHYSICAL_SCIENCE | LIVESTOCK | SUBSTRATE | LOCATION | IMMUNE_RESPONSE | MATERIAL | OVERALL |
|:----------------------:|:-----------:|:---------:|:--------:|:----------------:|:---------:|:---------:|:-------: |:---------------:|:--------:|:-------:|
| Baseline  w/o training |    15.31    |     -     |     -    |         -        |     -     |     -     |    -     |      15.31      |     -    |   17.5  |
|  Baseline w/ training  |    36.85    |   54.32   |   49.61  |       73.11      |   33.20   |   40.34   |  33.66   |      62.83      |   50.02  |  48.22  |
|      BOND Stage I      |    89.79    |   74.01   |   19.17  |       14.52      |   58.63   |   52.64   |  35.93   |      48.31      |   37.38  |  47.82  |
|      BOND Stage II     |    91.02    |   81.11   |   75.86  |       32.69      |   75.07   |   81.10   |   69.76  |      83.67      |   40.00  |  70.03  |
