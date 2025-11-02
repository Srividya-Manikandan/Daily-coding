"""This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed."""

def count_decodings(message):
    # Handle edge cases - empty string or leading '0' (like '001', though 1 has 'a' mapping 0 is invalid thus combinations starting with 0 are invalid)
    if not message or message[0] == '0':
        return 0

    n = len(message)
    dp = [0] * (n + 1)

    dp[0] = 1  # An empty string has one way to decode
    dp[1] = 1  # A single character (not '0') has one way to decode

    for i in range(2, n + 1):
        one_digit = int(message[i-1:i])  # Last one digit
        two_digit = int(message[i-2:i])  # Last two digits

        # Check if the last one digit is valid (1-9)
        if 1 <= one_digit <= 9:
            dp[i] += dp[i - 1]

        # Check if the last two digits are valid (10-26)
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]