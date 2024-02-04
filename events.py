import requests
import time


def check_events():
    r = requests.request(method="get", url="https://api.torn.com/user/?selections=events&key=????????????????")
    return r.json()


if __name__ == '__main__':
    event1 = ""
    while True:
        events = check_events()
        print(events)

        if event1 == events:
            time.sleep(10)
            continue
        else:
            event1 = events

        for event in events["events"]:
            if "Bottle" in events["events"][event]["event"]:
                s = str(events["events"][event]["event"])[75::].replace("</a>","")
                print(s, "\n")
            elif "initiated" in events["events"][event]["event"]:
                s = str(events["events"][event]["event"])[75::].replace("</a>", "").split(" <A")[0]
                print(s, "\n")
            elif "finalize" in events["events"][event]["event"]:
                s = str(events["events"][event]["event"])[75::].replace("</a>", "").split(" <A")[0]
                print(s, "\n")
        time.sleep(10)
