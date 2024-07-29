import pylhe

# Read a sample LHE file to inspect its structure
events = pylhe.read_lhe('EventOutput.Pert.00000001.lhe')

# Initialize a counter to limit the number of events to inspect
num_events_to_inspect = 12000
event_counter = 0

# Open a file to write the output
output_file = open('output2.txt', 'w')

# Iterate over the events to inspect their structure
for event in events:
    if event_counter >= num_events_to_inspect:
        break

    output_file.write(f"Event {event_counter + 1}:\n")
    output_file.write(f"Event ID: {event.eventinfo}\n")
    output_file.write(f"Event Weight: {event.eventinfo.weight}\n")

    num_particles = len(event.particles)
    output_file.write(f"Number of particles in the event: {num_particles}\n")
    # Write information about particles in the event
    for particle in event.particles[:10]:  # Write details of the first 10 particles
        output_file.write(f"Particle ID: {particle.id}, Status: {particle.status}, px: {particle.px}, py: {particle.py}, pz: {particle.pz}, energy: {particle.e}, mass: {particle.m}\n")

    output_file.write("--------------------\n")

    event_counter += 1

# Close the file
output_file.close()

print("Output has been saved to 'output2.txt'")
