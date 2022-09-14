# Drawing-Detection Using Yolo V5

## Introduction
The aim of this project is to detect the drowning person in swimming area and alarm the authority for timely rescue.

## Dataset
[Lifeguard](https://www.youtube.com/c/LifeguardRescue/videos) Rescue dataset was used for the drowning detection project. Lifeguard dataset was collected from YouTube that was basically based on the recorded video dataset of swimming pool. The details of the used dataset are following:
- Lifeguard Dataset (YouTube)
- Swimming Pool recorded videos
- Video Length: 1-2 minutes

## Preprocessing
The preprocessing steps of the proposed project are following:
- Extract Image Frames from Videos
- Annotate the Extracted Image Frame
- Annotation Criteria
  - Drowning (If Object Body is in Water up to Neck)
  - Not Drowning (If Object Body is in Water below the Neck)

## Model Training 
For the drowning detection during the swimming, Yolo V5 model was trained with the annotated images. The details of the model training are following:
- Use 250 Annotated Images

## Results
- Use 30 Annotated Samples for Evaluation
- Calculate Mean Absolute Error (MAE)
- Got 2.3567 value of MAE for validation samples

## Demo
![test1](https://user-images.githubusercontent.com/46160584/179975737-45beea2d-f74b-48c5-8d5f-fa90cfcc15be.jpg)

## Documentation
Access the Prepared Dataset and Report from [here](https://drive.google.com/drive/folders/11Os8-cJAMkViD45833Gy4bAO3IUz2etR?usp=sharing)
