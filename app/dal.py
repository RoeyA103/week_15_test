from connection import get_db
from bson.objectid import ObjectId
from fastapi import HTTPException ,status 
from fastapi.responses import JSONResponse
from pymongo.collection import ReturnDocument
from pymongo import DESCENDING
from rich import print as rprint

def serialize_doc(doc):
    if doc and "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc

def serialize_docs(docs):
    return [serialize_doc(doc) for doc in docs]

def get_collection():
        db = get_db()
        collection = db.employees
        return collection
    
def get_engineering_high_salary_employees():
    """Highly paid employees in the department Engineering"""
    try:
        collection = get_collection()
        fields = {'employee_id':1,'name':1,'salary':1,'_id':0}
        query = {"job_role.department":"Engineering",'salary':{'$gt':65000}}
        docs = list(collection.find(query,fields))  
        return docs
    except Exception as e:
        raise e

def get_employees_by_age_and_role():
    """Employees by age and position"""
    try:
        collection = get_collection() 
        query = {"$or":[{'job_role.title':"Engineer"},{'job_role.title':'Specialist'}] 
                ,'age':{'$gt' : 29 ,'$lte' : 45}}
        docs = list(collection.find(query))  
        return docs
    except Exception as e:
        raise e

def get_top_seniority_employees_excluding_hr():
    try:
        collection = get_collection() 
        query = {'job_role.department':{'$ne':'HR'}}
        docs = list(collection.find(query).sort("years_at_company",DESCENDING).limit(7))
        return docs
    except Exception as e:
        raise e

def get_employees_by_age_or_seniority():
    try:
        collection = get_collection() 
        fields = {'employee_id':1,'name':1,'age':1,"years_at_company":1,'_id':0}
        query = {"$or":[{'age':{'$gt' : 50}},{'years_at_company':{'$lte' : 2}}]}
        docs = list(collection.find(query,fields))
        return docs
    except Exception as e:
        raise e

def get_managers_excluding_departments():
    try:
        collection = get_collection() 
        query = {"$and":[{'job_role.title':"Manager"},
                        {'job_role.department':{'$ne':"Sales"}},
                        {'job_role.department':{'$ne':"Marketing"}}]}
        docs = list(collection.find(query))
        return docs
    except Exception as e:
        raise e

def get_employees_by_lastname_and_age():
    try:
        collection = get_collection() 
        fields = {'name':1,'age':1,'job_role.department':1,'_id':0}
        query = {'$and': [{"$or":[{'name':{"$regex": "Nelson$"}},
                        {'name':{"$regex": "Wright$"}}]},
                        {'age':{'$lte':34}}]}
        docs = list(collection.find(query))
        return docs
    except Exception as e:
        raise e