
# Paper 30:

## Paper Title: MLOps Automation – Developing a RESTful API for Text Based Emotion Detection

## Authors: 
- Yusuf Omeiza Ahmed
- Marko Manyang Monydit
- Abhilasha Sharma

## Publication Year: 2022

## Source/Conference/Journal: 2022 Fourteenth International Conference on Contemporary Computing (IC3-2022), Noida, India

## Abstract/Introduction Summary:
The paper introduces an algorithm for detecting emotions from text using logistic regression. The authors developed a RESTful API to bridge the gap between the client device and the trained model, emphasizing the importance of Machine Learning Operations (MLOps) in the process.

## Motivation:
- To address the gap in text-based emotion detection compared to other forms like facial expressions and speech.
- The rising influence of social media and blogs as rich sources of emotional information.
- The desire for continuous integration and delivery in ML models to allow adjustments to changing trends.

## Tools:
- OS Environment: Windows 10 Pro
- Programming Languages: Java and Python
- Sklearn, Numpy, Pandas
- Maven, Git, Docker
- Selenium, Junit5
- SpringBoot, Google Colab
- Postman
- Amazon SageMaker (mentioned for monitoring purposes)
  
## Benefits:
- Improved repeatability of workflows and models.
- Enhanced developer productivity.
- Auditability by creating clear audit trails.
- Reliable machine learning solutions through continuous integration and delivery.
- Scalability with cloud resources.

## Metrics:
- Confidence score ranging from 0 (least accurate) to 1 (most accurate) for emotion detection.

## Approaches:
- Implemented logistic regression classification algorithm.
- Emotion detection based on keyword spotting and contextual analysis.
- Tokenization of input text.
- Identification of emotional words.
- Analysis of word intensity.
- Model training and evaluation using sklearn's pipeline.

## Challenges:
- Variations in the accuracy of detected emotions compared to human interpretations.
- Determining emotional indicators due to the model's lack of linguistic information.
- Relatively small dataset used for training the model.

## How to implement responsible AI methods:
The paper does not provide explicit strategies or methods regarding responsible AI. However, it emphasizes the importance of continuous monitoring, training, and validation to ensure the model's accuracy and reliability.

## Reviewer's Comments:
The paper presents a compelling approach to emotion detection from textual data, emphasizing the importance of MLOps in developing, deploying, and maintaining such models. The logistic regression-based solution combined with a RESTful API showcases the potential of combining traditional ML techniques with modern operational paradigms. However, future work should focus on expanding the dataset and incorporating more linguistic context to improve accuracy.
