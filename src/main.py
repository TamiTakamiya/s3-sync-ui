import os
from datetime import datetime
from bottle import route, run, request

@route("/")
def main_page():
    return """
    <h2>Sync s3 data</h2>
    <form action="/input" method="post">
        <label for="start">Start date:</label>
        <input type="date" id="start" name="sync-start" value="2024-01-01" min="2023-04-18" max="2099-12-31" />
        <label for="start">End date:</label>
        <input type="date" id="start" name="sync-end" value="2024-02-29" min="2023-04-18" max="2099-12-31" />
        <input value="Enter" type="submit"/>
    </form>
"""

@route("/input", method="POST")
def input():
    def epoch_time(date_string):
        utc_time = datetime.strptime(date_string, "%Y-%m-%d")
        return int((utc_time - datetime(1970, 1, 1)).total_seconds())
    start_date = request.forms.get("sync-start")
    end_date = request.forms.get("sync-end")

    day_in_seconds = 24 * 60 * 60
    epoch = epoch_time(start_date)
    epoch_end = epoch_time(end_date)
    while epoch <= epoch_end:
        sync_cmd = f"aws s3 sync s3://{os.getenv['S3_BUCKET_ROOT']}/{epoch}000/ data/raw"
        rc = os.system(sync_cmd)
        if rc:
            return "Error"
        epoch += day_in_seconds
    return "Ok"

def main():
    if not os.getenv("S3_BUCKET_ROOT"):
        print("Specify S3_BUCKET_ROOT envvar")
    else:
        if not os.path.isdir("data/raw"):
            os.makedirs("data/raw")
        run(host='localhost', port=8080, debug=True)

if __name__ == "__main__":
    main()
