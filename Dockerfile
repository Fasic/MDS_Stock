FROM python:3.13
ENV PYTHONUNBUFFERED 1

LABEL image.name="mds_stock_api"
LABEL image.tag="mds_stock_api:latest"

COPY . /app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

EXPOSE 8080
EXPOSE 5432
WORKDIR app

RUN pip install -r requirements.txt
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
