
To run the project, you need to create a virtual environment. Follow these steps:
Create a virtual environment by running the following command:
python -m venv myenv

This will create a new virtual environment named "myenv".
Activate the virtual environment. Use the appropriate command based on your operating system:
For Windows:
myenv\Scripts\activate

Once the virtual environment is activated, install the project dependencies using the following command:
pip install -r requirements.txt

This will install all the required packages specified in the requirements.txt file.
Finally, run the program using Streamlit by executing the following command:
streamlit run main.py

