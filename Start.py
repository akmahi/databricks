# Databricks notebook source


# Need to import to use date time 
from datetime import datetime, date 
  
# need to import for working with pandas 
import pandas as pd 
  
# need to import to use pyspark 
from pyspark.sql import Row 

df = spark.createDataFrame([ 
    Row(a=1, b=4., c='GFG1', d=date(2000, 8, 1), 
        e=datetime(2000, 8, 1, 12, 0)), 
    
    Row(a=2, b=8., c='GFG2', d=date(2000, 6, 2),  
        e=datetime(2000, 6, 2, 12, 0)), 
    
    Row(a=4, b=5., c='GFG3', d=date(2000, 5, 3), 
        e=datetime(2000, 5, 3, 12, 0)) 
]) 

df.show() 
  
# show schema 
df.printSchema() 
