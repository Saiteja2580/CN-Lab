# 1. Create a simulator
set ns [new Simulator]

# 2. Setup trace and NAM files for recording
set tracefile [open out.tr w]
$ns trace-all $tracefile

set namfile [open out.nam w]
$ns namtrace-all $namfile

# 3. Create the central hub (node)
set hub [$ns node]

# 4. Create devices (nodes)
set device1 [$ns node]
set device2 [$ns node]
set device3 [$ns node]
set device4 [$ns node]

# 5. Connect devices to the hub
$ns duplex-link $device1 $hub 1Mb 10ms DropTail
$ns duplex-link $device2 $hub 1Mb 10ms DropTail
$ns duplex-link $device3 $hub 1Mb 10ms DropTail
$ns duplex-link $device4 $hub 1Mb 10ms DropTail

# 6. Setup traffic: device1 sends data to device3

# Attach agents
set udp [new Agent/UDP]
$ns attach-agent $device1 $udp

set null [new Agent/Null]
$ns attach-agent $device3 $null

# Connect sender and receiver
$ns connect $udp $null

# Setup CBR (Constant Bit Rate) application
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set packetSize_ 500
$cbr set interval_ 0.5

# Start and stop the traffic
$ns at 1.0 "$cbr start"
$ns at 5.0 "$cbr stop"

# 7. Finish simulation after 6 seconds
$ns at 6.0 "finish"

# Define finish procedure
proc finish {} {
    global ns tracefile namfile
    $ns flush-trace
    close $tracefile
    close $namfile
    exec nam out.nam &
    exit 0
}

# 8. Run the simulation
$ns run
