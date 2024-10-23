import os
import json
import time
import tkinter as tk
from tkinter import Label
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Define the scopes for Google Fit
SCOPES = ['https://www.googleapis.com/auth/fitness.heart_rate.read']


# Function to authenticate and get Google Fit service
def get_google_fit_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('fitness', 'v1', credentials=creds)
    return service


# Function to fetch heart rate data from Google Fit
def fetch_heart_rate_data():
    service = get_google_fit_service()
    data_sources = service.users().dataSources().list(userId='me').execute()

    for data_source in data_sources['dataSource']:
        if 'heart_rate' in data_source['dataStreamName'].lower():
            dataset = service.users().dataSources().datasets().get(
                userId='me',
                dataSourceId=data_source['dataStreamId'],
                datasetId=f'0-{int(time.time() * 1000000000)}').execute()

            heart_rates = []
            for point in dataset['point']:
                for value in point['value']:
                    heart_rate = value.get('fpVal')
                    if heart_rate:
                        heart_rates.append(heart_rate)

            if heart_rates:
                return heart_rates[-1]  # Return the latest heart rate
    return None


# Tkinter window to display heart rate
class HeartRateApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Heart Rate Data")
        self.geometry("400x200")

        # Label to display the heart rate
        self.heart_rate_label = Label(self, text="Heart Rate: Fetching...", font=("Arial", 20))
        self.heart_rate_label.pack(pady=50)

        # Fetch heart rate and update the label
        self.update_heart_rate()

    def update_heart_rate(self):
        heart_rate = fetch_heart_rate_data()
        if heart_rate:
            self.heart_rate_label.config(text=f"Heart Rate: {heart_rate} BPM")
        else:
            self.heart_rate_label.config(text="Heart Rate: No data")

        # Update every 60 seconds
        self.after(60000, self.update_heart_rate)


if __name__ == "__main__":
    app = HeartRateApp()
    app.mainloop()
