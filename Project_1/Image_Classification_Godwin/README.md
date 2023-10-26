## Model Accuracy

The model achieved an impressive accuracy score of 84% on the testing data. 
This result demonstrates the effectiveness of the approach used to build the model.

## Model Architecture

This model was created using transfer learning, leveraging the powerful Xception model 
as a base. Transfer learning is an approach where a pre-trained model is used as a starting 
point for a new task, allowing the model to learn from the patterns and features extracted from a large dataset.

## Xception Model

Xception is a deep convolutional neural network architecture that has demonstrated strong 
performance in various computer vision tasks. It is known for its ability to capture intricate 
features within images, making it an ideal candidate for transfer learning.

## Fine-Tuning

To adapt the Xception model for the specific task at hand, the base model was fine-tuned. 
Fine-tuning involves adjusting the weights of the pre-trained model to better suit the target task. 
In this case, the base model's weights were frozen to preserve the knowledge gained from the original dataset.

## Adding Extra Layers

To tailor the model to the specific problem, additional layers were added on top of the Xception base. 
These extra layers allow the model to learn task-specific features and make predictions based on the 
patterns it identifies in the data.

By combining transfer learning with fine-tuning and the addition of extra layers, this model 
achieved an accuracy score of 84% on the testing data, showcasing its effectiveness in solving the targeted problem.
