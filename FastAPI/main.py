from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field,computed_field
from typing import Annotated,Literal,Optional
import json

app = FastAPI()

class Patient(BaseModel):
    id:Annotated[str,Field(...,description='Id of the Patient',examples=['P001'])]
    name : Annotated[str, Field(...,max_length=50, description='Give name of the patient less than 50 char')]
    city:Annotated[str,Field(...,description='city where patient is living')]
    age : Annotated[int, Field(...,gt=0,lt=120,description='Age of the patient')]
    gender:Annotated[Literal['male','female','others'],Field(...,description='Gender of the patient')]
    height:Annotated[float, Field(...,gt=0, description='height of the patient in mtrs')]
    weight:Annotated[float, Field(...,gt=0, description='weight of the patient in KGs')]

    @computed_field # field to be calculated and not given by the user
    @property
    def bmi(self) -> float: # we get the instance of our model
        bmi = round(self.weight/(self.height**2),2) # round off upto 2 decimals  
        return bmi
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25 :
            return 'Normal'
        elif self.bmi < 30 :
            return 'Caution'
        else:
            return 'Obese'
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]

def load_data():
    with open('patients.json', 'r') as d:
        data = json.load(d)
    return data
def save_data(data):
    with open('patients.json','w') as s:
        json.dump(data,s) # will dump into s or file 

@app.get('/')
def hello():
    return {"message": "Patient Management System API"}

@app.get('/about')
def about():
    return {"message":"API to manage patient records."}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')  #path param
def view_patient(patient_id: str = Path(...,description ="ID of the patient to view",examples="P001")):    #... this tells that this is required
    data = load_data() # to load data
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')
def sort_patients(sort_by: str = Query(...,description='Sort on the basis of height, weight or bmi'), order: str = Query('asc',description='sort in asc or desc')):

    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid fields select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order select between asc and desc')
    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

@app.post('/create')
def create_patient(patient : Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail = 'Patient already exist')
    data[patient.id]=patient.model_dump(exclude=['id'])
    save_data(data)
    return JSONResponse(status_code=201, content={'message':'patient created successfully'} )
@app.put('/edit/{patient_id}')
def update_patient(patient_id:str,patient_update:PatientUpdate):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail = 'Patient not found')
    exist_patient_info = data[patient_id]
    Updated_info=patient_update.model_dump(exclude_unset=True)
    for key,value in Updated_info.items(): # loop is on the updated_info and changes on the existing info
        exist_patient_info[key] = value
    exist_patient_info['id']= patient_id
    new_patient_obj = Patient(**exist_patient_info)
    exist_patient_info = new_patient_obj.model_dump(exclude='id')
    data[patient_id] = exist_patient_info
    save_data(data)
    return JSONResponse(status_code=200,content={'message':'Patient Updated'})
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    data = load_data()
    if patient_id not in data:
            raise HTTPException(status_code=400, detail = 'Patient not found')
    del data[patient_id]
    save_data(data)
    return JSONResponse(status_code=200,content={'message':'Patient successfully deleted'})



# Pydantic 
# def insert_patient_data(name: str, age: int):
#     if type(name) == str and type(age) == int:
#         if age < 0:
#             raise TypeError("Age should be positive")
#         else:
#             print(name)
#             print(age)
#             print('inserted into database')
#     else:
#         raise TypeError('Incorrect data type')

# insert_patient_data('nitish', '30')

# All pydantic use
# from pydantic import BaseModel, EmailStr, AnyUrl,Field, field_validator, model_validator,computed_field
# from typing import List, Dict, Optional,Annotated
# class Address(BaseModel): #model inside a model 
#     city:str
#     state:str
#     pincode:int
# class Patient(BaseModel):
#     name : Annotated[str, Field(max_length=50,title='Name of the patient', description='Give name of the patient less than 50 char',examples=['pulkit','sarbjeet'])] # custom validation using Field
#     email:EmailStr
#     linkedIn_url : AnyUrl
#     age : int = Field(gt=0,lt=120)
#     weight:Annotated[float, Field(gt=0, strict=True)] #what happen is when you give this a string it will automatically converts it into the float datatype but if you want that it should be controlled by an error then it should be set by strict.
#     height:float
#     married : bool
#     address : Address
#     allergies: Optional[List[str]]= None # validating both that it should be list as well as string
#     contact_details: Dict[str,str]
#     @computed_field # field to be calculated and not given by the user
#     @property
#     def bmi(self) -> float: # we get the instance of our model
#         bmi = round(self.weight/(self.height**2),2) # round off upto 2 decimals  
#         return bmi
#     @model_validator(mode='after') #if validation requires for more than 1 field
#     def validate_emergency_contact(cls,model):
#         if model.age>60 and 'emergency' not in model.contact_details:
#             raise ValueError('Patient above 60 age must have a emergency contact')
#         return model

#     @field_validator('email') # we have to make a method inside our class and it is used with a decorator and it also have mode after which is default and before which means it will get the value before any data type change  
#     @classmethod 
#     def email_validator(cls,value):  
#         valid_domain = ['hdfc.com','icici.com']
#         domain_name = value.split('@')[-1] # this will get the last part after @
#         if domain_name not in valid_domain:
#             raise ValueError('Not a valid domain')
#         return value
# address_info = {'city':'muzaffarnagar','state':'UP','pincode':'251001'}
# address1 = Address(**address_info) # should be defined above
# patient_info = {'name':'Pulkit','email':'pulkit@hdfc.com','linkedIn_url':'htpp://linkedin.com/','age' : 65, 'weight': 78.2,'height':1.72,'married':False,'address':address1, 'allergies':['Dust','pollen'],'contact_details':{'phone':'123456895','emergency':'15646416521'}}
# patient1= Patient(**patient_info)
# def insert_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print(patient.bmi)
#     print(patient.address.pincode)# benefit that we can also get the single value of address from this

# insert_patient_data(patient1)
# #serialization
# temp = patient1.model_dump(include=['name']) # to get in the dictionary, include is used for only name to be exported as dict and we have exclude also
# # temp = patient1.model_dump_json() # to get in the json
# # exclude_unset = True, only the values set when the object creation
# print(temp)
# print(type(temp))
