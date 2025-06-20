import requests
import json

TEAMS_WEBHOOK_URL = "https://outlook.office.com/webhook/..."  # Replace with actual webhook

def send_teams_notification(name, email, department, issue, ticket_id):
    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "summary": f"New Help Desk Ticket #{ticket_id}",
        "themeColor": "0078D7",
        "title": f"🎫 Ticket #{ticket_id} Submitted",
        "sections": [{
            "facts": [
                {"name": "Name", "value": name},
                {"name": "Email", "value": email},
                {"name": "Department", "value": department},
                {"name": "Issue", "value": issue}
            ],
            "markdown": True
        }]
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(TEAMS_WEBHOOK_URL, headers=headers, data=json.dumps(payload))
    return response.status_code
