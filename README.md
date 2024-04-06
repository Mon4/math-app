# A mobile math learning app for elementary school using machine learning to recognize handwritten answers
The app is based on [window app](https://github.com/Mon4/python-educational-program) which I've made earlier in python.
 
## Android app in Java
You can change settings or start game. An app consists of three game modes: operation, areas and text task to choose.
<img src="https://github.com/Mon4/Math-project/assets/44522588/9fe92310-6a2f-4ee2-8ade-ae080dbb4415" width="300" height="600" />
<img src="https://github.com/Mon4/Math-project/assets/44522588/e1ab1b2e-1979-4eb0-a382-ab42f6e4d198" width="300" height="600" />
</br>

In the settings, you can choose the difficulty level. The difficulty lies in the range of numbers. The more difficult the difficulty level, the larger the numbers we have to count.

<img src="https://github.com/Mon4/Math-project/assets/44522588/34ed96c3-6fa3-48ff-8ec3-d9379ca84597" width="300" height="600" />
</br>

 When the answer is right, the user is informed of the right answer and receives points in the upper left corner. When the answer is wrong, the user is informed about the correct answer.
When button "Wyślij" is pressed app sends query to server where is model to recognizing digits and app displays under task question the recognized number. When button "Sprawdź" is pressed, app checks if recognized number equals counter number by app - if answer of user is right.

Example of operational mode:

<img src="https://github.com/Mon4/Math-project/assets/44522588/fb115384-a993-4a45-aee0-0ee75746b4de" width="300" height="600" />
<img src="https://github.com/Mon4/Math-project/assets/44522588/923c636d-05ea-4159-aca6-75ad4ddfadb9" width="300" height="600" />
</br>

There is also an option to clear the paint view by pressing the "Wyczyść" button. And also, if the user does not want to answer a specific question, he can press the "Następny" button to move to the next question. This increases the number of questions viewed in the left corner. 

Example of fields mode:

<img src="https://github.com/Mon4/Math-project/assets/44522588/11131898-2e64-4748-a551-92f99151babb" width="300" height="600" />
</br>

Example of text tasks:

<img src="https://github.com/Mon4/Math-project/assets/44522588/df97e9f0-2121-43cc-9253-ff15a901343d" width="300" height="600" />
</br>

## Tasks generator
The program takes the paths of txt files which contains task description. The files for the operations contain equations using x, y and z variables, e.g. x+y+z, for which the values are randomized each time.

For text tasks, the input file provides the contents of the tasks, which are displayed to the user, as well as the actions by which the computer can calculate the correct answer. By randomizing the variables x, y, z, a large number of tasks can be easily created. It is also possible for the user to easily add new tasks.

![171944830-4563842d-f4ca-474d-b9e8-a0507b8d8fc7](https://github.com/Mon4/math-project/assets/44522588/56e95a9f-68ac-4fa9-88d8-6c2de195bfcc)



## Digit recognition - model in Python
MLP model to recognize handwritten digits based on the MNIST dataset. I've used mainly python and tensorflow library. Also I used flask to set up ml model on the server.

Building 1 hidden layer model with flatten input data (28x28 images) and 10 output digits. Using softmax in hidden layer and ReLU in output.

sample input data: 

<img src="https://github.com/Mon4/Math-project/assets/44522588/13fedefd-8824-4fff-9ee8-b71890731598" width="800" height="500" />
</br>

Accuracy and loss function:

<img src="https://github.com/Mon4/Math-project/assets/44522588/ba38ca70-b30e-4b69-a234-974cfba80010" width="800" height="500" />
</br>
Baseline Error: 1.77%
