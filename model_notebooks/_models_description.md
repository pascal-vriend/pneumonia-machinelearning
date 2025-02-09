## Adult Models

Adult Model V0
- First attempt, not working properly

Adult Model V1
- First working notebook
- Derives small training and testing data from directories already seperated in /train and /test

Adult Model V2
- Uses an own custom CNN model and preprocesses data itself by resizing and normalizing colors
- Derives small training and testing data from directories already seperated in /train and /test
- Test set reached about 80% accuracy

Adult Model V3
- Uses ResNet model and preprocessed data
- Takes all as input and divides them to train and test sets
- Trained on UTwente Jupyter GPU server, test set reached 60% accuracy

Adult Model V4
- Combination of V2 and V3 but now on all data
- Trained on UTwente Jupyter GPU server, test set reached 70% accuracy

Adult Model V5
- Uses correct preprocessed x-rays
- Trained on UTwente Jupyter GPU server, test set reached 71% accuracy

***

## Pediatric Models
Pediatric Model Without Transfer
- modelv5.1.pth used to initialize weights (so custom CNN model)
- Model used immediately to predict labels and compute metrics (no training)
- Reached accuracy of 50%

Pediatric Model Without Initialization
- Same custom CNN model is used, but weights are not loaded from adult dataset
- Model trained from scratch

Pediatric Model Without Initialization K-Fold:
- Same as above but now using K-Fold
- About 81% accurate

Pediatric Model:
- modelv5.1.pth used to initialize weights (so custom CNN model)

Pediatric Model K-Fold:
- Same as above but now using K-Fold
- About 84% accurate

***

## Mixed Model

Mixed Adult Pediatric Model:
- Both adult and pediatric data loaded
- Dynamic sampler that increased pediatric weight throughout training
- Reached accuracy of 67%
