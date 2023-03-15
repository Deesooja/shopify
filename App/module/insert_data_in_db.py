
def insert_data(model, data, produt_obj ,option_obj ,new_name_of_id=None , update=False , shop=None):
    fields=[  field.name for field in model._meta.get_fields()]
    print('fields',fields)
    # print('data',data)
    if 'id' in data and new_name_of_id :
        data[new_name_of_id]=data.get('id')

    data['product']=produt_obj
    data['option']=option_obj
    data['shopify_created_status']=False
    data['shopify_updated_status']=True
    data['shop']=shop
    
    # data['name']=data.get('title')
    # print('data',data)
    # print(model)
    model_obj=model()
    # print('before',model_obj)
    if update:
       model_obj= model.objects.get(**{new_name_of_id: data.get('id')})
    # print('after',model_obj)

    for i in range(len(fields)):
        print('id',data.get(id))
        if fields[i]=='id':
            continue
        setattr(model_obj,fields[i],data.get(fields[i]))
        print(fields[i],data.get(fields[i]))
    model_obj.save()

    return model_obj

