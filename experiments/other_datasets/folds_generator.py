from sklearn.model_selection import StratifiedKFold
import glob
import pandas as pd

SEED = 42

for DATASET in ('hockey', 'movies', 'crowd'):

    violence = glob.glob(f'../datasets/{DATASET}_dataset/original_data/fight/*.avi', recursive=True)
    violence = ['/'.join(v.split('/')[-2:]) for v in violence]
    non_violence = glob.glob(f'../datasets/{DATASET}_dataset/original_data/nonfight/*.avi', recursive=True)
    non_violence = ['/'.join(v.split('/')[-2:]) for v in non_violence]

    X = violence + non_violence
    y = [1] * len(violence) + [0] * len(non_violence)
    folds = [0] * len(X)

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)

    for fold, (_, fold_index) in enumerate(skf.split(X, y)):
        for i in fold_index:
            folds[i] = fold

    pd.DataFrame({'video': X, 'label': y, 'fold': folds}).to_csv(f'../datasets/{DATASET}_dataset/folds.csv', index=False)
    print(f'Folds for {DATASET} dataset generated.')
