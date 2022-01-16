from enum import Enum


class StatusEnum(Enum):
    PROCESS = "PROCESS"
    COMPLETED = "COMPLETED"
    WAIT = "WAIT"
    INITIATED = "INITIATED"
    DENIED = "DENIED"
    FAIL = "FAIL"
