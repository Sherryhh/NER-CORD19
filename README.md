# Seed-based Weakly Supervised Named Entity Recognization

## Required Packages and Softwares
Auto Phrasing, CatE, skweak, Sklearn, Spacy, SciSpacy, BOND

## Data
Related data can be found ...[data](some link)

## Model
Spacy model en_ner_bc5cdr_md could be installed using pip inside the notebook or download [here](https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_bc5cdr_md-0.4.0.tar.gz). <br>
Modified en_ner_bc5cdr_md model that was trained with custom entity type can be download [here](https://drive.google.com/file/d/1Hn-KT0ErMbz5iGPfv6nFTJdMQet5wF3I/view?usp=sharing). <br>
BOND model can be found ...[](some link). <br>

## Code
### Data Processsing
To be filled 

### Baseline
To test results with en_ner_bc5cdr_md directly: <br>
> base.ipynb

To test results with re-trained model or re-training en_ner_bc5cdr_md with custom entity types: <br>
> baseline.ipynb

### BOND

## Results

|                        | CORONAVIRUS | EVOLUTION | WILDLIFE | PHYSICAL_SCIENCE | LIVESTOCK | SUBSTRATE | COUNTRY | IMMUNE_RESPONSE | MATERIAL | OVERALL |
|:----------------------:|:-----------:|:---------:|:--------:|:----------------:|:---------:|:---------:|:-------:|:---------------:|:--------:|:-------:|
| Baseline  w/o training |    15.31    |     -     |     -    |         -        |     -     |     -     |    -    |      15.31      |     -    |   17.5  |
|  Baseline w/ training  |    36.85    |   54.32   |   49.61  |       73.11      |   33.20   |   40.34   |  33.66  |      62.83      |   50.02  |  48.22  |
|      BOND Stage I      |             |           |          |                  |           |           |         |                 |          |         |
|      BOND Stage II     |             |           |          |                  |           |           |         |                 |          |         |
