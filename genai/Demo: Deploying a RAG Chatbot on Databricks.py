# Databricks notebook source
# MAGIC %md
# MAGIC # Demo: Deploying a RAG Chatbot on Databricks

# COMMAND ----------

# MAGIC %pip install dbdemos

# COMMAND ----------

import dbdemos
dbdemos.install('llm-rag-chatbot')
dbdemos.install('llm-rag-chatbot', catalog='dev', schema='rag_chatbot')

# COMMAND ----------


