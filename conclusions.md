# Grafana + Loki

## Considerations:
- Data model can be constructed using labels, but it has some limitations on data types (keys and values must be strings)
- There are many clients for ingestion but they look at some "log" file to compress it and push it to loki, so it must have access to the logging system
- Ingestion from serverless functions must be of push mode
- Ingestion performance for batched data is not good (each line must be logged).
- Loki stores data using streams and chunks defined by labels, many labels leads to a high dardinality:
  - https://grafana.com/docs/loki/latest/get-started/labels/#cardinality
  "Doing some quick math, if there are maybe four common actions (GET, PUT, POST, DELETE) and maybe four common status codes (although there could be more than four!), this would be 16 streams and 16 separate chunks"
  "When we talk about cardinality we are referring to the combination of labels and values and the number of streams they create"
  High cardinality causes Loki to build a huge index and to flush thousands of tiny chunks to the object store


## Best practice:
- To avoid those issues, don’t add a label for something until you know you need it! Use filter expressions (|= "text", |~ "regex", …) and brute force those logs. It works – and it’s fast.

## Limitations:
- Data model must be denormalized and meaningful values must be in the log line


# Power BI

## Considerations
- PBI is not for logs, it should be processed to create the data model


# Comparisons
- Calculations are easier to implement in grafana thanks to built-ins
- PBI required the records to have a date column, while grafana add it automatically in the tsdb
- PBI is more interactive, while grafana is not
- PBI can create dashboard, which group reports and can add real time visuals
- 
