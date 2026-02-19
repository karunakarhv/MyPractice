#Task: Write a Python class HeartbeatMonitor that:
#Has a method receive_ping(timestamp) that records when a ping arrived.
#Has a method is_connection_stable(current_time) that returns False 
# if the gap between any two pings was greater than 5 seconds, or if the last ping was more than 5 seconds ago.

class HeartbeatMonitor:
    def __init__(self):
        self.pings = []

    def receive_ping(self, timestamp):
        self.pings.append(timestamp)

    def is_connection_stable(self, current_time):
        if not self.pings:
            return False

        # Check if the last ping was more than 5 seconds ago
        if current_time - self.pings[-1] > 5:
            return False

        # Check gaps between consecutive pings
        for i in range(1, len(self.pings)):
            if self.pings[i] - self.pings[i-1] > 5:
                return False

        return True

# Example usage
monitor = HeartbeatMonitor()
monitor.receive_ping(0)  # Ping at time 0
monitor.receive_ping(3)  # Ping at time 3
print(monitor.is_connection_stable(4))  # True, last ping was 1 second ago
print(monitor.is_connection_stable(9))  # False, last ping was 6 seconds ago
monitor.receive_ping(10) # Ping at time 10
print(monitor.is_connection_stable(12)) # True, last ping was 2 seconds ago