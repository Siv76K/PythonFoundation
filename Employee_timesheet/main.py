from pydantic import BaseModel, Field

class TimesheetCreate(BaseModel):
    projectId: int
    userId: int
    hours: float = Field(gt=0, le=24)
    isApproved: bool = Field(default=False)

user_entry = TimesheetCreate(
    projectId=500,
    userId=10,
    hours=6.5,
    isApproved=False
)

def timesheet_validator(entry: TimesheetCreate) -> str:
    # Hours must not be less than 0
    if(entry.hours < 0):
        return "Hours cannot be less than 0"

    # Hours cannot exceed than 10
    if(entry.hours > 10):
        return "Hours cannot be greater than 10 per day"

    # approved timesheets cannot be edited
    if(entry.isApproved == True):
        return "You cannot edit the approved Timesheet"
    
    return "Valid"

result = timesheet_validator(user_entry)
print(result)