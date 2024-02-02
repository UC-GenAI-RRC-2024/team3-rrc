<!-- ABOUT THE PROJECT -->
## Project 3 of P&G-UC Hackathon about prediction of eczema in 2050





<p align="right">(<a href="#readme-top">back to top</a>)</p>
Atopic dermatitis is a common chronic skin disease characterized by dry skin, localized red scaly patches, intense itching, and skin pain. It is also known as 'atopic eczema', 'neurodermatitis', or simply as 'eczema'. The exact cause of atopic dermatitis is not fully understood, but it is believed to be influenced by genetic and environmental factors, disruptions in the skin barrier, alterations in the microbiome, and immune dysregulation. It is a highly variable skin disorder that can affect both children and adults, with symptoms typically fluctuating between periods of flares and remissions. The skin lesions associated with atopic dermatitis include papules, oozing vesicles, crusting, scaling, and thickening of the skin. The disease can have a significant impact on a person's physical well-being and quality of life, causing sleep deprivation, difficulty in performing daily activities, and emotional distress.


### Built With


* https://dash.plotly.com/


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The project has two parts, first the developer needs to index the input file (here PDF files). The files will be indexed and saved locally as vector embeddings.

After generating the index files, we can run the server to access to the index folder and provide QA interface witht the help of openAI.

### Prerequisites

For this project you need to have python installed, this project is tested with Python 3.10.12 version.

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get an openAI API Key at [https://openai.com/blog/openai-api](https://openai.com/blog/openai-api)
2. Clone the repo
   ```sh
   git clone https://github.com/UC-GenAI-RRC-2024/team3-rrc2024.git
   ```
3. go to the folder
   ```sh
   cd team3-rrc2024
   ```
4. make a virtual environment for installing the required libraries with specific versions
   ```sh
   virtualenv venv310
   . venv310/bin/activate
   ```
5. Install requirements.txt
   ```sh
   pip3 install -r requirements.txt
   ```
6. Enter your OpenAI API in `pages/chatbot/chatbot_model.py`
   ```js
   os.environ["OPENAI_API_KEY"] = 'your_openAI_API'
   ```
7. If you are re-indexing the pdf files, 
please comment out the init_index("OneDrive_1_1-27-2024") in the index.py file, this function assumes that all of the training pdf files are in the "OneDrive_1_1-27-2024". This runs the indexing. You should put the new indexed folder in the project folder. For your convenience, already indexed file is placed in "OneDrive_1_1-27-2024" folder @ https://mailuc-my.sharepoint.com/:f:/g/personal/shamsabz_ucmail_uc_edu/EvL9x1G1isBLjbQF-C4rta0BXvsj0amgxaCZ1CuHQrpeMw?e=AA9A8o

8. Run the server 
   ```py
   python3 index.py
   ```
9. The project will be running on your localhost @ http://127.0.0.1:8050/
   


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Please check http://149.165.174.107/ for the working prototype.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Behrouz Shamsaei  - behrouz.shamsaei@uc.edu

Project Link: [https://github.com/UC-GenAI-RRC-2024/team3-rrc2024.git](https://github.com/UC-GenAI-RRC-2024/team3-rrc2024.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I would like to give credit to our pariticipating team:

Aniket Bhanderi, (CEAS), 
Navya Ghanta, (Business), 
Xin Tang, (Business), 
Ryan Therkelsen, (A&S Mathematical Sci.), 
Domagoj Bui, (DAAP MDes)





