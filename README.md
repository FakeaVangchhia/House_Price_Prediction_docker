# How to install
- Clone the repository using 'git clone https://github.com/FakeaVangchhia/House_Price_Prediction_docker' in terminal
- cd House_Price_Prediction_docker
- pip install requirements.txt

## Run the model 
- uvicorn app.main:app

## Creating docker image
> Make sure the docker engine is running, and type the following command in terminal.
- docker build -t house-price-prediction .
- docker run -d -p 8000:8000 house-price-prediction

  ### Goto: http://127.0.0.1:8000/ and you will see your project running, you can also goto http://127.0.0.1:8000/docs and click on post -> Try it out -> change the Years of experience
  eg: 5, click on execute. You can get back to http://127.0.0.1:8000/ to see your output, you can also find the output below in the SwaggerUI.

### Thank you
