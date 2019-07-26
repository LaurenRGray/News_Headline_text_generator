# News Headline Text Generation Model

This project uses a LSTM neural network to create a generative model for text, which in this case is news headlines. 

## Data
The dataset used to train the network included both a [Kaggle dataset](https://www.kaggle.com/aashita/nyt-comments) and data retrieved using the New York Times API. 

## Methods
#### Step 1
The dataset was first cleaned, tokenized, and converted to sequences of n-grams. 

#### Step 2
These sequences were then used to train the network. I first used a simple LSTM network with the following architecture:
   - Input (Embedding) Layer : Takes the sequence of words as input, represented as dense vectors 
   - LSTM Layer : Hidden layer; computes the output using LSTM units (100 units in this case) 
   - Output (Dense) Layer : Dense layer; computes the probability of the best possible next word as the output

Note: the network was trained on AWS EC2 instance with GPU (as it will take a very long time to run on a local machine with CPU). 

#### Step 3: 
I then used the network to generate headlines. 

  Example result:
  
    Input: Donald Trump
    
    Output: Donald Trump Master of Low Expectations

## Next Steps
Future work will involve trying to improve the quality of model results by fine-tuning network architecture and parameters. For example, I will try:
- using a larger network
- increasing the input dimension in the embedding layer
- increasing the number of memory units in the LSTM layer(s)
- increasing the number of training epochs and decreasing the batch size
