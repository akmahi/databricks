# Databricks notebook source
# Need to import to use date time 
from datetime import datetime, date 
  
# need to import for working with pandas 
import pandas as pd 
  
# need to import to use pyspark 
from pyspark.sql import Row 
# pyspark dataframe 
rdd = spark.sparkContext.parallelize([ 
    (1, 4., 'GFG1', date(2000, 8, 1), datetime(2000, 8, 1, 12, 0)), 
    (2, 8., 'GFG2', date(2000, 6, 2), datetime(2000, 6, 2, 12, 0)), 
    (3, 5., 'GFG3', date(2000, 5, 3), datetime(2000, 5, 3, 12, 0)) 
]) 
df = spark.createDataFrame(rdd, schema=['a', 'b', 'c', 'd', 'e']) 
df 
  
# show table 
df.show() 
  
# show schema 
df.printSchema() 
