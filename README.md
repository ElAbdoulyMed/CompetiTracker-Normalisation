 ## Installation
```bash
git clone https://github.com/ElAbdoulyMed/CompetiTracker-Normalisation.git
pip install -r requirements.txt
```
## Usage
Put the input file inside `./data/raw` under the name `CompetiTracker.products.json` .

There's already a sample file .

MongoDB database should be named `CompetiTracker` .
```bash
python main.py
```
Data base will be updated by adding cleaned_ref & uniform_name for each product .
