FROM public.ecr.aws/lambda/python:3.11

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r requirements.txt

# Copy function code and services
COPY scripts/daily_notify.py ${LAMBDA_TASK_ROOT}
COPY services/ ${LAMBDA_TASK_ROOT}/services/

# Set the CMD to your handler
CMD [ "daily_notify.lambda_handler" ]
