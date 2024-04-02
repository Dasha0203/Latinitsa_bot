
FROM python:3.12-slim
ENV TOKEN="6838809615:AAFx3Q0Fks9WUfn03y6uGdxC075GS-rRlbA"
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]