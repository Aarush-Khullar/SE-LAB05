import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

# Global state
reservations = {}
equipment_pool = {"projector": 2, "microphone": 4, "webcam": 1}
conflicts = []
next_reservation = 1


def validate_time_slot(time_slot):
    """Validate a time slot formatted as HH-HH."""
    if not isinstance(time_slot, str) or not re.fullmatch(
        r"\d{1,2}-\d{1,2}", time_slot
    ):
        raise ValueError("Time slot must be formatted like 09-11.")

    start, end = map(int, time_slot.split("-"))
    if not (0 <= start < end <= 24):
        raise ValueError("Time slot must have a valid start and end.")

    return start, end


def schedule_room(room_id, time_slot, equipment_list=None):
    """Create a reservation if the room and equipment are available."""
    global next_reservation

    validate_time_slot(time_slot)
    equipment_list = list(equipment_list or [])

    for reservation in reservations.values():
        if (
            reservation["room"] == room_id
            and reservation["slot"] == time_slot
        ):
            message = f"{room_id} double-booked at {time_slot}"
            conflicts.append(message)
            raise ValueError(message)

    requested = Counter(equipment_list)

    for item, quantity in requested.items():
        if item not in equipment_pool:
            raise ValueError(f"Unknown equipment: {item}")
        if quantity > equipment_pool[item]:
            raise ValueError(f"Not enough equipment available: {item}")

    for item, quantity in requested.items():
        equipment_pool[item] -= quantity

    reservation_id = next_reservation
    reservations[reservation_id] = {
        "room": room_id,
        "slot": time_slot,
        "equipment": equipment_list,
    }
    next_reservation += 1
    return reservation_id


def cancel_reservation(reservation_id):
    """Cancel a reservation and return its equipment to the pool."""
    reservation = reservations.get(reservation_id)
    if reservation is None:
        return False

    for item in reservation["equipment"]:
        equipment_pool[item] += 1

    del reservations[reservation_id]
    return True


def slot_hours(time_slot):
    """Return the duration of a valid time slot in hours."""
    start, end = validate_time_slot(time_slot)
    return end - start


def export_schedule(file="schedule.json"):
    """Export all reservations to a JSON file."""
    with open(file, "w", encoding="utf-8") as output_file:
        json.dump(reservations, output_file, indent=4)


def log_conflicts(file="conflicts.log"):
    """Append conflict records and display the log safely."""
    with open(file, "a", encoding="utf-8") as output_file:
        for conflict in conflicts:
            output_file.write(f"{datetime.now()} {conflict}\n")

    log_path = Path(file)
    if log_path.exists():
        print(log_path.read_text(encoding="utf-8"))


def main():
    """Run the room scheduler demonstration."""
    schedule_room("Board-1", "09-11")

    try:
        schedule_room("Board-1", "09-11")
    except ValueError as error:
        print("Booking rejected:", error)

    try:
        slot_hours("14-12")
    except ValueError as error:
        print("Invalid slot rejected:", error)

    print("Missing reservation cancelled:", cancel_reservation(77))

    slot = input(
        "Slot for Board-2, like 10-12 (Enter for 10-12): "
    ).strip() or "10-12"

    try:
        schedule_room("Board-2", slot, ["projector", "webcam"])
    except ValueError as error:
        print("Booking rejected:", error)

    export_schedule()
    log_conflicts()
    print("Equipment left:", equipment_pool)
    print("Reservations:", reservations)


if __name__ == "__main__":
    main()

