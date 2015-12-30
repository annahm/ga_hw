## Class 9 Pre-work: Bias-Variance Tradeoff

Read this excellent article, [Understanding the Bias-Variance Tradeoff](http://scott.fortmann-roe.com/docs/BiasVariance.html), and be prepared to **discuss it in class**.

**Note:** You can ignore sections 4.2 and 4.3.

Here are some questions to think about while you read:
* Q: In the Party Registration example, what are the features? What is the response? Is this a regression or classification problem?
  - A: Features are wealth and religiousity.  Response is party affiliation (R/D).  This is a classification problem.
  [The features are wealth and religiousness. The response is voter party registration. This is a classification problem.]
* Q: Conceptually, how is KNN being applied to this problem to make a prediction?
  - A: Using euclidean distance points based on religiosity and wealth measures to find K nearest neighbors to a point.  The 
  prediction is based on majority responses of training data.  What measures and metrics are used to gauge this?  How do you
  measure religiosity?  How do you normalize the measures between wealth and religiousness.
  [Find the K most similar voters in the training data (in terms of wealth and religiousness), and use the majority party registration among those "neighbors" as the predicted party registration for the unknown individual.]
* Q: How do the four visualizations in section 3 relate to one another? Change the value of K using the slider, and make sure you understand what changed in the visualizations (and why it changed).
  - A: The first is just a 2D x-y plot of religiousness to wealth with labels/response in Red or Blue.  This shows us non-linear.
    Hence we choose KNN as a possible model to fit the data.  The second is a model using kNN w/ k=1.  Notice that there is one
    neighborhood for each data point.  The third shows for each point the 6-nearest neighbors (k=6 or whatever k is set to in
    the slider) from the training set for new test data and the resulting prediction.
    The fourth shows what the predictions would be for a range of k values.  
    ? It is not clear to me how the black line boundary was generated -- how do they know that this is the best-fit model?
    What was used to generate this model - it doesn't seem like kNN to me??
    [* First viz: training data colored by response value. Second viz: classification map for K=1. Third viz: out-of-sample data colored by predicted response value, and identification of the neighborhoods used to make that prediction. Fourth viz: predicted response value for each hexagon. Changing K changes the predictions in the third and fourth viz]
    
* Q: In figures 4 and 5, what do the lighter colors versus the darker colors mean? How is the darkness calculated?
  - A: The darker the color, the higher the confidence, in this case the percentage of neighbors.  IF it is 50/50, then white.
    [*Darkness indicates confidence in the prediction, and is calculated using the proportion of nearest neighbors that have the same response value.]
* Q: What does the black line in figure 5 represent? What predictions would the best possible machine learning model make, with respect to this line?
  - A: I understand from the paper that this was the best fit model, but what was the measure for best fit, is that based on
    bias and variance measures?  Or least errors over the training set?  How was the model generated?
    [* The black line is the the underlying model that generated the training data. The best possible machine learning model would learn that line as its decision boundary. It would not be a perfect model, but it would be the best possible model.]
* Q: Choose a very small value of K, and click the button "Generate New Training Data" a number of times. Do you "see" low variance or high variance, and low bias or high bias?
  - A: Low k is high variance, but low bias.  Overfitting problem.
    [* High variance, low bias]
* Q: Repeat this with a very large value of K. Do you "see" low variance or high variance, and low bias or high bias?
  - A: High k is low variance high bias.  Underfitting problem.
    [* Low variance, high bias]
* Q: Try using other values of K. What value of K do you think is "best"? How do you define "best"?
  - A: Model I thought was best fit was around 35-37.  The way I looked at it was least number mis-classified.  What is the
    way to measure a best fit? Is it least errors across the entire training set?  
    [* A value of K in the middle is best. The best value is the value that results in a model whose predictions most consistently match the decision boundary.]
* Q: Does a small value for K cause "overfitting" or "underfitting"?
  - A: Overfitting (i.e. high variance)
    [* Overfitting]
* Q: Why should we care about variance at all? Shouldn't we just minimize bias and ignore variance?
  - A: We care about variance because the model needs to be generalized enough to fit new data that is unexpected.
  How do we measure to optimize variance and bias?  Is it by plotting errors vs. complexity graph (e.g. Fig 6) so that errors 
  are minimzed?  Is that the way you do this across all models??
    [* If you had all of the possible data (past and future), a model with high complexity (and thus high variance) would be ideal because it would capture all of the complexity in the data and wouldn't need to generalize. But given that we only have a single sample of data, both bias and variance contribute to prediction error and should be appropriately balanced.]
