record_seconds = float(input())
distance_meters = float(input())
seconds_for_1_meter = float(input())

latency = (distance_meters // 15) * 12.5
swimming_record = (distance_meters * seconds_for_1_meter) + latency

if record_seconds > swimming_record:
    print(f"Yes, he succeeded! The new world record is {swimming_record:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(record_seconds - swimming_record):.2f} seconds slower.")