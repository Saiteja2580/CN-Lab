# 1. Create simulator
set ns [new Simulator]

# 2. Setup trace file for animation
set tracefile [open out.tr w]
$ns trace-all $tracefile

set namfile [open out.nam w]
$ns namtrace-all $namfile

# 3. Set the routing protocol
$ns node-config -routingAgent DSDV

# 4. Create routers (nodes)
set r0 [$ns node]
set r1 [$ns node]
set r2 [$ns node]
set r3 [$ns node]

# 5. Connect routers
$ns duplex-link $r0 $r1 1Mb 10ms DropTail
$ns duplex-link $r1 $r2 1Mb 10ms DropTail
$ns duplex-link $r2 $r3 1Mb 10ms DropTail
# Initially, no direct link between r0 and r3

# 6. Schedule the addition of a new link (topology change)
$ns at 3.0 "$ns duplex-link $r0 $r3 1Mb 10ms DropTail"

# 7. Set a simple traffic flow
set udp [new Agent/UDP]
$ns attach-agent $r0 $udp

set null [new Agent/Null]
$ns attach-agent $r3 $null

$ns connect $udp $null

set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set packetSize_ 500
$cbr set interval_ 0.5

# Start sending traffic
$ns at 1.0 "$cbr start"
$ns at 7.0 "$cbr stop"

# 8. Stop simulation
$ns at 10.0 "finish"

proc finish {} {
    global ns tracefile namfile
    $ns flush-trace
    close $tracefile
    close $namfile
    exec nam out.nam &
    exit 0
}

# 9. Run simulation
$ns run
