__author__ = 'goldi'
import boto
import boto.ec2

boto.set_stream_logger('boto')
# s3 = boto.connect_s3()
# available_regions=boto.s3.regions()
# for regions in available_regions:
#   print regions
list_ec2_instances = boto.ec2.regions()
print list_ec2_instances
my_region = boto.ec2.connect_to_region("us-east-1")
my_region.run_instances('ami-81e239ea')


# for bucket in s3.buckets.all();
#   print(bucket.name)

# import boto3
#
#
# Let's use Amazon S3
# s3 = boto3.resource('s3')
# Print out bucket names
# for bucket in s3.buckets.all():
#   print(bucket.name)i

# s3 = boto3.resource('s3')
# Print out bucket names
# for bucket in s3.buckets.all():
#   print(bucket.name)i
