from linkedin import LinkedInApplication

# Authenticate using your LinkedIn API key
api_key = "YOUR_API_KEY"
secret_key = "YOUR_SECRET_KEY"

authentication = LinkedInApplication(api_key, secret_key)

# Define your list of keywords
keywords = ["Python", "Bot", "Automation"]

# Search for jobs using the LinkedIn Jobs Search API
jobs = authentication.search_job(keywords=keywords, job_filters={'easy_apply_filter': True})

# Iterate through the list of jobs and apply for each one
for job in jobs['jobs']['values']:
    job_id = job['id']
    # Create a draft application for the job
    application = {
        "jobId": job_id,
        "applyDetails": {
            "applicationText": "I am interested in this job and believe my skills and experience make me a great fit for the role."
        }
    }

    application_response = authentication.create_job_application(job_id, job_application=application)

    # Check the response from the API and submit the application if it is successful
    if application_response:
        application_id = application_response['id']
        submit_response = authentication.submit_job_application(application_id)
        if submit_response:
            print(f"Application submitted for job {job_id}")
        else:
            print("Failed to submit application")
    else:
        print("Failed to submit application")

