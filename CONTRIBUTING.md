# Contributing to the Hacktoberfest Repository

Welcome to the Hacktoberfest repository organized by the Microsoft Learn Student Ambassadors in Nigeria! We appreciate your interest in contributing to our projects. Please read this guide to understand how you can participate and make meaningful contributions.

## How to Install Dependencies and Work on the Project Locally

1. **Clone the Repository:**

   From your terminal, clone your forked repository and name it `AI-Hacktober-MLSA`.

   ```bash
   # Replace {user_name} with your GitHub username
   git clone --depth 1 https://github.com/{user_name}/AI-Hacktober-MLSA.git
   ```

   > This ensures you clone only the most recent commit and all files to avoid unnecessary commit history (image files that have been resized).

2. **Set Up Virtual Environment:**

   Create a virtual environment named `AI-Hacktober-MLSA`.

   ```bash
   # Windows
   python -m venv AI-Hacktober-MLSA

   # macOS or Linux
   python3 -m venv AI-Hacktober-MLSA
   ```

   Activate the virtual environment:

   ```bash
   # Windows
   AI-Hacktober-MLSA\Scripts\activate

   # macOS or Linux
   source AI-Hacktober-MLSA/bin/activate
   ```

   Install necessary dependencies:

   ```bash
   cd AI-Hacktober-MLSA
   pip install -r requirements.txt
   ```

   Add the virtual environment to Jupyter Kernel (if contributing to Projects 1 and/or 3):

   ```bash
   python -m ipykernel install --user --name=AI-Hacktober-MLSA
   ```

3. **Work on Your Contributions:**

   - For **Project 1: Image Classification of Building Types**, follow the guidelines in `Project_1` directory.
   - For **Project 2: Speech Translation**, edit or enhance existing scripts following the instructions in `Project_2` directory.
   - For **Project 3: Prediction of Nigerian Students' Year One Performance**, work on your regression task as explained in `Project_3` directory.

4. **Commit and Push:**

   After making changes, commit them and push to your forked repository.

   ```bash
   git add .
   git commit -m "{COMMIT_MESSAGE}"
   git push
   ```

5. **Create a Pull Request:**

   Create a pull request to merge your changes into the main repository.

## 🏢 Project 1: Image Classification of Building Types

Contribute to image classification tasks:

### Contribution Guidelines:

1. Clone the repository and follow the [local setup instructions](#how-to-install-dependencies-and-work-on-the-project-locally).

2. Create a folder under the `Project_1` directory following the naming convention:
   - Folder Name: `Image_Classification_{GitHub_Username}`

   For example, if your GitHub username is `octocat`, your folder should be named `Image_Classification_octocat`.

3. Work on image classification tasks in your notebook. Minimum contribution: data preprocessing (images).

4. For modelling contributions, the model must achieve a minimum of 60% accuracy for validation.

5. The team will evaluate the model's performance using a separate test dataset.

6. Make a pull request when ready.

## 🌍 Project 2: Speech Translation

Enhance existing scripts for speech translation:

### Contribution Guidelines:

1. Clone the repository and follow the [local setup instructions](#how-to-install-dependencies-and-work-on-the-project-locally).

2. Create a virtual environment for the project using the provided `requirements.txt` file.

3. Edit, fine-tune, or create new functions in the scripts for new features or improvements.

4. Thoroughly test your changes in your virtual environment.

5. Commit your changes and push to your forked repository.

6. Create a pull request to merge your changes.

## 📚 Project 3: Prediction of Nigerian Students' Year One Performance

Contribute to regression task:

### Contribution Guidelines:

1. Contribute to the data collection process by completing the [Nigerian Students' Year One Performance survey](https://forms.office.com/r/Q6QqNzTasn).

2. Clone the repository and follow the [local setup instructions](#how-to-install-dependencies-and-work-on-the-project-locally).

3. Create a folder under the `Project_3` directory following the naming convention:
   - Folder Name: `GPA_Prediction_{GitHub_Username}`

   For example, if your GitHub username is `octocat`, your folder should be named `GPA_Prediction_octocat`.

4. Work on your regression task in your notebook. Contribution will be evaluated based on RMSE metric improvements.

### Evaluation Metric:

- **RMSE (Root Mean Squared Error):**
  - Aim to improve the RMSE metric.
  - Minimum standard for RMSE score for PR approval will be communicated.

## ✔️ General Guidelines

- Ensure your code is well-documented and follows best practices.

- Provide a descriptive pull request explaining the purpose of your changes.

- Be respectful and collaborative. Feel free to ask questions and seek assistance from other contributors or maintainers.

- Happy hacking! We appreciate your contributions to make this project better.

If you have any questions or need assistance, please feel free to reach out to us.

**Happy Hacking!**

## 🔗 Links to Resources

1. [How to Do Your First Pull Request](https://youtu.be/nkuYH40cjo4?si=Cb6U2EKVR_Ns4RLw)
2. [Process and Translate Speech with Azure AI Speech Services](https://learn.microsoft.com/en-gb/training/paths/process-translate-speech-azure-cognitive-speech-services/?wt.mc_id=studentamb_217190)
3. [How to Translate Text with Azure AI Translator in Python](https://learn.microsoft.com/en-us/azure/ai-services/translator/quickstart-text-rest-api?tabs=python#translate-text?wt.mc_id=studentamb_217190)
4. [Azure Speech Service documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/?wt.mc_id=studentamb_217190)
5. [Azure AI Translator documentation](https://learn.microsoft.com/en-us/azure/ai-services/translator/?wt.mc_id=studentamb_217190)
6. [Getting Started: Multilingual Speech Transcription and Translation Solution with Azure AI](https://youtu.be/ikNPMomeZKs?si=90exV6Kd5xbR46QE)
