# DeepLearningMovieClassification
Final Project for DD2424

Our experiments on networks are organized into independent Notebooks, each with a different network:
- notebook: the original binary sentiment classfication starter
- parameterTests: testing various paramenters on the binary classifier network
- GRU: experiments adding GRU layers to multi-class network
- manyLayers: experiments on a network with many repeated Conv1D, MaxPooling1D, and LSTM layers 
- LSTM: BEST results! experiments adding one simple LSTM layer to multi-class network

More review and ratings data can be scraped from IMDB.com with the script in Webscraping, using the downloaded and sorted list of titles.

