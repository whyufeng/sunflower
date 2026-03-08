# AWS Lambda Deployment Guide (Console UI)

We have successfully prepared your code for AWS Lambda. This guide will show you how to deploy it using the **AWS Management Console** instead of the command line.

## Prerequisites
1. You must have an AWS Account and be logged into the [AWS Management Console](https://console.aws.amazon.com/).
2. You need Python installed on your local machine to package the dependencies.

## Step 1: Package Your Code and Dependencies
Since AWS Lambda requires all dependencies to be included, we need to create a ZIP file containing your code and libraries.

1. Open a terminal in your project folder (`c:\Users\whyuf\Desktop\SunFlower`).
2. Create a deployment folder and install dependencies into it:
   ```bash
   mkdir package
   pip install -r requirements.txt -t package/
   ```
3. Copy your project code (e.g., `services/`, `scripts/daily_notify.py`) into the `package/` folder.
4. Compress the contents of the `package/` folder into a `.zip` file (e.g., `sunflower_lambda.zip`). **Make sure you zip the contents, not the folder itself.** The `daily_notify.py` should be at the root of the zip file.

## Step 2: Create the Lambda Function
1. Go to the **AWS Console** and search for **Lambda**.
2. Click **Create function**.
3. Choose **Author from scratch**.
4. **Function name**: `DailyNotify` (or another name you prefer).
5. **Runtime**: Select `Python 3.10` or newer.
6. **Architecture**: Leave as `x86_64`.
7. Click **Create function**.

## Step 3: Upload Your Code
1. In your new Lambda function page, scroll down to the **Code source** section.
2. Click the **Upload from** button and select **.zip file**.
3. Click **Upload**, select the `sunflower_lambda.zip` file you created in Step 1, and click **Save**.

## Step 4: Configure the Handler
Lambda needs to know which file and function to execute.
1. Scroll down to the **Runtime settings** section (below the code editor).
2. Click **Edit**.
3. Change the **Handler** to `scripts.daily_notify.lambda_handler` (assuming your file is in a `scripts` folder and has a `lambda_handler` function). 
   *(If you moved `daily_notify.py` to the root of the zip, it would just be `daily_notify.lambda_handler`)*
4. Click **Save**.

## Step 5: Configure Environment Variables
1. Click on the **Configuration** tab in your Lambda function.
2. Select **Environment variables** on the left menu.
3. Click **Edit**, then **Add environment variable**.
4. Add the following variables with your actual values:
   - Key: `TELEGRAM_BOT_TOKEN`, Value: `your_token_here`
   - Key: `TELEGRAM_CHAT_ID`, Value: `your_chat_id_here`
5. Click **Save**.

## Step 6: Setup EventBridge (Cron Job Scheduler)
To make this run daily automatically:
1. In your Lambda function overview at the top, click **Add trigger**.
2. From the dropdown, select **EventBridge (CloudWatch Events)**.
3. Select **Create a new rule**.
4. **Rule name**: `DailyNotificationSchedule`
5. **Rule type**: Select `Schedule expression`.
6. **Schedule expression**: Enter your desired time in UTC cron format. For example, to run every day at 8 AM UTC: `cron(0 8 * * ? *)`
7. Click **Add**.

## Step 7: Test Your Function
1. Click on the **Test** tab.
2. Create a new test event (the event JSON doesn't matter, you can leave the default).
3. Click **Test**.
4. Check your Telegram to see if the message arrived successfully!
