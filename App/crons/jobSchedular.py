from django_cron import CronJobBase, Schedule
from App.services.ShopifyServices import *
from App.models import *

class CheckAndCreateProduct(CronJobBase):

    RUN_EVERY_MINS = 1 # every 1 minat

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

    code = 'my_app.check_and_create_from_create_db_table'    # a unique code

    def do(self):

        print('Cron_job Hited :- CheckAndCreateProduct')

        for product_object in CreateProduct.objects.filter(shopify_created_status=False):

            print("Starting job :- CheckAndCreateProduct")

            created=creating_shopify_product_by_create_dbtable(product_object)

            if created:

                print("Done :- CheckAndCreateProduct")

            else:
                print("Not Done  :- CheckAndCreateProduct")
                

class CheckAndUpdateProduct(CronJobBase):
    
    RUN_EVERY_MINS = 1 # every 1 minat

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

    code = 'my_app.check_and__from_db_table'    # a unique code

    def do(self):

        print('Cron_job Hited :- CheckAndUpdateProduct')

        # for product_object in Product.objects.filter(shopify_update_status=False):

        print("Starting job :- CheckAndUpdateProduct")

        updating_shopify_product_by_dbtable()

        # if updated:

        #     print("Done :- CheckAndUpdateProduct")
       
       