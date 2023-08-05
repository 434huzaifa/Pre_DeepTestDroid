# Pre_DeepTestDroid
Bunch of Code/file to preprocess and model creation code. For the [DeepTestDroid](https://github.com/434huzaifa/DeepTestDroid)

# File Details

- MobileNetV3Large > Blackbox model. All the other models are trained with the same configuration.
- folderspliter > its similar to train_test_split. but it is used for image data.
- gui,gui2,gui3 > An application built for sorting screenshots manually using Tkinter.
- sorter > automatically sorting screenshots from the component numbers from data2_all.csv
- makedata > Save the JSON file name and component number from the JSON file to the data2_all.csv.

# File
- [data2_all.csv](https://drive.google.com/file/d/1AKXhTL26EA8l_VxybinDiK7mb4xM8gkl/view?usp=sharing)

# Need To know
- almost all screenshots have a json file containing details of the screenshot.
- Even though I am calling it a screenshot, it is actually a semantics annotation or wireframe.
