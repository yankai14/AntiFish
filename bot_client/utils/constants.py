from enum import Enum


class STATE(Enum):

    # Conversation states
    FEATURE_SELECTION = 1

    PHISHING_CHECK = 10

    REPORT = 20

    ABOUT = 30

    # Meta states
    SHOWING = 1000
    BACK = 1001
    STOPPING = 1002
    END = 1003
    START_OVER = 1004


class CONSTANTS:

    START_OVER = "start_over"