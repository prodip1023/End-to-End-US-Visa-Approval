# from us_visa.logger import logging
# from us_visa.exception import USvisaException
# import sys


# try:
#     r = 3/0
#     print(r)
# except Exception as e:
#     logging.info(e)
#     raise USvisaException(e, sys)


from us_visa.pipline.training_pipeline import TrainingPipeline


pipeline = TrainingPipeline()
pipeline.run_pipeline()