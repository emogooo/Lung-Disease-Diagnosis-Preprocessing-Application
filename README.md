# Lung Disease Diagnosis Preprocessing Application

This project involves the development of a data preprocessing application for an AI-supported lung disease diagnosis system. The application focuses on extracting the lung region from X-ray images, ensuring that the subsequent analysis is both accurate and efficient. By using advanced image processing techniques, the application identifies and crops the lung area, removing irrelevant parts of the image. This preprocessing step is crucial for enhancing the performance of AI models in diagnosing lung diseases such as pneumonia, tuberculosis, and lung cancer. The clean, focused images enable the AI to make more accurate predictions and diagnoses, ultimately improving patient outcomes.

## Pseudo Code:

![image](https://user-images.githubusercontent.com/58745898/190654275-56dc738d-96d7-4875-9073-84e577c7e297.png)

![image](https://user-images.githubusercontent.com/58745898/190654330-da304e38-95ca-4d18-9456-510f9a4cd33a.png)

![image](https://user-images.githubusercontent.com/58745898/190654374-1dfa31a8-9063-4f2d-ae7e-483d3ed2fb01.png)

![image](https://user-images.githubusercontent.com/58745898/190654407-ba1280dd-caec-49ef-a2f7-81fad145d0ab.png)

![image](https://user-images.githubusercontent.com/58745898/190654979-32ca0e15-4f11-421a-a593-a52a69dd19d3.png)



## The working steps are briefly as follows:

### X-ray Film Provided to the Algorithm:

![00004274_000](https://user-images.githubusercontent.com/58745898/190640588-9fbb80d3-eb1d-404d-9f92-66cf7db25183.png)

### 1. First, the film is converted to black and white with a high threshold value to detect text and symbols.

![a](https://user-images.githubusercontent.com/58745898/190641086-9acfc9f4-6987-41a7-92c3-b996c5fadb74.jpg)

### 2. The coordinates of the detected text and symbols on the film are painted black.

![BBBlogoveYazilarSiyahaBoyanir](https://user-images.githubusercontent.com/58745898/190644036-cac08058-fcf7-47c3-a5f4-c1ea242c4803.jpg)

### 3. The film is converted to black and white.

![CCCSiyahBeyazYapilir](https://user-images.githubusercontent.com/58745898/190644129-2c250ecb-255a-4211-b353-06e47661ec0a.jpg)

### 4. Blur is applied to the film.

![DDDBlurUygulanir](https://user-images.githubusercontent.com/58745898/190644183-148bcad7-ac4e-4992-98ab-84c2fd2d794d.jpg)

### 5. The blurred film is converted to black and white.

![EEEBlurlanmisFilmSiyahBeyazaCekilir](https://user-images.githubusercontent.com/58745898/190644402-7a1140f3-8e3a-4dcd-af73-a5c9356915f6.jpg)

### 6. The white pixels at the far left, far right, top, and bottom of the film are detected to determine the body's frame.

![GGGASDASDSADASDADSiyahBeyazaCekilmisResminEnYakinBeyazPikselleriBulunur](https://user-images.githubusercontent.com/58745898/190644517-d84e29b3-bca2-451f-b7d0-607dafb245b5.jpg)

### 7. The frame created in the previous step is overlaid onto the original image.

![FFFSiyahBeyazaCekilmisResminEnYakinBeyazPikselleriBulunur](https://user-images.githubusercontent.com/58745898/190644647-93b557d6-f10b-4594-934d-96bd12835ad2.jpg)

### 8. The frame is cropped from the original image, and the body image is prepared to be sent to the lung detection function.

![HBody](https://user-images.githubusercontent.com/58745898/190645001-51eebf3c-822e-43a0-b3b6-bf192556750a.jpg)

> [!NOTE]
> The lung detection function operates in three stages. The first stage attempts to find the entire lung by matching it with templates. If a full lung match is not found, the process moves to the second stage. In this stage, the left and right lungs are searched for separately. If the left lung is found, the right lung is then searched for. If both are found, the images are framed from their furthest coordinates to obtain the result. However, if either the left or right lung, or both, cannot be found, the process moves to the third stage. This stage searches sequentially for the upper left, lower left, upper right, and lower right parts of the lung. If all four corners are found, a frame is created from the furthest coordinates to obtain the lung image.

### 9. First Stage - Full Lung Matching

![JJJFullLung](https://user-images.githubusercontent.com/58745898/190649793-9c37dd5e-13e7-44c5-b347-97f1bcbbbc0d.jpg)

### 10. Second Stage - Left Lung Matching

![KKKLeftLung](https://user-images.githubusercontent.com/58745898/190649907-a12a8cc6-47d3-4452-8cd3-26591fbf4586.jpg)

### 11. Second Stage - Right Lung Matching

![MMMBothLung](https://user-images.githubusercontent.com/58745898/190650019-cfc8e916-d27f-46d0-9f7e-1d25dd2b166a.jpg)

### 12. Second Stage - Creating a Frame from the Furthest Points of Both Images and Cropping to Complete Lung Detection

![NNNBothFullLung](https://user-images.githubusercontent.com/58745898/190650202-61e6c1ad-a864-409e-8ea8-84eb059cdfb1.jpg)

### 13. Third Stage - Matching All Corners (Instead of adding a separate image for each corner, only the matching image for the last corner is included.)

![OOOCorners](https://user-images.githubusercontent.com/58745898/190650525-442aa1d9-0d83-4dc5-90a0-dde1a4e5b0b7.jpg)

### 14. Creating a Frame from the Furthest Points of the Four Images to Complete Lung Detection

![PPPCornersFull](https://user-images.githubusercontent.com/58745898/190650851-dfbf32bd-f908-4155-adc4-6df28b37b2fa.jpg)

### 15. Final Image

![RRRFinal](https://user-images.githubusercontent.com/58745898/190650917-dad02800-032f-412d-abeb-a2c87e09747d.png)

## As of ***16.09.2022***, the algorithm has been modified. The working principle and pseudo code of the old algorithm are provided below.
## The working steps are briefly as follows:

### X-ray Film Provided to the Algorithm:

![d](https://user-images.githubusercontent.com/58745898/158307662-107506fb-edaa-4460-bc8d-b9fd581bce2e.jpg)

### 1. First, the film is converted to black and white with a high threshold value to detect text and symbols.

![a](https://user-images.githubusercontent.com/58745898/158308128-d75a6b0e-536c-48ed-8690-fb02222c4288.jpg)

### 2. The coordinates of the detected text and symbols on the film are painted black.

![a](https://user-images.githubusercontent.com/58745898/158308404-fbe4cac4-c006-4db4-af32-628e9971674e.jpg)

### 3. Blur is applied to the film..

![a](https://user-images.githubusercontent.com/58745898/158308657-f52d49fd-6e06-45f0-a16f-e539cd3440af.jpg)

### 4. The blurred film is converted to black and white.

![a](https://user-images.githubusercontent.com/58745898/158308790-7b0e7d41-12b5-478f-aeca-6fb68fba7d00.jpg)

### 5. The white pixels at the far left, far right, top, and bottom of the film are detected to determine the body's frame. The image processed in step 4 is cropped from these frames and sent to the lung detection function.

![Adsız](https://user-images.githubusercontent.com/58745898/158309814-01622bc7-a118-4b30-83a1-a8c72a78d91b.png)

### 6. All the black pixels on the outside of the film are painted white.

![a](https://user-images.githubusercontent.com/58745898/158310148-6b933059-2b21-450f-8af2-fcaba122d0da.jpg)

### 7. The obtained image is blurred.

![a](https://user-images.githubusercontent.com/58745898/158310363-6233b803-7aee-4451-95af-0bf714084bb9.jpg)

### 8. The blurred image is converted to black and white to reveal the rib cage.

![a](https://user-images.githubusercontent.com/58745898/158310655-a8acfd73-15fc-4f3d-a1f7-13bf40d1c119.jpg)

### 9. The black pixels at the far left, far right, top, and bottom of the image are detected to determine the frame of the rib cage.

![a](https://user-images.githubusercontent.com/58745898/158311151-279416cb-d603-4041-bdcb-192be0719e2f.jpg)

### 10. The original image is cropped using these frames to obtain the desired image.

![a](https://user-images.githubusercontent.com/58745898/158311599-b0303496-4b32-46e7-ac5a-103e81cd8721.jpg)

### 11. Obtained Image:

![d-9079045](https://user-images.githubusercontent.com/58745898/158310672-3c56a853-088f-4295-a238-c712b75ca318.jpg)

## Pseudo Code:

* Start.

* Convert the image to black and white with a high threshold value (240/255). (a)

* Store the coordinates of the white pixels.

* Paint the pixels at these coordinates black in the original image. (b)

* Apply blur ((x/30), (y/15)) to the image and convert it to black and white with a normal threshold value (127/255). (c)

* Find the furthest white pixels in all four directions (up, down, left, right) and frame the image from these points.

* Crop the framed image to create a new image. (d)

* Paint the black pixels outside the new image white. (e)

* Apply a high amount of blur ((x/5), (y/5)) to the image and convert it to black and white with a normal threshold value (127/255). (f)

* Find the furthest black pixels in all four directions (up, down, left, right) in the new image and frame the image from these points.

* Crop the coordinates of the frame from the original image to obtain the lung image. (g)

* End.

### Parameters:
X = Horizontal length of the image (number of pixels)

Y = Vertical length of the image (number of pixels)

### Explanations:
X-ray films contain biomedical images as well as information such as the X-ray number, patient name, hospital, and doctor's name. To remove this information and reduce the margin of error during lung detection, the threshold value used in the initial black and white conversion is higher than normal.

The first blurring operation is to eliminate outlier pixels that can be considered noise on the X-ray film.

The second blurring operation is kept high to determine the coordinates of the corners of the lung. This prevents the imaging of non-lung entities (such as gas build-up in the abdomen, which appears darker and denser than the lungs, often seen in children).

![img](https://user-images.githubusercontent.com/58745898/183700555-40b4a4c8-7634-4e61-b859-77cf65a5073a.jpg)
