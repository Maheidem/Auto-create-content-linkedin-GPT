import openai_secret_manager
import openai
import requests
import json

# Get API key
secrets = openai_secret_manager.get_secrets("openai")
openai.api_key = secrets["api_key"]

# Generate data science content
prompt = "Write a data science article"
completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
)

# Get the first generated content
generated_text = completions.choices[0].text

# Post to LinkedIn
# Replace {access_token} and {user_id} with your own LinkedIn account information
access_token = "your_access_token"
user_id = "your_user_id"
post_url = f"https://api.linkedin.com/v2/ugcPosts"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}
post_data = {
    "author": f"urn:li:person:{user_id}",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": generated_text
            },
            "shareMediaCategory": "ARTICLE",
        },
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    },
}
response = requests.post(post_url, headers=headers, json=post_data)

# Print response
print(response.text)
