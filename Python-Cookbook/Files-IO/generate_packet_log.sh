#!/bin/zsh
# Generate a 1GB (~1000000000 bytes) synthetic network packet log

target_size=1000000000 # 1GB
out_file="network_packet_log.txt"

echo "Generating $out_file ~1GB. Please wait..."

protocols=(TCP UDP ICMP)
flags=(SYN ACK PSH FIN RST URG ECE CWR)

function random_ip() {
  echo "$((RANDOM%256)).$((RANDOM%256)).$((RANDOM%256)).$((RANDOM%256))"
}

function random_port() {
  echo "$((1000 + RANDOM%55000))"
}

function random_protocol() {
  echo "${protocols[$((RANDOM%${#protocols[@]}+1))]}"
}

function random_flag() {
  echo "[${flags[$((RANDOM%${#flags[@]}+1))]}]"
}

function log_line() {
  local ts="$(date '+%Y-%m-%d %H:%M:%S').$(( RANDOM % 1000000 ))"
  local proto=$(random_protocol)
  local src_ip=$(random_ip)
  local src_port=$(random_port)
  local dst_ip=$(random_ip)
  local dst_port=$(random_port)
  local size="$(( 40 + RANDOM % 1400 ))"
  local flag=$(random_flag)
  echo "$ts $proto $src_ip:$src_port > $dst_ip:$dst_port $flag $size bytes"
}

# Start writing logs
touch "$out_file"
current_size=$(stat -f%z "$out_file")

while [[ $current_size -lt $target_size ]]; do
  log_line >> "$out_file"
  current_size=$(stat -f%z "$out_file")
done

echo "Done: $out_file created $(du -h "$out_file")"
EOF
