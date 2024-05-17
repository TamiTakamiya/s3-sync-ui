# s3-sync-ui
## Summary

This is an utility to sync data from AWS S3 bucket to local directory using `aws s3 sync` command.

**This tool works under a very special situation, in which S3 buckets are organized using epoch time (in msecs)
like:**

```
    :
{S3_BUCKET_ROOT}/1710028800000/
{S3_BUCKET_ROOT}/1710115200000/
{S3_BUCKET_ROOT}/1710201600000/
{S3_BUCKET_ROOT}/1710288000000/
{S3_BUCKET_ROOT}/1710374400000/
    :
```

## Execution

1. Make sure that AWS CLI works and you can run `aws s3 sync` command from command line.
1. Set `S3_BUCKET_ROOT` envvar to point to the root bucket without setting the trailing slash (`/`)
1. Run
```
python3 src/main.py
```
1. Open http://127.0.0.1:8080 on browser
1. Specify start and end dates to specify the date range
1. Enter Submit
1. Check console outputs to see no errors are found.
1. If the `aws s3 sync` coomands are executed successfully, `Ok` is displayed on browser and data are stored in the `data/raw` directory.