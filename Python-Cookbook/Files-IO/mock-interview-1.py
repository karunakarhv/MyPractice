def packets_reorder_optimized(packets):
    if not packets:
        return []

    # 1. Find the range in one pass (O(N))
    max_idx = max(p['index'] for p in packets)
    
    # 2. Create a "buffer" filled with None (Pre-allocation)
    # This acts like the 'Jitter Buffer' in real audio hardware
    buffer = [None] * (max_idx + 1)
    
    # 3. Fill the buffer (O(N))
    for p in packets:
        print(f"Placing {p['data']} at index {p['index']}")
        buffer[p['index']] = p['data']
        
    return buffer

# Test
packets = [
    {"index": 2, "data": "AUDIO_PART_3"},
    {"index": 0, "data": "AUDIO_PART_1"},
    {"index": 3, "data": "AUDIO_PART_4"}
]
print(packets_reorder_optimized(packets))