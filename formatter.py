
def format_event(event):
    event_type = event['type']
    repo = event['repo']['name']
    payload = event['payload']
    
    match event_type:
        case "PushEvent":   
            ref = payload['ref']
            return f"Pushed to {repo} on ({ref})"
        
        case "WatchEvent":
            return f"Starred {repo}"
        
        case "ForkEvent":
            full_name = payload['forkee']['full_name']
            return f"Forked {repo} to {full_name}"
        
        case "IssueCommentEvent":
            title = payload['issue']['title']
            return f"Commented on '{title}' on {repo}"
        
        case "PullRequestEvent":
            action = payload['action']
            number = payload['number']
            return f"{action} pull request #{number} on {repo}"
        
        case "PullRequestReviewEvent":
            review_state = payload['review']['state']
            number = payload['pull_request']['number']
            return f"Reviewed {review_state} pull request #{number} on {repo}"
        
        case "CreateEvent":
            ref_type = payload['ref_type']
            ref = payload['ref']
            return f"Created {ref_type} {ref} on {repo}"
        
        case "DeleteEvent":
            ref_type = payload['ref_type']
            ref = payload['ref']
            return f"Deleted {ref_type} {ref} on {repo}"
        
        case "IssuesEvent":
            action = payload['action']
            title = payload['issue']['title']
            return f"{action} issue '{title}' on {repo}"
        
        case _:
            return f"{event_type} on {repo}"
        
        
        
def format_activity_list(username, events):
    lines = []
    
    header = f"Recent activity for {username}: {len(events)} events found."
    lines.append(header)
    
    if not events:
        lines.append("No recent activity found.")
    else:
        lines.append("--------------------------------")
        for event in events:
            lines.append(format_event(event))

    return "\n".join(lines)

