#MarkHead Flask API
## Instructions :
>* Create a virtual environment with :
>>* GNU/Linux : `python3 -m venv env`
>>* Windows : `python -m venv env`
>* Use this environment with :
>>* GNU/Linux : `source ./env/bin/activate`
>>* Windows : `.\env\Scripts\activate.bat`
> (env) should appear
>* Install `wheel` with :
>>* `pip install wheel`
>* Install all the required depedencies with :
>>* `pip install -r requirements.txt`
>* Look for outdated librairies and update them :
>>* `pip list --outdated` then :
>>>* GNU/Linux : `pip install --upgrade **librairies to update** --no-cache-dir`
>>>* Windows : `python -m pip install --upgrade **librairies to update**`
>* Install opencv-python and deepface depedencies with :
>>* `sudo apt-get update`
>>* `sudo apt-get install ffmpeg libsm6 libxext6  -y`
>* Run the flask web-server with :
>>* `flask run`
