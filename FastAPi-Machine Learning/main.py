from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import pickle
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("index.html") as f:
        html_content = f.read()
    return html_content


# Statik dosyalar için mount işlemi
app.mount("/static", StaticFiles(directory="static"), name="static")

class ModelSchema(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# @app.get("/")
# def hello():
#     return {"Hello": "Docker-MLOps"}
@app.post("/predict/knn")
def predict_knn(predict_value: ModelSchema):
    filename = '../output/knn.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    df = pd.DataFrame(
        [predict_value.dict().values()],
        columns=predict_value.dict().keys()
    )
    pred = loaded_model.predict(df)
    return {"predict": int(pred[0])}

@app.post("/predict/logreg")
def predict_logreg(predict_value: ModelSchema):
    filename = '../output/logreg.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    df = pd.DataFrame(
        [predict_value.dict().values()],
        columns=predict_value.dict().keys()
    )
    pred = loaded_model.predict(df)
    return {"predict": int(pred[0])}

@app.post("/predict/dectree")
def predict_dectree(predict_value: ModelSchema):
    filename = '../output/dec_tree.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    df = pd.DataFrame(
        [predict_value.dict().values()],
        columns=predict_value.dict().keys()
    )
    pred = loaded_model.predict(df)
    return {"predict": int(pred[0])}

# Uygulamayı başlatmak için
# python -m uvicorn main:app --reload
