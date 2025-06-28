# AI-Powered Math Learning Through Handwriting Recognition
This is a math learning app designed for children, with a unique feature: students can write their answers by hand. This not only helps them practice math but also improves handwriting skills. Unlike most similar apps, it uses machine learning to recognize handwritten input, making learning more natural and engaging.

 
## <img src="https://upload.wikimedia.org/wikipedia/commons/d/d7/Android_robot.svg" alt="Android" width="20"/> Android app in Java
You can easily customize settings or dive right into the game. The app offers three engaging and educational game modes: Operations (Działania), Areas (Pola), and Text Tasks (Tekstowe) — each designed to make math practice interactive, varied, and fun. This flexible structure allows kids to explore different types of challenges, keeping learning exciting and well-rounded.

<img src="https://github.com/Mon4/Math-project/assets/44522588/9fe92310-6a2f-4ee2-8ade-ae080dbb4415" width="300" height="600" />
<img src="https://github.com/Mon4/Math-project/assets/44522588/e1ab1b2e-1979-4eb0-a382-ab42f6e4d198" width="300" height="600" />
</br>

In the settings, user can select the desired difficulty level, which adjusts the range of numbers used in tasks. The higher the level, the larger and more challenging the numbers become — perfect for gradually building math skills and confidence.

<img src="https://github.com/Mon4/Math-project/assets/44522588/34ed96c3-6fa3-48ff-8ec3-d9379ca84597" width="300" height="600" />
</br>

When the answer is correct, the user is notified and earns points displayed in the top-left corner. If the answer is incorrect, the correct solution is shown for learning. After pressing **Send (Wyślij)**, the app sends the handwritten input to a server with a digit recognition model. The recognized number is then displayed below the task. Pressing **Check (Sprawdź)** compares the recognized number with the expected result to verify if the user's answer is correct.

### Example of operational mode:

This mode focuses on basic arithmetic operations like addition, subtraction, multiplication, and division. For instance: "12 × 3 =". The user writes the answer by hand, and the app uses machine learning to recognize and check it. It’s perfect for practicing quick mental math in an interactive way.

<img src="https://github.com/Mon4/Math-project/assets/44522588/fb115384-a993-4a45-aee0-0ee75746b4de" width="300" height="600" />
<img src="https://github.com/Mon4/Math-project/assets/44522588/923c636d-05ea-4159-aca6-75ad4ddfadb9" width="300" height="600" />
</br>

There is also a **Clean Up (Wyczyść)** button that allows users to clear the handwriting area and try again. If the user prefers to skip a question, they can press the **Next (Następny)** button to move forward. Each skipped or answered question increases the total question count, shown in the top-left corner.

### Example of fields mode:

In this mode, users solve tasks related to calculating the area of geometric figures such as rectangles, triangles, and circles. The app presents a figure with labeled dimensions, and the user writes the result by hand. It’s a great way to combine math understanding with visual learning and handwriting practice.

<img src="https://github.com/Mon4/Math-project/assets/44522588/11131898-2e64-4748-a551-92f99151babb" width="300" height="600" />
</br>

### Example of text tasks:

In this mode, users are given short word problems that require reading comprehension and basic math to solve. For example: "A farmer has 3 baskets. Each basket holds 5 apples. How many apples does he have in total?" The user writes the answer by hand, combining logic, math skills, and handwriting practice in one engaging task.

<img src="https://github.com/Mon4/Math-project/assets/44522588/df97e9f0-2121-43cc-9253-ff15a901343d" width="300" height="600" />
</br>

## 📂 Task File Handling

The program loads task descriptions from `.txt` files.

- **Operations Mode**  
  Files contain equations using variables like `x`, `y`, and `z` (e.g., `x + y + z`). These variables are randomized at runtime to generate a wide variety of arithmetic problems.

- **Text Tasks Mode**  
  Files include both the task description (word problem) and the formula used to calculate the correct answer. By randomizing values of `x`, `y`, and `z`, the app generates multiple versions of each task.

Users can easily add their own tasks by editing or creating new `.txt` files, making the app highly flexible and expandable.


![171944830-4563842d-f4ca-474d-b9e8-a0507b8d8fc7](https://github.com/Mon4/math-project/assets/44522588/56e95a9f-68ac-4fa9-88d8-6c2de195bfcc)



## Digit recognition - model in Python
MLP model to recognize handwritten digits based on the MNIST dataset. I've used mainly python and tensorflow library. Also I used flask to set up ml model on the server.

Building 1 hidden layer model with flatten input data (28x28 images) and 10 output digits. Using softmax in hidden layer and ReLU in output.

sample input data: 

## Digit Recognition – Python ML Model

A **Multilayer Perceptron (MLP)** model for recognizing handwritten digits based on the **MNIST dataset**. Built using **Python** and the **TensorFlow** library. The model is deployed on a server using **Flask**, enabling real-time digit recognition from the app.

### Model Architecture
- **Input Layer**: Flattened 28×28 pixel grayscale images  
- **Hidden Layer**: 1 layer with **ReLU** activation  
- **Output Layer**: 10 neurons (digits 0–9) with **Softmax**

### Sample Input

<img src="https://github.com/Mon4/Math-project/assets/44522588/ba38ca70-b30e-4b69-a234-974cfba80010" width="800" height="500" />
</br>

Accuracy and loss function:

<img src="https://github.com/Mon4/Math-project/assets/44522588/13fedefd-8824-4fff-9ee8-b71890731598" width="800" height="500" />
</br>

Baseline Error: 1.77%

--- 

The app is based on [window app](https://github.com/Mon4/python-educational-program) which I've made earlier in Python.
