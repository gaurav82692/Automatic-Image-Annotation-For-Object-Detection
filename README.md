# Are you tired by doing Annotation manually ?<br>
<br>![tumblr_maile4kaQO1qj1svso1_500](https://user-images.githubusercontent.com/54155003/124456019-dc494b80-dda7-11eb-84c3-f8ab0eb0abb8.gif)

## Let's Automate it.
We are going to use Reverse Engineering technique. First we will detect objects into images the save their bounding box coordinates as per our requirement in XML format.<br>
### Step 1
For Anaconda python Environment <br>
```
conda create -n env
Activate env 
```
For Linux <br>
```
sudo apt install python3-venv
python3 -m venv env
source env/bin/activate
```
### Step 2
Install dependencies
`pip install -r requirements.txt`<br>
### Step 3
1. Download pre-trained weights from given link 
https://drive.google.com/file/d/1FCGAQsBADMPdyfmZrOsSDeneikGWcnlu/view <br>
2. Replace yolov4-csp.weights with downloded weights (file size 202MB) in configuration directory<br>
### Step 4
Open `Annotaions.name` file present in configuration directory and edit the Labels names as per your dataset.
### Step 5
Run `python start_annotation.py`

# Bravooo 
Your work is done now check Annotations folder.<br>
<br>
![giphy](https://user-images.githubusercontent.com/54155003/124464209-87123780-ddb1-11eb-9eee-eb4ce367e5a8.gif)
