import boto3
from sqs_service import send_message_to_queue

def recurring_event_handler(event, context):
    print("**** RecurringEvents.recurring_event_handler")
    my_kwargs = event.get('kwargs')
    print(f"***** kwargs: {my_kwargs}")

    return 'Done'


def every_2_mins(event, context):
    print("**** RecurringEvents.every_2_mins")
    my_kwargs = event.get('kwargs')
    print(f"***** kwargs: {my_kwargs}")

    msg_id, md5_of_msg = send_message_to_queue("Hello Zappa SQS CloudWatch World...", 'zappa-test-queue')

    print("Notification sent with message id: %s" % msg_id)

    return 'Done'
