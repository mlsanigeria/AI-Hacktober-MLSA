# Contribution Guidelines

<<<<<<< HEAD
<<<<<<< HEAD
# Contributing to Hacktoberfest Repository

Welcome to the Hacktoberfest repository organized by the Microsoft Learn Student Ambassadors in Nigeria! We appreciate your interest in contributing to our projects. Please read this guide to understand how you can participate and make meaningful contributions.

## How to Install Dependencies and Work on Project Locally

From your terminal:

Clone the repository and name as `AI-Hacktober-MLSA`

```
git clone https://github.com/mlsanigeria/AI-Hacktober-MLSA.git
```

Create a virtual environment with the same name (`AI-Hacktober-MLSA`)
=======
=======
>>>>>>> 59c338c0174ab92ba97137a492daa21330ffc3bb
# Contributing to the Hacktoberfest Repository

Welcome to the Hacktoberfest repository organized by the Microsoft Learn Student Ambassadors in Nigeria! We appreciate your interest in contributing to our projects. Please read this guide to understand how you can participate and make meaningful contributions.

## How to Install Dependencies and Work on the Project Locally

From your terminal:

Clone your forked repository and name it `AI-Hacktober-MLSA`

```
# Replace {user_name} with your GitHub username
git clone --depth 1 https://github.com/{user_name}/AI-Hacktober-MLSA.git
```
> This makes sure you clone only the most recent commit and all files to avoid cloning every commit history as image files have been resized and hence will only take space on your local machine for what you don't need.

Create a virtual environment with the name (`AI-Hacktober-MLSA`)
<<<<<<< HEAD
>>>>>>> 875e090092874b8666533f89590c4d844bb005ac
=======
>>>>>>> 59c338c0174ab92ba97137a492daa21330ffc3bb

```
# Windows
python -m venv AI-Hacktober-MLSA

# macOS or Linux
python -m venv AI-Hacktober-MLSA
```

Activate the created virtual environment
```
# Windows
AI-Hacktober-MLSA\Scripts\activate

#macOS or Linux
source AI-Hacktober-MLSA/bin/activate
```

Then install the necessary dependencies.

``` 
cd AI-Hacktober-MLSA
pip install -r requirements.txt
```


<<<<<<< HEAD
<<<<<<< HEAD
Add the virtual environment to Jupyter Kernel (if you want to contribute to Project 1 and/or 3)
=======
Add the virtual environment to Jupyter Kernel (if you want to contribute to Projects 1 and/or 3)
>>>>>>> 875e090092874b8666533f89590c4d844bb005ac
=======
Add the virtual environment to Jupyter Kernel (if you want to contribute to Projects 1 and/or 3)
>>>>>>> 59c338c0174ab92ba97137a492daa21330ffc3bb

```
python -m ipykernel install --user --name=AI-Hacktober-MLSA
```

After making all the changes you wish to make, commit and push back to your forked repo.
```
git add .
git commit -m "{COMMIT_MESSAGE}"
git push
```

## 🏢 Project 1: Image Classification of Building Types

In this project, you will work on image classification tasks. We have provided a starter notebook for you to begin your work.

### Contribution Guidelines

<<<<<<< HEAD
<<<<<<< HEAD
1. Clone the repository to your local machine and follow the [procedure to set-up your environment locally](https://github.com/mlsanigeria/AI-Hacktober-MLSA/blob/main/CONTRIBUTING.md#how-to-install-dependencies-and-work-on-project-locally).
=======
1. Clone the repository to your local machine and follow the [procedure to set up your environment locally](https://github.com/mlsanigeria/AI-Hacktober-MLSA/blob/main/CONTRIBUTING.md#how-to-install-dependencies-and-work-on-project-locally).
>>>>>>> 875e090092874b8666533f89590c4d844bb005ac
=======
1. Clone the repository to your local machine and follow the [procedure to set up your environment locally](https://github.com/mlsanigeria/AI-Hacktober-MLSA/blob/main/CONTRIBUTING.md#how-to-install-dependencies-and-work-on-project-locally).
>>>>>>> 59c338c0174ab92ba97137a492daa21330ffc3bb

2. Create a folder under the `Project_1` directory with the following naming convention:
   - Folder Name: `Image_Classification_{GitHub_Username}`
   
   For example, if your GitHub username is `octocat`, your folder should be named `Image_Classification_octocat`.

3. Within your personal folder, you have your own environment to create your notebook and workspace.

4. Work on your image classification tasks in your notebook.

<<<<<<< HEAD
<<<<<<< HEAD
5. The minimum contribution a user can make is on preprocessing of the data(images).

6. For contributions related to modeling, the model's performance must achieve a minimun of 60% accuracy to be considered valid.

7. The team will perform an evaluation of the model using a seperate test dataset to verify its performance score.
=======
=======
>>>>>>> 59c338c0174ab92ba97137a492daa21330ffc3bb
5. The minimum contribution a user can make is to preprocess the data (images).

6. For contributions related to modelling, the model's performance must achieve a minimum of 60% accuracy to be considered valid.

7. The team will perform an evaluation of the model using a separate test dataset to verify its performance score.
<<<<<<< HEAD
>>>>>>> 875e090092874b8666533f89590c4d844bb005ac
=======
>>>>>>> 59c338c0174ab92ba97137a492daa21330ffc3bb

8. When you are ready, make a pull request to the main repository.

## 🌍 Project 2: Speech Translation

Project 2 involves enhancing existing scripts. We have provided starter scripts along with a `requirements.txt` file.

### Contribution Guidelines

<<<<<<< HEAD
<<<<<<< HEAD
1. Clone the repository to your local machine and follow the [procedure to set-up your environment locally](https://github.com/mlsanigeria/AI-Hacktober-MLSA/blob/main/CONTRIBUTING.md#how-to-install-dependencies-and-work-on-project-locally).
=======
1. Clone the repository to your local machine and follow the [procedure to set up your environment locally](https://github.com/mlsanigeria/AI-Hacktober-MLSA/blob/main/CONTRIBUTING.md#how-to-install-dependencies-and-work-on-project-locally).
>>>>>>> 875e090092874b8666533f89590c4d844bb005ac
=======
1. Clone the repository to your local machine and follow the [procedure to set up your environment locally](https://github.com/mlsanigeria/AI-Hacktober-MLSA/blob/main/CONTRIBUTING.md#how-to-install-dependencies-and-work-on-project-locally).
>>>>>>> 59c338c0174ab92ba97137a492daa21330ffc3bb

2. Create a virtual environment for the project using the provided `requirements.txt` file.

3. Edit, fine-tune, or create new functions in the scripts to add new features or improvements.

4. Test your changes thoroughly in your virtual environment.

5. Commit your changes and push them to your forked repository.

6. Create a pull request to merge your changes into the main repository.


<<<<<<< HEAD
<<<<<<< HEAD
## 📚 Project 3: Prediction of Nigerian Student's Year One Performance
=======
## 📚 Project 3: Prediction of Nigerian Students' Year One Performance
>>>>>>> 875e090092874b8666533f89590c4d844bb005ac
=======
## 📚 Project 3: Prediction of Nigerian Students' Year One Performance
>>>>>>> 59c338c0174ab92ba97137a492daa21330ffc3bb

In this project, you will work on a regression task. We have provided a starter notebook for you to begin your work.

### Contribution Guidelines

<<<<<<< HEAD
<<<<<<< HEAD
1. Contribute to the data collection process for this project by completing the survey on [Nigerian Student's Year One Performanc](https://forms.office.com/r/Q6QqNzTasn).
2. Clone the repository to your local machine and follow the [procedure to set-up your environment locally](https://github.com/mlsanigeria/AI-Hacktober-MLSA/blob/main/CONTRIBUTING.md#how-to-install-dependencies-and-work-on-project-locally).
=======
1. Contribute to the data collection process for this project by completing the survey on [Nigerian Students' Year One Performance](https://forms.office.com/r/Q6QqNzTasn).
2. Clone the repository to your local machine and follow the [procedure to set up your environment locally](https://github.com/mlsanigeria/AI-Hacktober-MLSA/blob/main/CONTRIBUTING.md#how-to-install-dependencies-and-work-on-project-locally).
>>>>>>> 875e090092874b8666533f89590c4d844bb005ac
=======
1. Contribute to the data collection process for this project by completing the survey on [Nigerian Students' Year One Performance](https://forms.office.com/r/Q6QqNzTasn).
2. Clone the repository to your local machine and follow the [procedure to set up your environment locally](https://github.com/mlsanigeria/AI-Hacktober-MLSA/blob/main/CONTRIBUTING.md#how-to-install-dependencies-and-work-on-project-locally).
>>>>>>> 59c338c0174ab92ba97137a492daa21330ffc3bb
3. Create a folder under the `Project_3` directory with the following naming convention:
   - Folder Name: `GPA_Prediction_{GitHub_Username}`
   
   For example, if your GitHub username is `octocat`, your folder should be named `GPA_Prediction_octocat`.

4. Within your personal folder, you have your own environment to create your notebook and workspace.

5. Work on your regression task in your notebook.

### Evaluation Metric

<<<<<<< HEAD
<<<<<<< HEAD
We evaluate the performance of the machine learning model using the Root Mean Squared Error(RMSE). The RMSE is calculated using the predicted normalized GPA values and actual normalized GPA values from the dataset. [Check the starter notebook for more information](https://github.com/mlsanigeria/AI-Hacktober-MLSA/blob/main/Project_3/GPA_Prediction_{GitHub_Username}/GPA_prediction.ipynb).

- Your contribution should aim to improve the RMSE metric.
- PRs will be reviewed based on the improvement they bring to the RMSE.
- A minimum standard for RMSE score for merging PRs will be set and communicated to you in your PR.
=======
=======
>>>>>>> 59c338c0174ab92ba97137a492daa21330ffc3bb
We evaluate the performance of the machine learning model using the Root Mean Squared Error(RMSE). The RMSE is calculated using the predicted normalized GPA values and the actual normalized GPA values from the dataset. [Check the starter notebook for more information](https://github.com/mlsanigeria/AI-Hacktober-MLSA/blob/main/Project_3/GPA_Prediction_{GitHub_Username}/GPA_prediction.ipynb).

- Your contribution should aim to improve the RMSE metric.
- PRs will be reviewed based on the improvements they bring to the RMSE.
- A minimum standard for the RMSE score for merging PRs will be set and communicated to you in your PR.
<<<<<<< HEAD
>>>>>>> 875e090092874b8666533f89590c4d844bb005ac
=======
>>>>>>> 59c338c0174ab92ba97137a492daa21330ffc3bb

## ✔️ General Guidelines

- Ensure your code is well-documented and follows best practices.

- Make sure to create a descriptive pull request explaining the purpose of your changes.

- Be respectful and collaborative. Feel free to ask questions and seek assistance from other contributors or maintainers.

- Happy hacking! We appreciate your contributions to make this project better.

If you have any questions or need assistance, please feel free to reach out to us.

**Happy Hacking!**

## 🔗 Links to Resources
1. [How to Do Your First Pull Request](https://youtu.be/nkuYH40cjo4?si=Cb6U2EKVR_Ns4RLw)
2. [Translate text and speech with Azure AI services](https://learn.microsoft.com/en-us/training/modules/translate-text-with-translation-service/?wt.mc_id=studentamb_217190)
