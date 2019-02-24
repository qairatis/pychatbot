bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Import the random module
import random
import re

# Define a dictionary containing a list of responses for each message
responses = {'default': 'default message',
 'goodbye': 'goodbye for now',
 'greet': 'Hello you! :)',
 'thankyou': 'you are very welcome'}

rules = {'I want (.*)': ['What would it mean if you got {0}',
                         'Why do you want {0}',
                         "What's stopping you from getting {0}"],
 'do you remember (.*)': ['Did you think I would forget {0}',
                          "Why haven't you been able to forget {0}",
                          'What about {0}',
                          'Yes .. and?'],
 'do you think (.*)': ['if {0}? Absolutely.',
                       'No chance'],
 'if (.*)': ["Do you really think it's likely that {0}",
             'Do you wish that {0}',
             'What do you think about {0}',
             'Really--if {0}']
}

patterns = {'goodbye': re.compile(r'bye|farewell', re.UNICODE),
 'greet': re.compile(r'hello|hi|hey', re.UNICODE),
 'thankyou': re.compile(r'thank|thx', re.UNICODE)}

# Define a function to find the intent of a message
def match_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message
        if pattern.search(message):
            matched_intent = intent
    return matched_intent


# Define a respond function
def respond(message):
    # Call the match_intent function
    intent = match_intent(message)
    # Fall back to the default response
    key = "default"
    if intent in responses:
        key = intent
    return responses[key]


# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


# Define match_rule()
def match_rule(rules, message):
    response, phrase = "default", None
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response, phrase


# Define replace_pronouns()
def replace_pronouns(message):
    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub('me', 'you', message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub('my', 'your', message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub('your', 'my', message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub('you', 'me', message)

    return message


# Send messages
send_message("hello!")
send_message("bye byeee")
send_message("thanks very much!")