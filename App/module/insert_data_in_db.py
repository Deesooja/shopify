
def insert_data(model,data,produt_obj,option_obj,new_name_of_id):
    fields=[  field.name for field in model._meta.get_fields()]
    print('fields',fields)
    print('data',data)
    if 'id' in data:
        data[new_name_of_id]=data.get('id')

    data['product']=produt_obj
    data['option']=option_obj
    print('data',data)
    print(model)
    model_obj=model()

    for i in range(len(fields)):
        if fields[i]=='id':
            continue
        setattr(model_obj,fields[i],data.get(fields[i]))
        print(fields[i],data.get(fields[i]))
    model_obj.save()

    return model_obj