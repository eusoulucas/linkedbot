import json
from linkedin_api import Linkedin

# Authenticate your API key and secret
client = Linkedin(access_token='YOUR_API_KEY')

# Specify the keywords you want to search for
keywords = 'software engineer'

# Use the search_jobs method to search for jobs matching the specified keywords
response = client.search_jobs(keywords=keywords)

# Get the list of jobs from the search results
jobs = response['elements']

# Loop through the list of jobs and apply for each one
for job in jobs:
    job_id = job['id']
    # use the apply method to apply for the job
    application = client.apply_job(job_id)
    print(f"Application for job {job_id} was sent.")
    # Print the application status
    print(json.dumps(application, indent=2))
