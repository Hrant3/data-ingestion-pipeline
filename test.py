import feedparser


def find_min_pledge(pledge_list):
    # Step 1: Filter out non-positive numbers
    positive_pledges = set(x for x in pledge_list if x > 0)

    # Step 2: Find the smallest missing positive integer
    smallest_missing = 1
    while smallest_missing in positive_pledges:
        smallest_missing += 1

    return smallest_missing
#
#
# # Test cases
# assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
# assert find_min_pledge([1, 2, 3]) == 4
# assert find_min_pledge([-1, -3]) == 1
#
# print("All test cases passed!")


def get_headlines(rss_url):
    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # Extract the titles from the entries
    headlines = [entry.title for entry in feed.entries]

    return headlines

google_news_url = "https://news.google.com/news/rss"
# print(get_headlines(google_news_url))
#


import io


# Simulate the stream_payments function
def stream_payments(callback_fn):
    """ Simulate streaming payments by calling the callback function with each payment. """
    for i in range(10):
        callback_fn(i)  # Simulate a payment with values 0 to 9


# Simulate the store_payments function
def store_payments(amount_iterator):
    """ Simulate storing payments by iterating over the payment amounts. """
    for amount in amount_iterator:
        print(f"Storing payment: {amount}")  # Print the payment amount being stored


# First implementation using a list to accumulate payments
def payment_generator():
    """ Generator to yield payments one by one. """
    payment_queue = []

    def callback_fn(amount):
        """ Callback function to be passed to stream_payments. """
        payment_queue.append(amount)
     # - DATABASE_URL=postgresql://user:password@db:5432/metrics_db
      #- DATABASE_URL = "postgresql://user:password@localhost:5432/metrics_db"
    # Stream payments and populate the payment_queue via callback
    stream_payments(callback_fn)

    # Yield from the queue as we receive payments
    while payment_queue:
        yield payment_queue.pop(0)


def process_payments_2():
    """ Process payments by streaming and then storing them. """
    # Create the payment generator
    payments = payment_generator()

    # Store payments using the generator
    store_payments(payments)


# Run the process to see it in action
process_payments_2()



