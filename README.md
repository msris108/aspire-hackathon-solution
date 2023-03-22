# Aspire Hackathon 2023

## Services
1. Backend core, with SSO(OTP login)
2. Frontend React + Redux
3. Logging and Monitoring services (Not configured properly yet)  

- Check the issues for issues to be resolved before hackathon
- Check Individual readmes at aspire-backend and aspire-frontend

|Service|Port|Notes|
|---|---|---|
|Backend|8000|Django, Django-Restframework|
|Frontend|3001|React, Redux|
|Prometheus|9090|Metrics|
|Grafana|3000|Metrics but fancier with Dashboards|
|Elastisearch|9200|Fast Search of ORM data|
|Logstash|5959|Logging and tracing|
|Kibana|5601|UI for all that logging|

> docker-compose -f docker-compose.yaml up

In an ideal world everything would start running with the above command, unfortunately we don't live in an ideal world :)  

Check out localhost:3001/login for logging in _and_ localhost:8000/auth/email to get started

