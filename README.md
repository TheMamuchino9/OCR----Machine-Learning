## OCR----Machine-Learning
I learned about the Optical Character Recognition (OCR) capabilities of Azure Computer Vision. Using the Read Text functionality of Computer Vision, I was able to accurately extract both printed and handwritten text from images and documents

I used the optical character recognition (OCR) API to extract text from images. 

![image](https://user-images.githubusercontent.com/86535567/128938694-0a15789b-5597-478f-b37b-ae1f36e77e2a.png)

The image is of a street sign:

![image](https://user-images.githubusercontent.com/86535567/128938823-b94dcf1b-a4ad-4f3b-9a92-7268fee0217a.png)


#Read scanned documents

To use the Read API, I must send an image to the Computer Vision service and it will be read and analyzed asynchronously by the service. This means I must send follow-on requests to check the status of the operation and retrieve the results when processing is completed.


![image](https://user-images.githubusercontent.com/86535567/128939236-7585ba46-0c73-4281-87db-4836c5b7b754.png)

![image](https://user-images.githubusercontent.com/86535567/128939291-fe3dcb3b-6a0b-4412-99cb-0afab9d1517b.png)


## Read Handwritten Text

In addition to printed text, the `Read API` is also capable of reading handwritten text.

![image](https://user-images.githubusercontent.com/86535567/128939764-d77fc5a0-df30-420f-939a-fcb28464e9fa.png)

Results: 

![image](https://user-images.githubusercontent.com/86535567/128939792-a0e5c2b9-dc5f-4f69-9918-8958c3eefe77.png)






