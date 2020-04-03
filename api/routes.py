from . import  app,db
from flask import jsonify,request
from .models import Patient

@app.route('/')
def hello():
    return  jsonify({"message":"Hello API"})

@app.route('/patients',methods=['POST'])
def add_patient():
    fname=request.json.get('fname')
    lname=request.json.get('lname')
    gender=request.json.get('gender')
    sickness=request.json.get('sickness')

    new_patient=Patient(fname=fname,lname=lname,gender=gender,sickness=sickness)
    db.session.add(new_patient)
    db.session.commit()

    message={"message":"New Patient Created Successfully!!"}
    
    return jsonify(message)


@app.route('/patients',methods=['GET'])
def get_all_patients():
    patients=Patient.query.all()

    patient_list=[]

    for patient in patients:
        patient_obj={}
        patient_obj['fname']=patient.fname
        patient_obj['lname']=patient.lname
        patient_obj['gender']=patient.gender
        patient_obj['sickness']=patient.sickness

        patient_list.append(patient_obj)
    
    return jsonify({"Available Patients":patient_list})



@app.route('/patients/<int:id>',methods=['GET'])
def get_specific_patient(id):
    patient_to_get=Patient.query.get_or_404(id)
    patient_obj={
        "fname":patient_to_get.fname,
        "lname":patient_to_get.lname,
        "gender":patient_to_get.gender,
        "sickness":patient_to_get.sickness
    }
    return jsonify({"Patient":patient_obj})

@app.route('/patients/update/<int:id>',methods=['PATCH'])
def update_patient(id):
    patient_to_update=Patient.query.get_or_404(id)
    patient_to_update.fname=request.json.get('fname')
    patient_to_update.lname=request.json.get('lname')
    patient_to_update.gender=request.json.get('gender')
    patient_to_update.sickness=request.json.get('sickness')

    db.session.commit()

    return jsonify({"Updated Patient Info":{
        "fname":patient_to_update.fname,
        "lname":patient_to_update.lname,
        "gender":patient_to_update.gender,
        "sickness":patient_to_update.sickness
    }})



@app.route('/patients/delete/<int:id>',methods=['DELETE'])
def delete_patient(id):
    patient_to_delete=Patient.query.get_or_404(id)
    db.session.delete(patient_to_delete)
    db.session.commit()
    message={"message":"Patient deleted successfully"}
    return jsonify(message)


@app.errorhandler(404)
def not_found(error):
    return jsonify({"message":"Not found"})

