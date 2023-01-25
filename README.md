# Auto-create-content-linkedin-GPT
Just run the cells on generate-post-content.ipynb. 

Linkedin API code based on https://www.jcchouinard.com/authenticate-to-linkedin-api-using-oauth2/ series

create a credentials.json file in the root directory following this structure:
```json
{
    "client_id": "XXXXXXXX",
    "client_secret": "XXXXXXXX",
    "redirect_uri": "http://localhost:8080",
    "openai_access_token": "XXXXXXXX"
}
