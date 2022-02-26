from enum import Enum


class STATE(Enum):

    # Conversation states
    FEATURE_SELECTION = 1

    PHISHING_CHECK = 10
    PHISING_GET_LINK = 11

    REPORT = 20
    REPORT_GET_LINK = 21

    ABOUT = 30

    # Meta states
    SHOWING = 1000
    BACK = 1001
    STOPPING = 1002
    START_OVER = 1004

    END = -1.


class CONSTANTS:

    START_OVER = "start_over"