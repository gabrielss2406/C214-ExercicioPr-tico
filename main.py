from services.teacherSchedule import create_teacher_from_json

json_response = """
{
    "nomeDoProfessor": "John Doe",
    "horarioDeAtendimento": "09:00 - 12:00",
    "periodo": "morning",
    "sala": "101",
    "predio": ["1", "2", "3"]
}
"""

teacher = create_teacher_from_json(json_response)

print("Name:", teacher.name)
print("Schedule:", teacher.schedule)
print("Period:", teacher.period)
print("Room:", teacher.room)
print("Building:", teacher.building)

assert teacher.name == "John Doe", "Name test failed"
assert teacher.schedule == "09:00 - 12:00", "Schedule test failed"
assert teacher.period == "morning", "Period test failed"
assert teacher.room == "101", "Room test failed"
assert teacher.building == ["1", "2", "3"], "Building test failed"

print("All manual tests passed!")
