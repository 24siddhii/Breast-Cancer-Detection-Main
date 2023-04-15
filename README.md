# Breast-Cancer-Detection-Main

Breast cancer is the second leading cause of cancer-related deaths and the most diagnosed cancer in women across the world. There are some devices that detect breast cancer but many times they lead to false positives, which results in patients undergoing painful, expensive surgeries that were not even necessary. The early detection of breast cancer is one of the most prominent challenges.  Thus, a system that predicts the Breast cancer on the basis of medical images and textual data  by applying machine learning techniques is proposed in this project. 

OBJECTIVE:

The objective is to identify the presence of breast cancer as early as possible by using medical images and textual data . Early detection can lead to better treatment outcomes and higher chances of survival. Medical images, such as mammograms and ultrasound, can provide visual information about any abnormalities in breast tissue. Textual data, including various parameters of breast mass like radius_mean, smoothness_mean, textual_mean etc can provide additional information that may help identify patients who are at higher risk of developing breast cancer. Combining medical images and textual data improves the ability to identify patients for early interventions, resulting in better outcomes by detecting breast cancer at an early stage.


METHODOLOGY:

The flow of the system is divided into two parts , i.e, a database with textual and other with medical images. The textual data involves steps which includes data pre-processing, EDA and Feature Selection, normalization of data, and applying ensemble hard voting technique resulting in remarkable accuracy of 97.3%. On the other hand, with mammograms, pre-processing is performed by applying Sobel filter and Median filter , later comparing the accuracy of both by fitting into CNN model. The overall process of the proposed system is shown in Figure 1.
 

Figure 1: The Working Model of Proposed System

The voting is an ensemble method that combines the performances of multiple models to make predictions. In majority voting, the predicted class label for a particular sample is the class label that represents most of the class labels predicted by each individual classifier. Here, various ML algorithms to be used in voting techniques are: Support Vector Machine (SVM), K-Nearest Neighbor (KNN), Random Forest (RF) and Naïve Bayes (NB). Through ensemble technique, the system will combine the predictions of above-mentioned machine learning algorithms and with the help of hard/ majority voting technique, our system will aggregate predictions of each classifier and predict the class that gets the most votes. The results indicate that the Ensemble Voting approach is ideal as a predictive model for breast cancer, resulting in uniqueness of our system compared to the previous existing system. The overall accuracy of the proposed ensemble model is 97.3%.
On the other hand, with mammograms, pre-processing is performed by applying Sobel filter and Median filter. Afterwards, the median filtered images are fed in CNN architecture having 10 layers which includes Conv2D layer with 20 filters, BatchNormalization layer, MaxPooling2D layer with pool size of (2,2), Conv2D layer with 40 filters, MaxPooling2D layer with pool size of (3,3), Conv2D layer with 80 filters, MaxPooling2D layer with pool size of (5,5) , Flatten layer. Two Dense layers with 80 and 3 units, respectively., L2 regularization, and a Dropout rate of 0.5. 
Thus, landed up with an accuracy of 80%.
